from sys import stdin


def round_cus(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)


N = int(stdin.readline())
if not N:
    print(0)
else:
    dicts = [int(stdin.readline()) for _ in range(N)]
    dicts.sort()
    line = round_cus(N * 0.15)
    if line != 0:
        dicts = dicts[line:-line]
    print(round_cus(sum(dicts) / (N - 2 * line)))
