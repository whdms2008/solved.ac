while True:
    a = input()
    print(exit() if a == "0" else "yes" if a[::-1] == a else "no")