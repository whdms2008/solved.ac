import sys

a = int(sys.stdin.readline())  # 값을 입력 받는다
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:  # 4의 배수이고, 100의 배수가 아니거나 400의 배수일 경우 윤년(1)
    print(1)  # 윤년
else:
    print(0)  # 윤년아님
