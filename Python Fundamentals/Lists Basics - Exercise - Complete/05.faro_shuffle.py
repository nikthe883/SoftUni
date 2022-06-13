string_input = input()
faro_number = int(input())

string_list = [x for x in string_input.split(" ")]


for i in range(faro_number):
    string_list1 = string_list[:len(string_list) // 2]
    string_list2 = string_list[len(string_list) // 2:]
    string_list = [c for pair in zip(string_list1, string_list2) for c in pair]

print(string_list)
