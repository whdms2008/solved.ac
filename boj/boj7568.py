from sys import stdin

N = int(stdin.readline())

data = [list(map(int,stdin.readline().split(" "))) for i in range(N)]

result = []
for i in range(len(data)):
    check = 0
    for j in range(N):
        if i == j:
            continue
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            check += 1
    print(check+1, end=" ")