x1, y1 = input().split()
x2, y2 = input().split()
x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

d = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5

print("%.4f" % d)