user_input = input().split(", ")

the_list = []


for i in user_input:
    if 3 <= len(i) <= 16:
        if i.isalnum() or "_" in i or "-" in i:
            if " " not in i:
                the_list.append(i)

for i in the_list:
    print(i)
