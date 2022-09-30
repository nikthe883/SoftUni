n = int(input())
sym = {}

for i in range(n):
    word = input()
    synonym = input()
    if word not in sym:
        sym[word] = []
    sym[word].append(synonym)

for word in sym:
    print(f"{word} - {', '.join(sym[word])}")
