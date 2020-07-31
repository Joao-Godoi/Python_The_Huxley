import math
p1 = float(input())
p2 = float(input())
p3 = float(input())
freq = float(input())

med = (p1*2 + p2*2 + p3*3)/7
med = round(med, 1)
freq_total = freq * 100

if freq_total < 75:
    print("Frequencia: %i%%\nMedia: %.1f\nAluno reprovado por faltas!" %(freq_total, med))

elif freq_total >= 75 and med > 9:
    print("Frequencia: %i%%\nMedia: %.1f\nAluno aprovado com louvor!" %(freq_total, med))

elif freq_total >= 75 and 6 <= med <= 9:
    print("Frequencia: %i%%\nMedia: %.1f\nAluno aprovado!" %(freq_total, med))

elif freq_total >= 75 and 6 > med >= 4:
    print("Frequencia: %i%%\nMedia: %.1f\nAluno de recuperação!" %(freq_total, med))

elif med < 4:
    print("Frequencia: %i%%\nMedia: %.1f\nAluno reprovado!" %(freq_total, med))