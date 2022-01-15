# inputs

exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

# calculations

# to minutes

exam_time = exam_hour * 60 + exam_minute
arrival_time = arrival_hour * 60 + arrival_minute

time_diff = abs(exam_time - arrival_time)



if arrival_time > exam_time:
    print("Late")
    if time_diff < 60:
        print(f"{time_diff} minutes after the start")
    else:
        hours = time_diff // 60
        minutes = time_diff % 60
        print(f"{hours}:{minutes:02d} hours after the start")

elif arrival_time <= exam_time:
    if time_diff >= 60:
        hours = time_diff // 60
        minutes = time_diff % 60
        print("Early")
        print(f"{hours}:{minutes:02d} hours before the start")
    elif 30 < time_diff < 60:
        print("Early")
        print(f"{time_diff} minutes before the start")
    elif time_diff <= 30:
        print("On time")
        print(f"{time_diff} minutes before the start")
    else:
        print("On time")

