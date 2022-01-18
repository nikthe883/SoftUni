
width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())

volume_free_space = width_free_space * length_free_space * height_free_space

volume_taken = 0
done = False
while volume_free_space >= volume_taken:
    num_boxes = input()
    if num_boxes == "Done":
        done = True
        break
    volume_taken += int(num_boxes)


space = abs(volume_taken - volume_free_space)
if not done:
    print(f"No more free space! You need {space} Cubic meters more.")
else:
    print(f"{space} Cubic meters left.")


