from django.urls import path

from .views import HomePageView, CreateScheduleView


urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('create/', CreateScheduleView.as_view(), name='create'),
]