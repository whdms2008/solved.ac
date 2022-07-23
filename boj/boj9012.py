import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    ps = input().strip()
    while True:
        if "()" in ps:
            ps = ps.replace("()", "")
        elif len(ps) == 0:
            print("YES")
            break
        else:
            print("NO")
            break
