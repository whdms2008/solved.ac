for i in range(int(input())):
    result = ""
    num, Str = input().split(" ")
    for j in range(len(Str)):
        result += Str[j] * int(num)
    print(result)
