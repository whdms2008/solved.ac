x, y, w, h = list(map(int, input().split()))

if w - x > h - y:
    if y > h - y:
        print(h - y)
    else:
        print(y, h-y)
        print(y)
else:
    if x > w - x:
        print(w-x)
    else:
        print(x)
