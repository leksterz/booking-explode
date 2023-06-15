from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Request, Schedule
from datetime import datetime, timedelta, timezone
from django.views import generic
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.utils import timezone
from .forms import ScheduleForm, ScheduleRequestForm
import logging
from django.views.generic.edit import CreateView
from django.contrib import messages


class ScheduleListView(generic.ListView):
    model = Schedule
    template_name = 'frontend/schedule.html'
    context_object_name = 'schedule_list'
    paginate_by = 5

    def get_queryset(self):
        offset = self.kwargs['offset']
        date = timezone.localtime() + timezone.timedelta(days=offset)
        queryset = super().get_queryset().filter(date=date)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.localtime()
        prev_date = (now - timezone.timedelta(days=1)).date()
        next_date = (now + timezone.timedelta(days=1)).date()
        context['prev_url'] = reverse_lazy('frontend:schedule', args=[prev_date])
        context['next_url'] = reverse_lazy('frontend:schedule', args=[next_date])
        context['form'] = ScheduleRequestForm(offset=self.kwargs['offset'])
        return context

logger = logging.getLogger(__name__)

class ScheduleRequestView(FormView):
    form_class = ScheduleRequestForm
    template_name = 'frontend/request.html'
    success_url = reverse_lazy('frontend:request')

    def form_valid(self, form):
        selected_time_slots = form.cleaned_data['time_slots']
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        date = selected_time_slots[0].date

        # Extract the start time and end time from the selected time slots.
        start_time = selected_time_slots.first().start_time
        end_time = selected_time_slots.last().end_time

        try:
            # Save the request object.
            request = Request.objects.create(
                name=name,
                email=email,
                date=date,
                start_time=start_time,
                end_time=end_time,
                status='pending'
            )

            # Update the selected time slots.
            for slot in selected_time_slots:
                slot.is_selected = True
                slot.save()
            
            logger.info(f"New request created: {request}")
            
            # Add a success message.
            messages.success(self.request, 'Your request has been submitted successfully!')
            logger.info('Form submission successful! Message passed: %s' % self.request.POST.get('message', ''))
            logger.info(messages.get_messages(self.request))
            return super().form_valid(form)

        except Exception as e:
            logger.exception(f"Error occurred while creating request: {e}")
            return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        offset = int(self.kwargs.get('offset', '0'))
        date = timezone.localtime() + timezone.timedelta(days=offset)
        queryset = Schedule.objects.filter(date=date)
        context['schedule_list'] = queryset
        context['form'] = ScheduleRequestForm(offset=offset)
        now = timezone.localtime()
        prev_date = (now - timezone.timedelta(days=1)).date()
        next_date = (now + timezone.timedelta(days=1)).date()
        context['prev_url'] = reverse_lazy('frontend:request', kwargs={'offset': offset-1})
        context['next_url'] = reverse_lazy('frontend:request', kwargs={'offset': offset+1})
        context['messages'] = messages.get_messages(self.request)
        return context