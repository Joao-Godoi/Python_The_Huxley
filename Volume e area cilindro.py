h = float(input())
r = float(input())

area = (2 * (3.14 * (r * r))) + (2 * (3.14 * r * h))
vol = 3.14 * (r * r) * h

print("%.2f" % vol)
print("%.2f" % area)