from django import forms


class CreateScheduleForm(forms.Form):
	title = forms.CharField(label='title', max_length=100)
	focus = forms.CharField(label='focus', max_length=100)
	number_of_weeks = forms.CharField(label='number_of_weeks', max_length=100)
