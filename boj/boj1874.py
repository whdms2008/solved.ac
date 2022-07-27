from sys import stdin

input = stdin.readline

N = int(input())

nums = [int(input()) for _ in range(N)]
data = list(range(1,nums[0]+1))
i = len(data)
result = ["+"] * (i)
while nums:
    if len(data) == 0 or data[-1] < nums[0]:
        if i < nums[0]:
            a = nums[0]
            data += list(range(i+1, a+1))
            result += ["+"] * (a-i)
            i += 1*a-i
            continue
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


