
# inputs

hour = int(input())
minute = int(input())

# calculations

min_later = minute + 15

total_mins = hour * 60 + min_later
time_hour = total_mins // 60
time_minute = total_mins % 60

if time_hour > 23:
    time_hour = 0


time_minute = time_minute if time_minute > 10 else str(time_minute).zfill(2)

# output

print(f'{time_hour}:{time_minute}')
