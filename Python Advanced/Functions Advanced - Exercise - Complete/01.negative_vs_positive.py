numbers = [int(x) for x in input().split()]

positive = []
negative = []

for i in numbers:
    if i > 0:
        positive.append(i)
    else:
        negative.append(i)

print(sum(negative))
print(sum(positive))
if abs(sum(negative)) > sum(positive):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")

