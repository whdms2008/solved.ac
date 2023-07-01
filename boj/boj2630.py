from sys import stdin


def chk_color(paper, white, blue):
    datas = [[], [], [], []]
    flat = [item for sublist in paper for item in sublist]
    N = len(paper)

    if flat.count(0) == len(flat) or flat.count(1) == len(flat):
        return white + (flat.count(0) == len(flat)), blue + (flat.count(1) == len(flat))
    elif N != 1:
        for p in paper[:N // 2]:
            datas[0].append(p[:N // 2])
            datas[1].append(p[N // 2:])
        for p in paper[N // 2:]:
            datas[2].append(p[:N // 2])
            datas[3].append(p[N // 2:])
        for data in datas:
            white, blue = chk_color(data, white, blue)
        return white, blue


for i in chk_color([list(map(int, stdin.readline().split())) for j in range(int(stdin.readline()))], 0, 0):
    print(i)
