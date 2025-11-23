"""
[ 문제 ]
해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다.
이 회사는 N개의 컴퓨터로 이루어져 있다. 김지민은 귀찮기 때문에, 한번의 해킹으로 여러 개의 컴퓨터를 해킹할 수 있는 컴퓨터를
해킹 하려고 하낟.
이 회사의 컴퓨너는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데, A가 B를 신뢰하는 경우에는
B를 해킹하면, A도 해킹ㅎ라 수 있다는 소리다.

이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을
작성하시오.

[ 입력 ]
첫째 줄에, N과 M이 들어온다, N<=10,000, M<=100,000
둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오면 A 가 B를 신뢰한다를 의미한다.
컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있다.

[ 출력 ]
첫째 줄에, 김지민이 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력한다.

"""

from collections import defaultdict
from collections import deque
import sys


def bfs(graph, n):
    hacks = {}
    for start_node in range(1, n + 1):
        q = deque([start_node])
        visited = [False] * (n+1)
        visited[start_node] = True
        hack_cnt = 0
        while q:
            curr = q.popleft()
            for next_node in graph[curr]:
                if not visited[next_node]:
                    q.append(next_node)
                    visited[next_node] = True
                    hack_cnt += 1
        if hack_cnt:
            hacks[start_node] = hack_cnt
    return hacks.items()


input = sys.stdin.readline

N, M = map(int, input().split(" "))

graph = defaultdict(list)

for _ in range(M):
    A, B = map(int, input().split(" "))
    graph[B].append(A)

sort_bfs = sorted(bfs(graph, N))

max_hacks = []
max_cnt = max([value for _, value in sort_bfs])

for id, cnt in sort_bfs:
    if max_cnt == cnt:
        max_hacks.append(id)

print(*sorted(max_hacks))
