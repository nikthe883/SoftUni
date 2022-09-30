numbers_list = []
for i in range(3):
    numbers_list.append(int(input()))


def find_smallest_number(numbers_list):
    return min(numbers_list)


print(find_smallest_number(numbers_list))
