
time_action = int(input())
number_scenes = int(input())
time_scene = int(input())

time_action *= 0.85

time_action -= number_scenes * time_scene

if time_action >= 0:
    print(f"You managed to finish the movie on time! You have {time_action:.0f} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {abs(time_action):.0f} minutes.")
