int_list = [int(num) for num in input().split(" ")]
remove_numbers = int(input())

for i in range(remove_numbers):
    int_list.remove(min(int_list))

print(', '.join(str(e) for e in int_list))



