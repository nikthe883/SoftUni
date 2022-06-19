population = [int(x) for x in input().split(", ")]

wealth = int(input())

equal = True

for i in range(len(population)):
    if population[i] < wealth:
        wealthiest_person = population.index(max(population))

        population[wealthiest_person] -= wealth - population[i]
        population[i] += wealth - population[i]


for i in population:
    if i < wealth:
        equal = False

if not equal:
    print("No equal distribution possible")
else:
    print(population)
