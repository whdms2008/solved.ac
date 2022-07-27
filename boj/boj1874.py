from sys import stdin

input = stdin.readline

N = int(input())

nums = [int(input()) for _ in range(N)]
data = [1]
i = 2
result = ["+"]
while nums:
    if len(data) == 0 or data[-1] < nums[0]:
        result.append("+")
        data.append(i)
        i += 1
    elif data[-1] == nums[0]:
        result.append("-")
        del data[-1]
        del nums[0]
    else:
        print("NO")
        exit()

for i in result:
    print(i)
