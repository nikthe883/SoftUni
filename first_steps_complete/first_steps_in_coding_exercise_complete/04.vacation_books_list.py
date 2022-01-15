
# inputs

book_pages = int(input())
pages_per_hour = int(input())
deadline = int(input())

# calculations

time_for_reading_book = book_pages / pages_per_hour
hours_per_day = time_for_reading_book / deadline

# output

print(round(hours_per_day))