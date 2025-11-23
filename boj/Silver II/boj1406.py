# L : 커서를 왼쪽으로 1칸 옮김, 문장의 맨 앞이면 무시
# D : 커서를 오른쪽으로 한 칸 옮김, 문장의 맨 뒤이면 무시
# B : 커서 왼쪽에 있는 문자를 삭제함 ( 문장의 맨 앞이면 무시됨 )
# 삭제로 인해 커서가 한 칸 왼쪽으로 이동한 것 처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
# P $ : $ 라는 문자를 커서 왼쪽에 추가함.
import sys
input = sys.stdin.readline

left = list(input().strip())
right = []
M = int(input().strip())

for _ in range(M):
    command = input().strip().split(" ")
    match command[0]:
        case "L":
            if left:
                right.append(left.pop())
        case "D":
            if right:
                left.append(right.pop())
        case "B":
            if left:
                left.pop()
        case "P":
            left.append(command[1])

print("".join(left + right[::-1]))
