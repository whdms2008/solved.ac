import sys

def input():
    return sys.stdin.readline()


while True:
    num = int(input())
    if num == 0:
        break
    print(sum([n for n in range(num, 0, -1)]))