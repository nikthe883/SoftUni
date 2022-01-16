
# inputs

city = input()
sales = float(input())

# variables

# commissions Sofia

commission_sofia_to_500 = 5
commission_sofia_from_500_to_1000 = 7
commission_sofia_from_1000_to_10_000 = 8
commission_sofia_above_10_000 = 12

# commissions Varna

commission_varna_to_500 = 4.5
commission_varna_from_500_to_1000 = 7.5
commission_varna_from_1000_to_10_000 = 10
commission_varna_above_10_000 = 13

# commissions Plovdiv

commission_plovdiv_to_500 = 5.5
commission_plovdiv_from_500_to_1000 = 8
commission_plovdiv_from_1000_to_10_000 = 12
commission_plovdiv_above_10_000 = 14.5

# decisions

if city == "Sofia":
    if 0 <= sales <= 500:
        pay = (sales * commission_sofia_to_500) / 100
        print(f"{pay:.2f}")

    elif 500 < sales <= 1000:
        pay = (sales * commission_sofia_from_500_to_1000) / 100
        print(f"{pay:.2f}")

    elif 1000 < sales <= 10_000:
        pay = (sales * commission_sofia_from_1000_to_10_000) / 100
        print(f"{pay:.2f}")

    elif sales > 10_000:
        pay = (sales * commission_sofia_above_10_000) / 100
        print(f"{pay:.2f}")

    else:
        print("error")

elif city == "Varna":
    if 0 <= sales <= 500:
        pay = (sales * commission_varna_to_500) / 100
        print(f"{pay:.2f}")

    elif 500 < sales <= 1000:
        pay = (sales * commission_varna_from_500_to_1000) / 100
        print(f"{pay:.2f}")

    elif 1000 < sales <= 10_000:
        pay = (sales * commission_varna_from_1000_to_10_000) / 100
        print(f"{pay:.2f}")

    elif sales > 10_000:
        pay = (sales * commission_varna_above_10_000) / 100
        print(f"{pay:.2f}")

    else:
        print("error")

elif city == "Plovdiv":
    if 0 <= sales <= 500:
        pay = (sales * commission_plovdiv_to_500) / 100
        print(f"{pay:.2f}")

    elif 500 < sales <= 1000:
        pay = (sales * commission_plovdiv_from_500_to_1000) / 100
        print(f"{pay:.2f}")

    elif 1000 < sales <= 10_000:
        pay = (sales * commission_plovdiv_from_1000_to_10_000) / 100
        print(f"{pay:.2f}")

    elif sales > 10_000:
        pay = (sales * commission_plovdiv_above_10_000) / 100
        print(f"{pay:.2f}")

    else:
        print("error")

else:
    print("error")
