targets = [int(x) for x in input().split(" ")]
action = input()
targets_shot = 0
while action != "End":

    if 0 <= int(action) <= len(targets) - 1:
        target = targets[int(action)]
        targets[int(action)] = -1
        targets_shot += 1
        for i in range(len(targets)):
            if targets[i] != -1:
                if targets[i] > target:
                    targets[i] = targets[i] - target
                else:
                    targets[i] = targets[i] + target
    action = input()

print(f"Shot targets: {targets_shot} -> {' '.join(str(x) for x in targets)}")


