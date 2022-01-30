people_number = int(input())

fitness = {"Back": 0,
           "Chest": 0,
           "Legs": 0,
           "Abs": 0,
           "Protein shake": 0,
           "Protein bar": 0}

for i in range(people_number):
    why = input()
    if why in fitness:
        fitness[why] += 1

total_training = fitness['Back'] + fitness['Chest'] + fitness['Legs'] + fitness['Abs']
total_supp = fitness['Protein shake'] + fitness['Protein bar']

print(f"{fitness['Back']} - back\n"
      f"{fitness['Chest']} - chest\n"
      f"{fitness['Legs']} - legs\n"
      f"{fitness['Abs']} - abs\n"
      f"{fitness['Protein shake']} - protein shake\n"
      f"{fitness['Protein bar']} - protein bar\n"
      f"{total_training / people_number * 100 :.2f}% - work out\n"
      f"{total_supp / people_number * 100 :.2f}% - protein\n"
      )
