control_mins = int(input())
control_secs = int(input())
distance = float(input())
speed = int(input())

control_secs += control_mins * 60
slope_slowdown = distance / 120 * 2.5
marin_time = distance / 100 * speed - slope_slowdown

if marin_time <= control_secs:
    print(f"Marin Bangiev won an Olympic quota!\n"
          f"His time is {marin_time:.3f}.")
else:
    needed = marin_time - control_secs
    print(f"No, Marin failed! He was {needed:.3f} second slower.")
