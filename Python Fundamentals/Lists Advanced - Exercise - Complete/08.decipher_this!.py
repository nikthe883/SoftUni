word = input().split(" ")


def acii(word):
    number = ""
    message = []
    for i in range(len(word)):
        for b in word[i]:
            if b.isdigit():
                number += b
                word[i] = word[i].replace(b, "")

        word[i] = chr(int(number)) + word[i]

        some_list = list(word[i])
        some_list[1], some_list[-1] = some_list[-1], some_list[1]
        some_list = "".join(some_list)
        message.append(some_list)
        number = ""
    return " ".join(message)


print(acii(word))
