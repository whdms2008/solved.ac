from sys import stdin

input = stdin.readline
N = int(input())

a = []
for i in range(N):
    b = int(input())
    if b == 0:
        del a[-1]
    else:
        a.append(b)
print(sum(a))