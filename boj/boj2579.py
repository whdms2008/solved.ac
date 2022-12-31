# 계단 오르기 - 동적 계획법 ( DP : Dynamic Programming )
import sys


n = int(sys.stdin.readline())
s = [int(sys.stdin.readline()) for _ in range(n)]
if len(s) <= 2:
    print(sum(s))
else:
    dp = [0] * n
    dp[0] = s[0]
    dp[1] = max(s[0] + s[1], s[1])
    dp[2] = max(s[0] + s[2], s[1] + s[2])
    for i in range(3, n):
        dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
    print(dp[-1])
