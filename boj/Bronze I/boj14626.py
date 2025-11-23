numbers = input()

for i in range(10):
    result = 0
    for idx, num in enumerate(numbers.replace("*", str(i))):
        num = int(num)
        result += num if idx % 2 == 0 else num*3

    if result % 10 == 0:
        print(i)
        break
