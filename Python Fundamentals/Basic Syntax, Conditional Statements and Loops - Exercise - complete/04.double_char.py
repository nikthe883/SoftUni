word = input()

while word != "End":
    double_char = ""
    if word != "SoftUni":
        for i in word:
            double_char += i*2
        print(double_char)
    word = input()
