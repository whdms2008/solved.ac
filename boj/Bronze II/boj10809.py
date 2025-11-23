import sys

a = sys.stdin.readline()
check = [chr(i) for i in range(ord('a'), ord('z') + 1)]
for i in check:
    print(a.find(i), end=" ")
