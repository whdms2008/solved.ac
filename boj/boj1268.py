# 임시 반장 정하기

# 1학년 부터 5학년까지 지내오면서
# 한번이라도 같은 반이었던 사람이 가장 많은 학생을 임시 반장으로 정하려 한다.

# 각 학생들이, 1학년 ~ 5학년 까지 몇 반에 속했었는지를 나타내는 표를 만듦

# 학생마다, 학년 마다 겹치는 수가 가장 높은 학생을 선정

# 그냥 겹치는 애들 모두 학년에 넣고 하는건?

# 예 )
# 1: {}, 2: {3:[3, 4]}, 3: {2:[3,4,5]}, 4: {6:[2, 4]}, 5: {}
# 1: [0, 0, 0, 0, 0], 2: [0, 0, 0, 1, 0], 3: [0, 1, 1, 0, 0], 4: [0, 1, 1, 1, 0 ]

# 결국 학생끼리 알고있는지에 대해서도 체크 해야함.
# 한번 체크된 학생은 별도의 리스트가 필요하려나? 정말 개수만 넣을지, 아니면 학생 번호를 넣을지..

# 학생 번호를 넣는게 나을 듯 하다.
# 어차피 최대 값은 항상 N이다.

# 학생번호를 key로 하고 value를 학생 번호로

# {1 : [], 2: [4], 3:[4, 5], 4:[2, 3, 5], 5:[3, 4]

from collections import defaultdict

N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]
grades = []


for i in range(5):
    grades.append([])
    for j in range(N):
        grades[-1].append((j, matrix[j][i]))
print(grades)

cnt_student = defaultdict(list)
for i in range(N):
    for j in range(5):
        result = list(filter(lambda student: student[1] == grades[i], grades[1]))
        print(result)

