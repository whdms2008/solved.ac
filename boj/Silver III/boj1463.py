# X가 3으로 나누어 떨어지면 3으로 나눔
# X가 2로 나누어 떨어지면, 2로 나눔
# 1을 뺀다

# 정.수 N이 주어졌을때 적절히 사용하여 1로 만든다
# 연산을 사용하는 횟수의 최솟값을 출력
import sys

input = sys.stdin.readline

N = int(input())

d = [0] * (N + 1)

for i in range(2, N + 1):
    d[i] = d[i-1] + 1
    if i % 3 == 0:
        d[i] = min([d[i],d[i//3] + 1])
    if i % 2 == 0:
        d[i] = min([d[i],d[i//2] + 1])
print(d[N])