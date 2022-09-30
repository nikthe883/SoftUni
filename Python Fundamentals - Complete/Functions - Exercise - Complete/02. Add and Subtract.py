n1 = int(input())
n2 = int(input())
n3 = int(input())


def sum_numbers(a, b):
    return a + b


def subtract(ab, c):
    return ab - c


def add_and_subtract():
    add = sum_numbers(n1, n2)
    subtracted = subtract(add, n3)
    return subtracted


print(add_and_subtract())
