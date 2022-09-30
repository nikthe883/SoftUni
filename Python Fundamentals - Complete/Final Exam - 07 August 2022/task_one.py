message = input()

commands = input().split(" ")

while commands[0] != "Finish":

    if commands[0] == "Replace":
        message = message.replace(commands[1], commands[2])
        print(message)
    elif commands[0] == "Cut":
        if 0 <= int(commands[1]) <= len(message) and 0 <= int(commands[2]) <= len(message):
            message = message[:int(commands[1])] + message[int(commands[2])+1:]
            print(message)
        else:
            print("Invalid indices!")
    elif commands[0] == "Make":
        if commands[1] == "Upper":
            message = message.upper()
        elif commands[1] == "Lower":
            message = message.lower()
        print(message)
    elif commands[0] == "Check":
        if commands[1] in message:
            print(f"Message contains {commands[1]}")
        else:
            print(f"Message doesn't contain {commands[1]}")
    elif commands[0] == "Sum":
        if 0 <= int(commands[1]) <= len(message) and 0 <= int(commands[2]) <= len(message):
            new_message = message[int(commands[1]):int(commands[2])+1]

            ascii_values = 0
            for i in new_message:
                ascii_values += ord(i)

            print(ascii_values)
        else:
            print("Invalid indices!")

    commands = input().split(" ")
