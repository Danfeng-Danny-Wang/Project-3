from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Schedule, Day, Week
from .createWorkout import createWorkout
from .forms import CreateScheduleForm


class HomePageView(ListView):
	template_name = 'home.html'
	model = Schedule


class CreateScheduleView(TemplateView):
	template_name = 'create_schedule.html'


class ScheduleDetailView(DetailView):
	model = Schedule
	template_name = 'schedule.html'


def create_schedule(request):

	if request.method == 'POST':
		form = CreateScheduleForm(request.POST)
		if form.is_valid():
			workout_schedule = createWorkout(form.focus, form.number_of_weeks)
			schedule_instance = Schedule()
			schedule_instance.title = form.title
			schedule_instance.focus = form.focus
			schedule_instance.number_of_weeks = form.number_of_weeks
			schedule_instance.save()
			create_weeks(workout_schedule, form.number_of_weeks, form.title)


	return render(request, 'home.html')

def create_weeks(schedule, number_of_weeks, schedule_title):

	for i in range(number_of_weeks):
		activities = schedule[i]
		day_1 = activities[1]
		day_2 = activities[2]
		day_3 = activities[3]

		week_instance = Week()
		week_instance.week_number = i
		# Need change
		week_instance.schedule = Schedule(title=schedule_title)
		week_instance.save()

		create_days(day_1, title, i)
		create_days(day_2, title, i)
		create_days(day_3, title, i)

def create_days(day, schedule_title, week_number):
	
	day_instance = Day()
	day_instance.activity_1 = day[0]
	day_instance.activity_2 = day[1]
	day_instance.activity_3 = day[2]
	day_instance.activity_4 = day[3]
	day_instance.activity_5 = day[4]
	day_instance.activity_6 = day[5]
	# Need change
	day_instance.week = Week(schedule=Schedule(title=schedule_title), week_number=week_number)
	day_instance.save()
		