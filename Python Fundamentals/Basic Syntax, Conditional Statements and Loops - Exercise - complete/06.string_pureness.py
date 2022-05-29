
n = int(input())
pure_check_list = [",", ".", "_"]

for i in range(n):
    string_input = input()
    pureness = [x for x in string_input if x in pure_check_list]
    if len(pureness) == 0:
        print(f"{string_input} is pure.")
    else:
        print(f"{string_input} is not pure!")
