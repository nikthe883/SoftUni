
capacity = 255
total_filled = 0
pour = 0
n = int(input())

for _ in range(n):
    pour = int(input())
    capacity -= pour
    if capacity < 0:
        print("Insufficient capacity!")
        capacity += pour

print(255 - capacity)


