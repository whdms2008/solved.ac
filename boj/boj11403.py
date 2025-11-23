"""
[ 문제 ]
가중치가 없는 방향 그래프 G가 주어졌을 때, 모든 정점( i,j)에 대해서,
i에서 j로 가는 길이가 양수인 경로가 있는지 없는지 구하는 프로그램 작성

[ 입력 ]
첫째 줄에 정점의 개수 N (1<=N<=100)이 주어진다.
둘째 줄부터 N개의 줄에는 그래프의 인접 행렬이 주어진다.
i번째 줄의 j번째 숫자가 1인 경우에는 i에서 j로 가는 간선이 존재한다는 뜻
0인 경우 없다는 뜻이다. i번 째 줄의 i번째 숫자는 항상 0이다.

[ 출력 ]
총 N개의 줄에 걸쳐서 문제의 정답을 인접행렬 형식으로 출력한다.
정점 i에서 j로 가는 길이가 양수인 경로가 있으면 i번째 줄의 j번째 숫자를 1로 없으면 0 출력
"""

N = int(input())

matrix = [list(map(int, input().split(" "))) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if matrix[i][k] == 1 and matrix[k][j] == 1:
                matrix[i][j] = 1

for line in matrix:
    print(*line)