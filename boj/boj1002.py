import sys
import math


def turret(x1, y1, r1, x2, y2, r2):
    # 두 원의 중심 사이 거리 계산
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # 무한대 경우 (두 원이 완전히 일치)
    if x1 == x2 and y1 == y2 and r1 == r2:
        return -1

    # 접점 개수 판별
    if d > r1 + r2:  # 두 원이 서로 떨어져 있음
        return 0
    elif d < abs(r1 - r2):  # 한 원이 다른 원 내부에 있지만 접하지 않음
        return 0
    elif d == r1 + r2:  # 외접
        return 1
    elif d == abs(r1 - r2):  # 내접
        return 1
    else:  # 두 점에서 만남
        return 2


T = int(sys.stdin.readline().strip())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    print(turret(x1, y1, r1, x2, y2, r2))
