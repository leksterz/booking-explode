from django.urls import path
from .views import ScheduleListView, ScheduleRequestView

app_name = 'frontend'

urlpatterns = [
    path('request/<int:offset>/', ScheduleRequestView.as_view(), name='request'),
    path('<int:offset>/', ScheduleListView.as_view(), name='schedule'),
    path('', ScheduleListView.as_view(), {'offset': 0}, name='schedule_today'), # added default offset value of 0
]

# urlpatterns = [
#     # ex: /frontend
#     path('', views.schedule, name='schedule'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]