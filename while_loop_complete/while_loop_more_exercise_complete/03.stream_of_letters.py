
c_count = 0
o_count = 0
n_count = 0
message = ""

while True:

    letter = input()

    if letter == "End":
        break
    if letter == "c" and c_count == 0:
        c_count += 1
    elif letter == "o" and o_count == 0:
        o_count += 1
    elif letter == "n" and n_count == 0:
        n_count += 1
    else:
        if letter.isalpha():

            message += letter


    if c_count == 1 and o_count == 1 and n_count == 1:
        print(f"{message} ",end = "")
        message = ""
        c_count = 0
        o_count = 0
        n_count = 0