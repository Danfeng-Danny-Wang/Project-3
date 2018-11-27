from django.db import models


class Schedule(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	focus = models.CharField(max_length=20)
	number_of_weeks = models.PositiveIntegerField(null=True, blank=True)
