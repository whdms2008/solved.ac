from sys import stdin

N, K = map(int, stdin.readline().split(" "))

coin = [int(stdin.readline()) for _ in range(N)]
coin.reverse()
cnt = 0
for i in coin:
    if K % i != K:
        cnt += K // i
        K -= i * (K // i)
print(cnt)