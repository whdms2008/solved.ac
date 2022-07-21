import sys

n, k = map(int, sys.stdin.readline().strip().split(" "))
a = [i for i in range(1, n+1)]
result = []
cnt = a[a.index(k)]
for i in range(n):
    check = len(a[cnt:]) + k
    if cnt > len(a):
        cnt = len(a)-check
    if len(a) < k:
        cnt = len(a)
    print(a, cnt-1, check)
    result.append(a[cnt-1])
    a.pop(cnt-1)
    cnt += k-1
print(f"<{str(result)[1:-1]}>")