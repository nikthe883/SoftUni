n = int(input())

positive = []
negative = []

for _ in range(n):
    user_input = int(input())
    if user_input >= 0:
        positive.append(user_input)
    else:
        negative.append(user_input)

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}\n Sum of negatives: {sum(negative)}")
