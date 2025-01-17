while True:
    string = input().lower()
    if string == "#":
        break
    print(sum([string.count(word) for word in ['a', 'e', 'i', 'o', 'u']]))
