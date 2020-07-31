pa = []
r = int(input())
ult = int(input())

qtd_ele = ult/r
qtd_ele = round(qtd_ele + 0.5)
n = qtd_ele - 1

primeiro = ult - n * r

for x in range(primeiro, ult, r):
    pa.append(x)
print("A somatoria da PA eh: %i" %(sum(pa)+ult))