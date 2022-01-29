
# inputs

deposit_money = float(input())
deposit_time = int(input())
annual_interest_rate = float(input())

# calculations

annual_interest_rate_percentage = annual_interest_rate / 100

total_money = deposit_money + deposit_time *((deposit_money * annual_interest_rate_percentage) / 12)

# output

print(total_money)
