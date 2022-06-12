first_character = ord(input())
second_character = ord(input())


def all_in_between(first, second):
    all_characters = ""
    for character in range(first + 1, second):
        all_characters += f'{chr(character)} '

    return all_characters


print(all_in_between(first_character, second_character))
