"""
[ 문제 ]
N+1개의 I와 N개의 O로 이루어져 있으면, I와 O 이 교대로 나오는 문자열을
P_N 이라고 한다.
- P_1 IOI
- P_2 IOIOI
- P_3 IOIOIOI
- P_N IOIO...OI ( O 가 N개 )
I와 O 로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 P_N이 몇 군데 포함되어
있는지 구하는 프로그램을 작성
"""

"""
[ 입력 ]
첫째 줄에 N이 주어진다.
둘째 줄에는 S의 길이 M이 주어진다
셋째 줄에 S가 주어진다.
"""

"""
[출력]
S에 P_N이 몇 군데 포함되어 있는지 출력한다.
1 <= N <= 1,000,000
2N+1 <= M <= 1,000,000
S는 I와 O로만 이루어져 있다.
"""
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()

answer = 0
pattern_cnt = 0
i = 0

while i < M - 1:
    if S[i:i + 3] == 'IOI':
        pattern_cnt += 1
        if pattern_cnt == N:
            answer += 1
            pattern_cnt -= 1
        i += 2
    else:
        pattern_cnt = 0
        i += 1
print(answer)
