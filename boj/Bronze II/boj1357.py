x, y = input().split(" ")

def rev(num):
    return num[::-1]

rev_x = int(rev(x))
rev_y = int(rev(y))

print(int(rev(str(rev_x + rev_y))))