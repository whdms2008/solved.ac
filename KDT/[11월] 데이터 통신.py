# 구름 통신 망은 N 개의 통신탑, M 개의 통신 케이블로 구성되어있음
# 그래프 같다

# 각 통신탑은 1 ~ N 번까지 번호가 있음

# 통신 케이블로 연결 되어 있는 통신탑끼리는 서로 데이터를 주고 받을 수 있다.
# 연결 되지 않은 통신탑 끼리는 데이터를 주고 받을 수 없다

# 각 통신 케이블은 서로 다른 두 통신탑을 양방향으로 연결하고 있다
# 각 통신 케이블에는 주고 받을 수 있는 데이터 크기의 상한 k_i, 가 존재한다.
# 만약 전송하려는 데이터의 현재 크기가 k_i 보다 크다면, 그 통신 케이블로는 데이터를 전송할 수 없다.

# 구름이는 S번 통신탑에서 E번 통신탑으로 크기가 1인 데이터를 전송하려고 한다.
# 데이터는 통신 케이블을 통해 한번 이동할 대마다 이동 기록이 쌓여 크기가 1 증가

# 구름이는 데이터가 E번 통신탑에 도달했을 때 데이터의 크기가 최소가 되기를 원한다
# 구름이는 가능한 가장 효율적인 경로를 찾아 데이털ㄹ 전송했을 때, E번 통신탑에서 가능한
# 데이터의 최소 크기를 구해보자,
# 전송이 불가능 하다면 -1
import heapq
from collections import defaultdict


def dijkstra():
    min_data_sizes = [float('inf')] * (N + 1)
    min_data_sizes[S] = 1
    hq = [(1, S)]

    while hq:
        cur_size, cur_node = heapq.heappop(hq)

        # 현재 노드(cur_node)의 데이터가 현재 크기(cur_size) 보다 작다면 무시
        if cur_size > min_data_sizes[cur_node]:
            continue

        # 인접 노드 탐색
        for next_node, max_k in graph[cur_node]:
            # cur_size가 최대 크기(max_k)의 값보다 같거나, max_k가 더 클 경우
            if max_k >= cur_size:
                # 지나갔기 때문에 다음 size는 1 증가
                next_size = cur_size + 1
                # size 가 현재 node의 최소 size 보다 작을 경우에만 갱신
                if next_size < min_data_sizes[next_node]:
                    min_data_sizes[next_node] = next_size

                    # 다음 반복을 위해 heapq에 push
                    heapq.heappush(hq, (next_size, next_node))

    # E번 통신탑에 도달 가능한지 확인
    return min_data_sizes[E] if min_data_sizes[E] != float('inf') else -1


# N:통신탑 수, M: 통신 케이블 수
N, M = map(int, input().split(" "))
# S:전송 시작 통신탑 번호, E:데이터를 받는 통신탑의 번호
S, E = map(int, input().split(" "))
# 구조 : {시작키(1): [(전송위치, 전송 크기), ...], 시작키(2):[~~~]}
graph = defaultdict(list)

for _ in range(M):
    # a, b 통신탑을 연결, 데이터크기 최대 k_i
    a, b, k = map(int, input().split(" "))
    graph[a].append((b, k))
    graph[b].append((a, k))

# 결과 계산
print(dijkstra())
