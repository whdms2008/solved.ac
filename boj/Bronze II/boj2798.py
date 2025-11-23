import sys

n, m = list(map(int, sys.stdin.readline().split()))
a = list(map(int, sys.stdin.readline().split()))
result = []
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            b = m-(a[i]+a[j]+a[k])
            if b >= 0:
                result.append(b)
print(m-min(result))

