"""
자연수 N, M이 주어졌을 때, 아래조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성

- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
- 고른 수열은 오름차순이어야 한다.

[ 입력 ]
- 첫째 줄에 자연수 N과 M이 주어진다. ( 1<= M <= N <= 8 )

[ 출력 ]
- 한 줄에 하나 씩 문제으 조건을 만족하는 숭려을 출력한다.
중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.
예제 1 )
3 1
=>
1
2
3

예제 2)
4 2
=>
1 2
1 3
1 4
2 3
2 4
3 4
"""

N, M = map(int, input().split(" "))

checked = [False] * N
nums = [i+1 for i in range(N)]

def dfs(seq, idx):
    if len(seq) == M:
        print(*seq)
        return

    for i in range(idx, N):
        if checked[i]:
            continue
        seq.append(nums[i])
        checked[i] = True
        dfs(seq, i+1)
        seq.pop()
        checked[i] = False

dfs([], 0)