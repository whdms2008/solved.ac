# 피제수(분자) A
# 제수(분모) B가 있다.
# 두 수를 나누었을 때, 소숫점 아래 N번째 자리수를 구하려고 한다.
# 예를 들어, A=3, B=4, N=1 이라면, a/b=0.75 이므로 답은 7이 된다.

# 입력
# A B N
# 1 <= A, B <= 100,000, N(1<= 1,000,000)

# 출력
# A / B 를 했을 때, 소숫점 아래 N번째 수를 출력한다.

import sys
input = sys.stdin.readline

A, B, N = map(int, input().split())

digit = 0
for _ in range(N):
    A = (A % B) * 10
    digit = A // B
    print(digit)

print(digit)
