capacity = float(input())

suitcase_capacity = input()
total_load = 0
count = 0

while suitcase_capacity != "End":


    if count % 3 == 0:
        int_suitcase_capacity = float(suitcase_capacity)
        int_suitcase_capacity *= 1.10

    total_load += float(suitcase_capacity)
    if total_load >= capacity:
        break
    count += 1
    suitcase_capacity = input()



if total_load >= capacity:
    print("No more space!")
else:
    print("Congratulations! All suitcases are loaded!")

print(f"Statistic: {count} suitcases loaded.")