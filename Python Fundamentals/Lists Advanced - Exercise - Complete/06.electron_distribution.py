electrons = int(input())

shells = []
loops = 1
while electrons > 0:
    electrons_in_shell = 2 * loops * loops
    if electrons_in_shell > electrons:
        electrons_in_shell = electrons
    electrons -= electrons_in_shell
    shells.append(electrons_in_shell)
    loops += 1
print(shells)
