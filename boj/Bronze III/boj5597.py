import sys

check = list(range(1, 31))
for i in range(28):
    a = int(sys.stdin.readline())
    check.remove(a)
print(check[0])
print(check[1])
