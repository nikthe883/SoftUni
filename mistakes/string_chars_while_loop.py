word = ""
char_c = 0
char_o = 0
char_n = 0
chars = ["c", "o", "n"]  # this is better to be a list not a dictionary chars = {"c", "o", "n"}
# last_char = False - we don't need this

while True:
    char = input()
    if char == "End":
        break

    if char.isalpha():
        if char not in chars:
            word += char

        if char == "c":
            if char_c > 0:
                word += char
            else:
                char_c += 1
        elif char == "o":
            if char_o > 0:
                word += char
            else:
                char_o += 1
        elif char == "n":
            if char_n > 0:
                word += char
            else:
                char_n += 1

    if char_n > 0 and char_o > 0 and char_c > 0:
        print(f"{word} ", end="")  # add here the print
        word = ""
        char_n = 0
        char_o = 0
        char_c = 0

# we don't need this

# while last_char != True:
#     if word[-1] != " ":
#         word = word[0:-1]
#     else:
#         last_char = True
#
# print(word)