
# Detects whether or not you have time in your launch break to watch a series

# imports

import math

# inputs

series_name = input()
episode_time = int(input())
launch_time = int(input())

# variables

eat_time = 0.125
relax_time = 0.25


# calculations

eat_time_curr_break = launch_time * eat_time
relax_time_curr_break = launch_time * relax_time

watch_time = launch_time - (eat_time_curr_break + relax_time_curr_break)


# decisions


if watch_time >= episode_time:
    left_time = watch_time - episode_time
    print(f"You have enough time to watch {series_name} and left with {math.ceil(left_time)} minutes free time.")

else:
    need_time = episode_time - watch_time
    print(f"You don't have enough time to watch {series_name}, you need {math.ceil(need_time)} more minutes.")

# testing

#print(eat_time_curr_break,relax_time_curr_break,launch_time,watch_time)