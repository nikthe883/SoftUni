numbers = input().split(" ")

def rounding_numbers(numbers):
    rounded_list = []
    for i in numbers:
        rounded_list.append(round(float(i)))

    return rounded_list

print(rounding_numbers(numbers))
