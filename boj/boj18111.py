from sys import stdin
from collections import Counter
N, M, B = map(int, stdin.readline().split(" "))
block = [list(map(int, stdin.readline().split(" "))) for i in range(N)]

avg = 0
for i in range(N):
    avg += sum(block[i])
avg = round(avg/(N*M))
print(avg)
for i in range(N):
    for j in range(M):
        print(f"낮음[{block[i][j]}] {i}*{j}" if avg > block[i][j] else f"높음[{block[i][j]}] {i}*{j}" if avg != block[i][j] else f"같음[{block[i][j]}] {i}*{j}")
