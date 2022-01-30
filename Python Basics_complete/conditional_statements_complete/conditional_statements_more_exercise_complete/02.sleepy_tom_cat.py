
# inputs

off_days = int(input())

# variables

off_days_play_minutes = 127
work_days_play_minutes = 63
days_in_year = 365
tom_preferred_play_time = 30_000

# calculation

work_days = days_in_year - off_days
work_days_play_time = work_days * work_days_play_minutes
off_days_play_time = off_days * off_days_play_minutes
yearly_play_time = work_days_play_time + off_days_play_time

# decision

if yearly_play_time >= tom_preferred_play_time:
    over_limit_play_time_hours = (yearly_play_time - tom_preferred_play_time) // 60
    over_limit_play_time_minutes = (yearly_play_time - tom_preferred_play_time) % 60

    print(f"Tom will run away\n"
          f"{over_limit_play_time_hours} hours and {over_limit_play_time_minutes} minutes more for play")

else:
    under_limit_play_time_hours = (tom_preferred_play_time - yearly_play_time) // 60
    under_limit_play_time_minutes = (tom_preferred_play_time - yearly_play_time) % 60

    print(f"Tom sleeps well\n"
          f"{under_limit_play_time_hours} hours and {under_limit_play_time_minutes} minutes less for play")
