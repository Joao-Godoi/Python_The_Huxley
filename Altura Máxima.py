import math
ang = float(input())
v = float(input())
g = float(input())

vf = v ** 2
sen = (math.sin(ang)) ** 2
gf = 2 * g

h = (vf * sen) / gf
print(h)