
# check speed from user input


# inputs

speed = float(input())

# vars

slow = 10
average = 50
fast = 150
ultra_fast = 1000

# decisions

if speed <= slow:
    print('slow')
elif slow < speed <= average:
    print('average')
elif average < speed <= fast:
    print('fast')
elif fast < speed <= ultra_fast:
    print('ultra fast')
else:
    print('extremely fast')