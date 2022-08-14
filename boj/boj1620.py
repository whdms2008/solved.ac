from sys import stdin

input = stdin.readline
N, M = map(int, input().split(" "))
dic = {}
for i in range(1, N+1):
    name = stdin.readline().strip()
    dic[i] = name
    dic[name] = i
for _ in range(M):
    quiz = input()[:-1]
    print(dic[int(quiz)] if quiz.isdigit() else dic[quiz])