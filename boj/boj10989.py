import sys

T = int(sys.stdin.readline())
a = []
for i in range(T):
    a.append(int(sys.stdin.readline()))
a.sort()
result = ""
for i in a:
    result += str(i)+"\n"
print(result)