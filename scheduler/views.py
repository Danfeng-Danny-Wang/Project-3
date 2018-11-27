from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Schedule


class HomePageView(ListView):
	template_name = 'home.html'
	model = Schedule


class CreateScheduleView(TemplateView):
	template_name = 'create_schedule.html'


class ScheduleDetailView(DetailView):
	model = Schedule
	template_name = 'schedule.html'