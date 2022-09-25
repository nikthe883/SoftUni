first_sequence = set(input().split())
second_sequence = set(input().split())

n = int(input())

for _ in range(n):
    commands = input()

    if "Add First" in commands:
        commands = commands.split()
        first_sequence = first_sequence.union(commands[2:])

    elif "Add Second" in commands:
        commands = commands.split()
        second_sequence = second_sequence.union(commands[2:])

    elif "Remove First" in commands:
        commands = commands.split()
        for number in commands[2:]:
            if number in first_sequence:
                first_sequence.remove(number)

    elif "Remove Second" in commands:
        commands = commands.split()
        for number in commands[2:]:
            if number in second_sequence:
                second_sequence.remove(number)

    elif "Check Subset" in commands:

        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print("True")
        else:
            print("False")

print(*sorted(map(int, first_sequence)), sep=", ")
print(*sorted(map(int, second_sequence)), sep=", ")
