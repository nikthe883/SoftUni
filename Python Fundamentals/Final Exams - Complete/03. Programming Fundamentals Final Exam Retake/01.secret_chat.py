message = input()

commands = input().split(":|:")

while commands[0] != "Reveal":
    if commands[0] == "InsertSpace":
        message = message[:int(commands[1])] + " " + message[int(commands[1]):]
        print(message)

    elif commands[0] == "Reverse":
        if commands[1] not in message:
            print("error")
        else:
            reversed_string = commands[1][::-1]
            message = message.replace(commands[1], "", 1)
            message = message + reversed_string
            print(message)

    elif commands[0] == "ChangeAll":
        message = message.replace(commands[1], commands[2])
        print(message)

    commands = input().split(":|:")

print(f"You have a new text message: {message}")
