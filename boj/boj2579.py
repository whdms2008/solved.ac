# 계단 오르기 - 동적 계획법 ( DP : Dynamic Programming )
import sys

n = int(sys.stdin.readline())
s = [int(sys.stdin.readline()) for _ in range(n)]
if len(s) <= 2:
    print(sum(s))
else:
    dp = [0] * n
    dp[0] = s[0]  # 1칸 움직일 경우
    dp[1] = max(s[0] + s[1], s[1])  # 2칸 움직일 경우 0, 1 또는 1
    dp[2] = max(s[0] + s[2], s[1] + s[2])  # 3칸 움직일 경우 0, 2, 또는 1, 2
    # 예 ) [ 10, 20, 30, 40, 50, 60 ]
    # dp[0] = 10
    # [ 0 ]
    # dp[1] = max(10 + 20, 20) - 0번을 거치고 1번을 가거나, 0번을 뛰어넘고 1번으로 가는 경우
    # [ 0 -> 1, [0] -> 1 ]
    # dp[2] = max(10 + 30, 20 + 30 ) - 0번에서 한칸 뛰고 2번으로, 2번에서 3번으로
    # [ 0 -> [1] -> 2, [1]-> 2 -> 3 ]

    for i in range(3, n):
        dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
        # dp[3] = 10 + 30 + 40, 20 + 40
        # 0 -> [1] -> 2 -> 3, [0] -> 1 -> [2] -> 3

        # dp[4] = 30 + 30 + 50
    print(dp[-1])
