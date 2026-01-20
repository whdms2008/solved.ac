N, M = map(int, input().split(" "))

checked = [False] * N
nums = [i+1 for i in range(N)]

def dfs(seq, idx):
    if len(seq) == M:
        print(*seq)
        return

    for i in range(idx, N):
        seq.append(nums[i])
        dfs(seq, i)
        seq.pop()

dfs([], 0)