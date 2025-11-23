num = input()
if "7" not in num:
    if int(num) % 7 != 0:
        print("0")
    else:
        print("1")
else:
    if int(num) % 7 != 0:
        print("2")
    else:
        print("3")