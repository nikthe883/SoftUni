
# inputs

length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100


# calculations

volume = height * width * length

# output

print((volume / 1000) * (1 - percent))