#
# first_row = int(input())
# second_row = int(input())
#
# odd_numbers = [1,3,5,7,9]
#
# numbers = []
#
# for i in range(first_row,second_row):
#     x = [int(a) for a in str(i)]
#     if(set(x).issubset(set(odd_numbers))):
#         numbers.append(i)
#
#
# listToStr = ' '.join([str(elem) for elem in numbers])
#
# print(listToStr)

start = int(input())
end = int(input())

first_start = int(start / 1000)
second_start = int((start / 100) % 10)
third_start = int((start / 10) % 10)
fourth_start = int(start % 10)

first_end = int(end / 1000)
second_end = int((end / 100) % 10)
third_end = int((end / 10) % 10)
fourth_end = int(end % 10)

for num_1 in range(first_start, first_end + 1):
    for num_2 in range(second_start, second_end + 1):
        for num_3 in range(third_start, third_end + 1):
            for num_4 in range(fourth_start, fourth_end + 1):
                if num_1 % 2 != 0 and num_2 % 2 != 0 and num_3 % 2 != 0 and num_4 % 2 != 0:
                    print(f'{num_1}{num_2}{num_3}{num_4}', end=' ')