# imports

from math import floor

# inputs

hours_needed_to_complete_project = int(input())
project_deadline_in_days = int(input())
number_of_workers_for_overtime = int(input())

# variables

time_for_training = 0.1
normal_work_day_hours = 8
maximum_overtime_hours_per_day = 2

# calculations

left_working_days_without_training = project_deadline_in_days - (project_deadline_in_days * time_for_training)
left_working_hours_without_training = left_working_days_without_training * normal_work_day_hours

total_overtime_hours = number_of_workers_for_overtime * maximum_overtime_hours_per_day * project_deadline_in_days
total_work_hours = floor(total_overtime_hours + left_working_hours_without_training)

# decisions

if total_work_hours >= hours_needed_to_complete_project:

    hours_remaining = total_work_hours - hours_needed_to_complete_project
    print(f"Yes!{hours_remaining} hours left.")

else:
    hours_needed = hours_needed_to_complete_project - total_work_hours
    print(f"Not enough time!{hours_needed} hours needed.")
