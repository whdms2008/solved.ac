import sys

def input():
    return sys.stdin.readline().strip()

print(sorted([int(input()) for _ in range(3)])[1])
