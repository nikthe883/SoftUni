
letter_one = input()
letter_two = input()
skip = input()
count = 0

for l1 in range(ord(letter_one), ord(letter_two) + 1):
    for l2 in range(ord(letter_one), ord(letter_two) + 1):
        for l3 in range(ord(letter_one), ord(letter_two) + 1):
            if l1 != ord(skip) and l2 != ord(skip) and l3 != ord(skip):
                count += 1
                print(f"{chr(l1)}{chr(l2)}{chr(l3)}", end=" ")
print(count)
