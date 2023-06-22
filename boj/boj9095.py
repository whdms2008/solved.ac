from sys import stdin

def sol(n):
    return 1 if n == 1 else 2 if n == 2 else 4 if n == 3 else sol(n - 1) + sol(n - 2) + sol(n - 3)


for _ in range(int(stdin.readline())):
    print(sol(int(stdin.readline())))
