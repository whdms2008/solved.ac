import sys

n, k = map(int, sys.stdin.readline().strip().split(" "))
a = [i for i in range(1, n + 1)]
result = []
cnt = 0
for i in range(n):
    for j in range(k-1):
        if cnt > len(a)-1:
            cnt = 0
        cnt += 1
    if cnt > len(a)-1:
        cnt = 0
    result.append(a[cnt])
    del a[cnt]
print(f"<{str(result)[1:-1]}>")
