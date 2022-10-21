from collections import deque

words = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}

vowels = deque(input().split())
consonants = input().split()

found_word = False
while vowels and consonants:
    letter_vowels = vowels.popleft()
    letter_consonants = consonants.pop()
    for word in words.keys():
        words[word] = words[word].replace(letter_vowels, '')
        words[word] = words[word].replace(letter_consonants, '')
        if words[word] == '':
            print(f"Word found: {word}")
            found_word = True
            break
    if found_word:
        break


if not found_word:
    print("Cannot find any word!")


if vowels:
    print(f'Vowels left: {" ".join(vowels)}')
if consonants:
    print(f'Consonants left: {" ".join(consonants)}')
