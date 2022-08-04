password = input()

commands = input().split(" ")


while commands[0] != "Done":
    new_password = ""
    if commands[0] == "TakeOdd":
        for i in range(len(password)):
            if i % 2 != 0:
                new_password += password[i]
        password = new_password
        print(password)
    elif commands[0] == "Cut":
        length = int(commands[1]) + int(commands[2])
        password = password[:int(commands[1])] + password[length:]
        print(password)

    elif commands[0] == "Substitute":
        if commands[1] in password:
            password = password.replace(commands[1], commands[2])
            print(password)
        else:
            print("Nothing to replace!")

    commands = input().split(" ")
print(f"Your password is: {password}")
