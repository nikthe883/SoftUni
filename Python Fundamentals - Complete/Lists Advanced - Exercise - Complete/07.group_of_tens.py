user_input = [int(x) for x in input().split(", ")]

max_value = max(user_input)
boundary = 10
check = lambda x:  x <= boundary

for i in range(1, max_value + 1, 10):
    list_items_to_be_removed = (list(filter(check, user_input)))
    [user_input.remove(x) for x in list_items_to_be_removed]

    print(f"Group of {boundary}'s: {list_items_to_be_removed}")
    boundary += 10
