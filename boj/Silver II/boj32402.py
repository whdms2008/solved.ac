person = [0, 0]
camera = [0, -1]

# 방향에 따른 이동 벡터
move_vectors = {
    'W': [(0, 1), (1, 0), (0, -1), (-1, 0)],
    'S': [(0, -1), (-1, 0), (0, 1), (1, 0)],
    'A': [(-1, 0), (0, 1), (1, 0), (0, -1)],
    'D': [(1, 0), (0, -1), (-1, 0), (0, 1)]
}

mouse_pos = 0
N = int(input())
for _ in range(N):
    COMMAND = input()
    if COMMAND == "MR":
        mouse_pos = (mouse_pos + 1) % 4
        dx = camera[0] - person[0]
        dy = camera[1] - person[1]
        # 시계 방향 90도 회전
        camera[0] = person[0] + dy
        camera[1] = person[1] - dx
    elif COMMAND == "ML":
        mouse_pos = (mouse_pos - 1) % 4
        dx = camera[0] - person[0]
        dy = camera[1] - person[1]
        # 반시계 방향 90도 회전
        camera[0] = person[0] - dy
        camera[1] = person[1] + dx
    elif COMMAND in ['W', 'A', 'S', 'D']:
        move_x, move_y = move_vectors[COMMAND][mouse_pos]
        person[0] += move_x
        person[1] += move_y
        camera[0] += move_x
        camera[1] += move_y
    else:
        continue  # 유효하지 않은 입력은 무시
    print(f"{person[0]} {person[1]} {camera[0]} {camera[1]}")
