user_input = input().split(", ")
user_input = [x for x in user_input]


def check(user_input):
    for i in user_input:
        print(i == i[::-1])


check(user_input)
