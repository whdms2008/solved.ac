import sys

r = 31
M = 1234567891
L = int(sys.stdin.readline())
a = sys.stdin.readline()
result = 0
for i in range(0, L):
    result += (ord(a[i])-96)*(r**i)
print(result % M)

