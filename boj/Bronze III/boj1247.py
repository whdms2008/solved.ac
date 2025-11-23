import sys

input = sys.stdin.readline

for _ in range(3):
    N = int(input())
    result = sum([int(input()) for num in range(N)])
    print("0" if result == 0 else "+" if result > 0 else "-")