
initial_height = int(input())

height_to_jump = initial_height - 30
fails = 0
count = 0

while True:
    jump = int(input())
    count += 1

    if jump <= height_to_jump:
        fails += 1
        if fails == 3:
            print(f"Tihomir failed at {height_to_jump}cm after {count} jumps.")
            break
    else:
        if height_to_jump >= initial_height:
            print(f"Tihomir succeeded, he jumped over {initial_height}cm after {count} jumps.")
            break
        height_to_jump += 5
        fails = 0

