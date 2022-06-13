word_one = input()
word_two = input()

list1 = list(word_one)
list2 = list(word_two)

for i in range(len(list1)):
    if list1[i] != list2[i]:
        list1[i] = list2[i]
        print(''.join(list1))
