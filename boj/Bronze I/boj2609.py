import sys

a, b = map(int, sys.stdin.readline().split(" "))
for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break
for j in range(max(a, b), a * b + 1):
    if j % a == 0 and j % b == 0:
        print(j)
        break
