import sys

n = int(sys.stdin.readline())
i, j, c = 2, 5, 2
if n == 1:
    print(n)
    exit()
while not i <= n <= i + j:
    i += j + 1
    j += 6
    c += 1
print(c)
