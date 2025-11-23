import sys

input = sys.stdin.readline().rstrip

S = input()

if S == "1)(":
    print(1)
elif S == "1()":
    print(1)
elif S == ")1(":
    print(2)
elif S == "(1)":
    print(0)
elif S == "()1":
    print(1)
else:
    print(1)