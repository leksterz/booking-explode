from django import forms
from .models import Schedule, Request
from django.utils import timezone
from django.forms.widgets import SelectDateWidget
from django.core.exceptions import ValidationError
from datetime import datetime, date

class ScheduleForm(forms.Form):
    def __init__(self, *args, **kwargs):
        offset = kwargs.pop('offset', 0)  # default value of 0 if offset is not provided
        super().__init__(*args, **kwargs)
        date = timezone.localtime() + timezone.timedelta(days=offset)
        self.fields['time_slots'].queryset = Schedule.objects.filter(date=date, status='available')

    time_slots = forms.ModelMultipleChoiceField(
        queryset=Schedule.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        label="Select time slot(s)"
    )

class ScheduleRequestForm(ScheduleForm):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()

    class Meta:
        model = Schedule
        fields = ['time_slot']

