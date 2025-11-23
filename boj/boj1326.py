"""
[ 문제 ]
개구리가 일렬로 놓여 있는 징검 다리 사이를 폴짝폴짝 뛰어다니고 있다.
징검 다리에는 숫자가 각각 쓰여 있는데
이 개구리는 매우 특이한 개구리여서
어떤 징검다리에서 점프를 할 때 그 징검다리에 쓰여 있는 수의 배수만큼 떨어져 있는 곳으로만 갈 수 있다.

이 개구리는 a번째 징검다리에서 b번째 징검다리까지 가려고 한다.
이 개구리가 a번째 징검다링서 시작하여 최소 몇 번 점ㅍ를 하여 b 번째 징검다리까지 갈 수 있는지를 알아보는 프로그램을 작성하ㅣㅅ오.

[ 입력 ]
첫째 줄에는 징검다리의 개수 N(1<=N<=10,000)이 주어지고, 이어서 각 징검다리에 쓰여 있는 N개의 정수가 주어진다.
그 다음줄에는 N보다 작거나 같은 자연수 a, b가 주어지는 데, 이는 개구리가 a번 징검다리에서 시작하여 b번 징검다리에 가고 싶다는 뜻이다.
징검다리에 쓰여있는 정수는 10,000보다 작거나 같은 자연수이다.


[ 출력 ]
첫째 줄에 개구리가 a번 징검다리에서 b번 징검다리로 최소 몇 번 점프하여 갈 수 있는 지를 출력하시오.
a에서 b로 갈 수 없는 경우네는 -1을 출력한다.
"""

import sys
from collections import deque


def bfs(graph, start_node, end_node):
    q = deque([start_node-1])

    # graph 처음부터 순회 해서, idx를 현재 값 기준으로 점프 시키고, idx가 최대또는 end_node를 초과하면 종료
    # 하고 도착 했으면 step을 반환, 없으면 -1
    step = 0
    while q:
        curr = q.popleft()
        if start_node < end_node:
            remain_dist = (end_node - curr)
            curr_val = remain_dist // graph[curr]
            if curr_val == remain_dist:
                return step
            else:
                q.append(graph[curr] * curr_val)
            print(step, curr, remain_dist, curr_val, q)
        elif start_node > end_node:
            remain_dist = (end_node - curr)
            curr_val = remain_dist // graph[curr]
            if curr_val == remain_dist:
                return step
        else:
            return 0
        step += 1


input = sys.stdin.readline

N = int(input())
bridge = list(map(int, input().split(" ")))
a, b = map(int, input().split(" "))

print(bfs(bridge, a, b))
