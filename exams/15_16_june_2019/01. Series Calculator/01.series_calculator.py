
series_name = input()
numbers_seasons = int(input())
number_episodes = int(input())
time_no_ads_per_episode = int(input())

ads = time_no_ads_per_episode * 0.20
total_time_episode = ads + time_no_ads_per_episode
additional_time_per_season = numbers_seasons * 10

total_watch_time = total_time_episode * number_episodes * numbers_seasons + additional_time_per_season

print(f"Total time needed to watch the {series_name} series is {total_watch_time:.0f} minutes.")
