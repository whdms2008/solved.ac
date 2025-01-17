# 이름 나이 몸무게
# 나이 17세 초과, 몸무게 80kg 이상이면 성인
# 이 밖은 모두 청소년

import sys

input = sys.stdin.readline

while True:
    name, age, weight = input().split(" ")

    if name == "#":
        break

    if int(age) > 17:
        print(f"{name} Senior")
        continue
    if int(weight) >= 80:
        print(f"{name} Senior")
        continue
    print(f"{name} Junior")
