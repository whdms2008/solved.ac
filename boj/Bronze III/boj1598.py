num1, num2 = map(int, input().split())

# 1 >= 40
x = abs((value+1 if ( value := num1 // 4) == 0 else value) - (value+1 if ( value := num2 // 4) == 0 else value))
#
y = abs(num1 % 4 - num2 % 4)
print(x, y)
print(abs(x + y))