from django.urls import path

from .views import HomePageView, CreateScheduleView, ScheduleDetailView, create_schedule


urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('create/', CreateScheduleView.as_view(), name='create'),
	path('schedule/<int:pk>/', ScheduleDetailView.as_view(), name='schedule'),
	path('schedule/create/', create_schedule, name='create_schedule'),
]