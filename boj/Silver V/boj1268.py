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
grades = defaultdict(set[int])

for student_number in range(N):
    for idx, grade in enumerate(matrix[student_number]):
        class_list = [(std_num, matrix[std_num][idx]) for std_num in range(N) if
                      std_num != student_number and matrix[std_num][idx] == grade]
        for std_num, class_num in class_list:
            grades[student_number].add(std_num)
            grades[std_num].add(student_number)

result = 0
if grades.values():
    max_length = max(len(items) for items in grades.values())
    result = min({key: items for key, items in grades.items() if len(items) == max_length})

print(result + 1)

# 나중에 최적화 해보자!
# matrix = [list(map(int, input().split())) for _ in range(N)]
# grades = []
# for i in range(N):
#     grades.append([])
#     for j in range(N):
#         grades[-1].append(matrix[j][i])
# print(grades)