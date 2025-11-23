# 귀걸이를 돌려받지 못한 소녀의 이름을 교장에게 알려라

# 입력
"""
시나리오 번호1부터 순서대로 증가, 각 시나리오는 아래 내용을 포함.
1. 한 줄에 귀걸이를 압수당한 여학생의 수, n (1 <= n <= 100)이 주어짐
2. 다음 n줄에 걸쳐 여학생들의 이름(최대 60자)이 주어집니다.
3. 다음 2n - 1줄에 여학생 번호와 'A'또는 'B'가 공백을 사이에 두고 주어집니다.
번호는 교감선생님의 여학생 이름 리스트와 순서가 일치,
즉, 1은 첫 번째로 압수당한 여학생
여학생 번호는 최대 2번 등장하며,
두 번째로 등장할대는 첫번째 경우와 다른 'A' 또는 'B'가 뒤에 적힙니다.
번호가 처음 등장하는 것은 압수되었음을, 두 번째로 등장하는 것은 돌려받았음을 의미

'0' 을 마지막 줄로 하여 입력을 종료 '0'은 처리하지 않음
"""

# 출력
"""
시나리오 번호와 귀걸이를 돌려받지 못한 여학생의 이름을 공백으로 구분하여 한 줄씩 출력
"""
scenario_num = 1
scenario_list = dict()
while True:
    n = int(input())
    if n == 0:
        break
    scenario_list[scenario_num] = []
    girls = []

    for i in range(n):
        girls.append(input())

    chk_list = dict()
    for _ in range(2 * n - 1):
        num, alpha = input().split()
        num = int(num)
        if not chk_list.get(num):
            chk_list[num] = alpha
        else:
            chk_list.pop(num)
    scenario_list[scenario_num] = girls[list(chk_list.keys())[0]-1]
    scenario_num += 1
for idx, girl in scenario_list.items():
    print(idx, girl)