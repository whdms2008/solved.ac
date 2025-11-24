"""
[ 문제 ]
정육면체 주사위를 사용, 주사위 각 면에는 1~6까지 수가 적혀있다.
크기는 10x10이며, 총 100칸으로 나ㅏ누어져 있다.
보드판에는 1부터 100까지의 수가 하나씩 적혀있다.

주사위를 굴려 나온 수 만큼 이동해ㅑㅇ 하낟.

플레이어가 i번 칸에 있고, 주사위가 4라면, i+4번 칸으로 이동해야 한다.

만약 주ㅏ위를 굴린 결과가 100번 칸을 넘어간다면 이동할 수 없다.

도착한 칸이 사다리면, 사다리를 타고 위로 올라간다.

뱀이 있는 칸에 도착하면, 뱀을 따라서 내려가게 된다.

즉, 사다리를 이용해 이동한 카느이 번호는 원래 있던 칸의 번호보다 크고, 뱀을 이용해 이동한 칸의 번호는 원래 있던
칸의 번호보다 작아진다.

겡미의 목표는 1번 칸에서 100번 칸에 도착하는 것이다.

게임판의 상태가 주어졌을 때, 100번 칸에 도착하기 위해 주사위를 굴려야 하는 횟수의 최솟값을 구해보자.

[ 입력 ]
사다리의 수 N( 1<= N <= 15 ) 뱀의 수 M(1 <=M<15)이 주어진다.
둘째 줄 부터 n개의 줄에는 사다리의 정보를 의미하는 X, Y(X<Y)가 주어진다. x번 칸에 도착하면 y번 칸으로 이동한다는 의미

다음 M개의 줄에는 뱀의 정보를 의미하는 u, v(u >v)가 주어진다. u번째 칸에 도착하면, v번 칸으로 이동한다는 의미이다.

1번 칸과 100번 칸은 뱀과 사다리의 시작 또는 끝이 아니다. 모든 칸은 최대 하나의 사다리 또는 뱀을 가지고 있으며,
동시에 두 가지를 모두 가지고 있는 경우는 없다.

항상 100번 칸에 도착할 수 있는 입력만 주어진다.

[ 출력 ]
100번 칸에 도착하기 위해 주사위를 최소 몇 번 굴려야 하는지를 출력한다.
"""

import sys
from collections import deque


def solve(steals, snakes):
    q = deque([(1, 0)])
    visited = [False] * 100
    visited[0] = True

    while q:
        curr, dice_cnt = q.popleft()

        if curr == 100:
            return dice_cnt

        for num in range(1, 7):
            next_num = curr + num
            if next_num > 100:
                continue
            if visited[next_num - 1]:
                continue

            if next_num in steals[0]:
                next_num = steals[1][next_num]
            if next_num in snakes[0]:
                next_num = snakes[1][next_num]
            visited[next_num - 1] = True
            q.append((next_num, dice_cnt + 1))


input = sys.stdin.readline

N, M = map(int, input().split(" "))

steals, snakes = [set(), dict()], [set(), dict()]

for _ in range(N):
    s, e = map(int, input().split(" "))
    steals[0].add(s)
    steals[1][s] = e

for _ in range(M):
    s, e = map(int, input().split(" "))
    snakes[0].add(s)
    snakes[1][s] = e

print(solve(steals, snakes))
