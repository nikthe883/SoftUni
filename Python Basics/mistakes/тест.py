from itertools import combinations

num1 = int(input()) * "1"
num2 = int(input()) * "2"
num3 = int(input()) * "5"
n = int(input())

a = list(num1) + list(num2) + list(num3)  # combines the lists of str to one list
# print(a)
a_int = [int(i) for i in a]  # converts the list of strings to a list of digits
#print(a_int)
b = []

for l in range(0, len(a_int)+1):  # for list in range length of the list a_int
    for i in combinations(a_int, l):  # seek all combinations of the numbers
        if sum(i) == n:
            b.append(i)  # appends to new list

#print(b)
c = list(dict.fromkeys(b))  # gets rid of the duplicates because dictionaries can not have dupes.
#print(sorted(c))
for ne6tosi in reversed(sorted(c)): # sorts the list in order 1,2,3,4 - so on and reverses the for loop
    print(f"{ne6tosi.count(1)} * 1 lv. + {ne6tosi.count(2)} * 2 lv. + {ne6tosi.count(5)} * 5 lv. = {n} lv.")  # STOLEN FROM KRUM

