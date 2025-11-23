import sys

def input():
    return sys.stdin.readline()

while True:
    nums = input().split(" ")
    if len(nums) == 1:
        break

    n, m = map(int, nums)

    print(int(m / (n + 1)))
