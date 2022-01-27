
# inputs

degrees = float(input())

# main

if 35.00 >= degrees >= 26.00:
    print("Hot")
elif 25.9 >= degrees >= 20.1:
    print("Warm")
elif 20 >= degrees >= 15:
    print("Mild")
elif 14.9 >= degrees >= 12:
    print("Cool")
elif 11.9 >= degrees >= 5:
    print("Cold")
else:
    print("unknown")
