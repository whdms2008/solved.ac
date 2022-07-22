import sys

N, M = map(int, sys.stdin.readline().strip().split(" "))
board = []
for i in range(N):
    data = sys.stdin.readline().strip()
    board.append(data)
cnts = []
for i in range(N - 7):
    for j in range(M - 7):
        cnt = [0, 0]
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    cnt[board[k][l] != 'W'] += 1
                else:
                    cnt[board[k][l] != 'B'] += 1
        cnts.append(min(cnt))
print(min(cnts))
