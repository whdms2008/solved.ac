import sys

cnt = int(sys.stdin.readline())
val = 0
x = list(map(int, sys.stdin.readline().split()))
check = int(sys.stdin.readline())
for i in x:
    if i == check:
        val += 1
print(val)
