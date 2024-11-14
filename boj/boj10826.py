import sys

N = int(sys.stdin.readline())

if N == 0 or N == 1:
    print(N)
else:
    def fibonacci():
        memo = [0, 1]

        for i in range(2, N + 1):
            previous = memo[1]
            memo[1] = memo[0] + memo[1]
            memo[0] = previous
        return memo[1]

    print(fibonacci())