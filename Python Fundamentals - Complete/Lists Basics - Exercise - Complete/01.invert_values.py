user_input = input()

output = []
my_list = [int(el) for el in user_input.split(' ')]
for i in my_list:
    if i < 0:
        output.append(abs(i))
    else:
        output.append(-abs(i))
print(output)