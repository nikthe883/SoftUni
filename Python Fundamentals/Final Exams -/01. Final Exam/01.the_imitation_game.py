message = input()
user_input = input().split("|")

while user_input[0] != "Decode":

    if user_input[0] == "ChangeAll":
        message_list = list(message)
        for i in range(len(message_list)):
            if message_list[i] == user_input[1]:
                message_list[i] = user_input[2]
        message = "".join(message_list)

    elif user_input[0] == "Insert":
        message = message[:int(user_input[1])] + user_input[2] + message[int(user_input[1]):]

    elif user_input[0] == "Move":
        message = message[int(user_input[1]):] + message[:int(user_input[1])]

    user_input = input().split("|")

print(f"The decrypted message is: {message}")
