from collections import deque

seq = input().split(", ")
seq1 = input().split(",")
seq2 = input().split(", ")

seq1 = deque(seq1)
seated = []
count = 0
while True:

    if len(seated) == 3:
        break


    num1 = int(seq1.popleft())
    num2 = int(seq2.pop())
    char = chr(num1 + num2)
    count += 1
    found = False

    for i in range(len(seq)):
        if char in seq[i]:
            if str(num1) in seq[i] or str(num2) in seq[i]:
                if seq[i] in seated:
                    continue
                else:
                    seated.append(seq[i])
                    found = True
                    break
    if not found:
        seq1.append(str(num1))
        seq2.insert(0, str(num2))

    if count == 10:
        break

print(f"Seat matches: {', '.join(seated)}")
print(f"Rotations count: {count}")
