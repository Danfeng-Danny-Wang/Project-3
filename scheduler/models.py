from django.db import models
from .createWorkout import createWorkout


class Schedule(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	focus = models.CharField(max_length=20)
	number_of_weeks = models.PositiveIntegerField(null=True, blank=True)

	@property
	def week_ono_day_one_activity_one(self):
		schedule = createWorkout(self.focus, self.number_of_weeks)
		return schedule[0][1][0]


class Week(models.Model):
	schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
	week_number = models.PositiveIntegerField(null=True, blank=True)


class Day(models.Model):
	week = models.ForeignKey(Week, on_delete=models.CASCADE)
	activity_1 = models.TextField(max_length=200)
	activity_2 = models.TextField(max_length=200)
	activity_3 = models.TextField(max_length=200)
	activity_4 = models.TextField(max_length=200)
	activity_5 = models.TextField(max_length=200)
	activity_6 = models.TextField(max_length=200)

