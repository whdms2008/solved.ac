import sys

a = list(sys.stdin.readline())
for i in range(len(a)):
    if a[i].islower():
        print(a[i].upper(), end="")
    else:
        print(a[i].lower(), end="")
