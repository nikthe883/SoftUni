days = int(input())
doctors = 7
treated = 0
untreated = 0
for i in range(1, days+1):
    patients = int(input())
    if i % 3 == 0:
        if treated < untreated:
            doctors += 1
    if patients > doctors:
        untreated += patients - doctors
        treated += doctors
    else:
        treated += patients

print(f"Treated patients: {treated}.\n"
      f"Untreated patients: {untreated}.")
