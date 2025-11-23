from sys import stdin

T = int(stdin.readline())

data = [list(map(int, stdin.readline().split(" "))) for i in range(T)]
data = sorted(data, key=lambda x: (x[1], x[0]))
for i in data:
    print(i[0], i[1])
