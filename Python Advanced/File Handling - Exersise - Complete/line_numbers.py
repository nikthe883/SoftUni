from string import punctuation

with open("files/text.txt", "r") as even_lines_file:
    text = even_lines_file.readlines()

line = 0
for i in text:
    line += 1
    chars_numbers = 0
    punc_numbers = 0

    for char in i:
        if char.isalpha():
            chars_numbers += 1
        if char in punctuation:
            punc_numbers += 1

    with open("files/output.txt", "a") as output_file:
        output_file.write(f"Line {line}: {i.strip()} ({chars_numbers})({punc_numbers})\n")
