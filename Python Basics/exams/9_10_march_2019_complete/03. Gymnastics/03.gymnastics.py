
country = input()
device = input()

points = 0

if country == "Bulgaria":
    if device == "ribbon":
        points = 9.600 + 9.400
    elif device == "hoop":
        points = 9.550 + 9.750
    elif device == "rope":
        points = 9.500 + 9.400
elif country == "Russia":
    if device == "ribbon":
        points = 9.100 + 9.400
    elif device == "hoop":
        points = 9.300 + 9.800
    elif device == "rope":
        points = 9.600 + 9.000
else:
    if device == "ribbon":
        points = 9.200 + 9.500
    elif device == "hoop":
        points = 9.450 + 9.350
    elif device == "rope":
        points = 9.700 + 9.150

remaining_points = 20 - points
percent_remaining = remaining_points / 20 * 100

print(f"The team of {country} get {points:.3f} on {device}.\n"
      f"{percent_remaining:.2f}%")
