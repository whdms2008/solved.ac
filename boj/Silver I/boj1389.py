# 케빈 베이컨의 6단계 법칙

# 케빈 베이컨의 6단계 법칙에 의하면 지구상의 모든 사람들은
# 최대 6단계 이내에서 서로 아는 사람으로 연결될 수 있음

# 임의의 두 사람이 최소 몇 단계 만에 이어질 수 있는지 계산하는 게임

# 케빈 베이컨의 수가 가장 작은 사람을 찾으려 한다.
# 유저가 5명
# 1 : [3], 2 :[3], 3 :[4], 4:[5]가 친구인 경우를 생각

# 1은 2깢 ㅣ3을 통해 2단계 만에, 3까지 1단계, 4까지 1단계, 5까지 4를 통해서
# 2단계 만에 알 수 있다. 따라서
# 케비 베이컨의 수는 2+1+1+2 = 6이다.
#

# 입력
"""
첫째 줄에 유저의 수 N(2<= N <= 100)과 친구 관계의 수 M(1 <= M <=5,000)이 주어진다.
둘째 줄 부터 M개의 줄에는 친구 관계가 주어진다.
친구 관계는 A, B로 이루어져있으며, A,B가 친구란 뜻이며, B, A가 친구이며, A, B가 같은 경우는 없다.
친구 관계는 중복되어 들어올 수도 있으며, 친구가 한 명도 없는 사람은 없다.
또 모든 사람은 친구 관계로 연결되어져 있다. 사람의 번호는 1부터 N까지이며, 두 사람이 같은 버노를 갖는 경우는 없다.
"""

# 출력
"""
첫째 줄에 BOJ 유저 중 케빈 베이컨의 수가 가장 작은 사람을 출력한다.
그런 사람이 여러명일 경웅는 번호가 가장 작은 사람을 출력한다.
"""
from collections import deque, defaultdict

def bfs(graph, start):
    visited = {start:0}
    q = deque([start])
    while q:
        current = q.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited:
                q.append(neighbor)
                visited[neighbor] = visited[current] + 1
    return sum(visited.values())

N, M = map(int, input().split(" "))

graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

min_val = 9999
min_id = -1
for i in range(1, N+1):
    ret = bfs(graph, i)
    if ret < min_val:
        min_id = i
        min_val = ret
print(min_id)