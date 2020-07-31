seg = int(input())

dias = seg // 86400
hora = (seg % 86400) - seg // 3600
minu = (seg % 3600) - seg // 60
seg = 0

print(int(dias))
print(int(hora))
print(int(minu))
print(int(seg))