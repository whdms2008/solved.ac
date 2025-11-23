from sys import stdin

input = stdin.readline

N, M = map(int, input().split(" "))

a = set([input().strip() for _ in range(N)])
b = set([input().strip() for _ in range(M)])

result = sorted(list(a & b))
print(len(result))

for i in result:
    print(i)
