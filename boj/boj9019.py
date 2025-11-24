"""
[ 문제 ]
네 개의 명령어 D, S, L, R을 이용하는 간단한 계산기가 있다.
이 계산기에는 레지스터가 하나 있는데, 이 레지스터에는 0 이상, 10,000 미만의 십진수를 저장할 수 있다.
각 명령어는 이 레지스터에 저장된 n을 다음과 같이 변환한다.

n의 네 자릿수를 d_1, d_2, d_3, d_4 라고 하자 ( 즉 n = ((d_x * 10 + d_2) * 10 + d_x3 ) * 10 + d_4 라고 하자)

1. D: D는 n을 두 배로 바꾼다.
결과 값이 9999보다 큰 경우에는 10000으로 나눈 나머지를 취한다. 그 결과 값(2n mod 10000)을 레지스터에 저장한다.

2. S: S는 n에서 1을 뺀 결과 n-1을 레지스터에 저장한다.
n이 0 이라면 9999 가 대신 레지스터에 저장된다.

3. L: L은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다.
이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d_2, d_3, d_4, d_1이 된다.

4. R: R은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다.
이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.

L, R 명령어는 십진 자릿수를 가정하고 연산을 수행
예를 들어 n = 1234 라면 여기에 L을 적용하면2341이 되고 r을 적용하면 4123이 된다.

작성할 프로그램은 주어진 서로 다른 두 정수 A와 B(A != B)에 대하여 A를 B로 바꾸는 최소한의 명령어를 생성하는 프로그램이다.
예를 들어서 A = 1234, B = 3412 라면 다음과 같이 두 개의 명령어를 적용하면 A를 B로 변환할 수 있다.

1234 ->L -> 2341 -> L -> 3412
1234 ->R -> 4123 -> R -> 3412
따라서 프로그램은 LL이나 RR을 출력

n의 자릿수로 0이 포함된 경우에 주의해야 한다.
예를 들어서 1000에 L을 적용하면 0001이 되므로 결과는 1이 된다.

그러나 R을 적용하면 0100이 되므로 결과는 100이 된다.

[ 입력 ]
첫째 줄 T개의 테스트케이스
둘째 줄 각 테스트케이스에 두 개의 정수 A, B가 (A!=B) 공백으로 분리되어 차례로 주어진다.
A는 레지스터의 초기값, B는 최종값
A와 B는 모두 0 이상 10,000 미만이다.

[ 출력 ]
A에서 B로 변환하기 위해 필요한 최소한의 명령어 나열을 출력한다. 가능한 명령어 나열이 여러가지면, 아무거나 출력한다.
"""

import sys
from collections import deque

input = sys.stdin.readline

T = int(input())


def solve(a: int, b: int):
    q = deque([(a, "")])

    visited = [False] * 1_0000

    while q:
        curr, cmds = q.popleft()
        if curr == b:
            return cmds

        for cmd in ["D", "S", "L", "R"]:
            next_num = 0
            if cmd == "D":
                next_num = curr * 2
                if next_num > 9999:
                    next_num %= 10000
            elif cmd == "S":
                if curr == 0:
                    next_num = 9999
                else:
                    next_num = curr - 1
            elif cmd == "L":
                num_1 = curr // 1000
                num_2 = (curr % 1000) * 10
                next_num = num_2 + num_1
            elif cmd == "R":
                num_1 = curr // 10
                num_2 = (curr % 10) * 1000
                next_num = num_2 + num_1
            if visited[next_num]:
                continue

            q.append((next_num, (cmds + cmd)))
            visited[next_num] = True



for _ in range(T):
    A, B = map(int, input().split(" "))
    print(solve(A, B))
