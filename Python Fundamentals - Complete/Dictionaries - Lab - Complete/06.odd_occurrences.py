words = input().split(" ")
my_dict = {}

for i in words:
    word_lower = i.lower()
    if word_lower not in my_dict:
        my_dict[word_lower] = 0
    my_dict[word_lower] += 1


for k, v in my_dict.items():
    if v % 2 != 0:
        print(k, end=" ")
