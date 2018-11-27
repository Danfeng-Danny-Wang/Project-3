from django.urls import path

from .views import HomePageView, CreateScheduleView, ScheduleDetailView


urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('create/', CreateScheduleView.as_view(), name='create'),
	path('schedule/<int:pk>/', ScheduleDetailView.as_view(), name='schedule'),
]