from random import randint

# User can choose to focus on Strength, Hypertrophy or Power
# Want to add in more parameters and maybe lifting numbers
def createWorkout(userFocus, numWeeks):

	chestFocusedAux = ['Flat Dumbell', 'Incline Dumbell Bench', 'Chest Flys', 
					   'Push-ups (to failure)', 'Incline Barbell Bench', 'Decline Dumbell Bench',
					   'Plate Raises', 'Bodyweight Dips'
				]
	backFocusedAux = ['Pull-ups', 'Single Arm Dumbell Row', 'T-bar Row', 
					  'Lat Pulldown', 'Cable Row', 'Reverse Hyperextension', 
					  'Hamcurl Machine', 'Eccentric Hamstring Extensions'
				]
	legFocusedAux = ['Lunges', 'Deficite Lunges', 'Jumpsquats', 
					 'Calf Raises', 'Lateral Bandwalks', 'Goblet Squat', 
					 'Hamstring Curls', 'Quad Extensions'
				]

	cardioExercises = ['20 minute jog', '30 minutes rowing machine', '30 minute biking']
	abExercises = ['In-and-Out Abs', '20 crunches', 'Romanian Twists', 'Kettlebell Shrugs']

	mainReps = {'Strength':'3 sets of 1-3 reps','Hypertrophy':'3 sets of 8-12 reps','Power':'3 sets of 3-5 reps'} 
	auxReps = {'Strength':'3 sets of 5-8 reps','Hypertrophy':'3 sets of 8-12 reps'}

	workOut = {}
	for week in range(numWeeks):
		weeklyWorkout = {}

		if(userFocus == 'Power'):
			
			for x in range(1,4):
				dailyWorkout = []
				dailyWorkout.append(mainReps[userFocus] + ' of Bench Press')
				dailyWorkout.append(mainReps[userFocus] + ' of Deadlifts')
				dailyWorkout.append(mainReps[userFocus] + ' of Squats')
				dailyWorkout.append(cardioExercises[randint(0,2)])
				dailyWorkout.append(abExercises[randint(0,3)])
				weeklyWorkout[x] = dailyWorkout
			
		else:

			# Need to make sure auxillary lifts don't repeat
			dailyWorkoutOne = []
			dailyWorkoutOne.append(mainReps[userFocus] + ' of Bench Press')
			for x in range(randint(3,4)):
				dailyWorkoutOne.append(auxReps[userFocus] + ' of ' + chestFocusedAux[randint(0,7)])
			dailyWorkoutOne.append(cardioExercises[randint(0,2)])
			dailyWorkoutOne.append(abExercises[randint(0,3)])

			dailyWorkoutTwo = []
			dailyWorkoutTwo.append(mainReps[userFocus] + ' of Deadlifts')
			for x in range(randint(3,4)):
				dailyWorkoutTwo.append(auxReps[userFocus] + ' of ' + backFocusedAux[randint(0,7)])
			dailyWorkoutTwo.append(cardioExercises[randint(0,2)])
			dailyWorkoutTwo.append(abExercises[randint(0,3)])


			dailyWorkoutThree = []		
			dailyWorkoutThree.append(mainReps[userFocus] + ' of Squats')
			for x in range(randint(3,4)):
				dailyWorkoutThree.append(auxReps[userFocus] + ' of ' + legFocusedAux[randint(0,7)])
			dailyWorkoutThree.append(cardioExercises[randint(0,2)])
			dailyWorkoutThree.append(abExercises[randint(0,3)])

			weeklyWorkout[1] = dailyWorkoutOne
			weeklyWorkout[2] = dailyWorkoutTwo
			weeklyWorkout[3] = dailyWorkoutThree

		workOut[week] = weeklyWorkout

	print(userFocus, 'Workout')
	for x in workOut:
		print('Week:',x)
		for y in workOut[x]:
			print('Day:', y)
			for z in workOut[x][y]:
				print(z)
			print()
		print()

	return workOut

if __name__ == '__main__':
	createWorkout('Power', 9)