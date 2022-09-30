user_input = input()

def absolute_value(user_input):
    value = user_input.split(" ")

    my_list = []
    for v in value:
        my_list.append(abs(float(v)))
    return my_list


smt  = absolute_value(user_input)
print(smt)