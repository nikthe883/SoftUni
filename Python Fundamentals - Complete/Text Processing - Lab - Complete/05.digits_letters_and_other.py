text = input()
digits = ""
letters = ""
other = ""


for i in text:
    if i.isdigit():
        digits += i
    elif i.isalpha():
        letters += i
    else:
        other += i

print(f"{digits}\n"
      f"{letters}\n"
      f"{other}")
