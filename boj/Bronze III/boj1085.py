x, y, w, h = list(map(int, input().split()))
w = w-x
h = h-y
print(min(x,y,w,h))
