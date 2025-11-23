import sys

def input():
    return sys.stdin.readline()

print("go" if len(input()) >= len(input()) else "no")