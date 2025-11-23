from collections import deque
from sys import stdin


def valid(grid, row, col):
    m, n = len(grid), len(grid[0])
    return 0 <= row < m and 0 <= col < n and grid[row][col] == 0


def get_neighbor(row, col):
    return [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]


def get_tomato(grid, n, m):
    queue = deque()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                queue.append((i, j, 0))
    days = 0
    while queue:
        row, col, days = queue.popleft()
        for neighbor in get_neighbor(row, col):
            if valid(grid, *neighbor):
                grid[neighbor[0]][neighbor[1]] = 1
                queue.append((neighbor[0], neighbor[1], days + 1))

    for row in grid:
        if 0 in row:
            return -1

    return days


N, M = list(map(int, stdin.readline().split()))

maze = [list(map(int, stdin.readline().split())) for _ in range(M)]
print(get_tomato(maze, N, M))
