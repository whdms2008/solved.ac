import sys

T = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split(" ")))
data = [a[i] for i in range(T)]
result = 0
for i in range(T):
    cnt = 0
    for j in range(1, data[i]+1):
        if data[i]%j == 0:
            cnt += 1
    if cnt == 2:
        result += 1
print(result)