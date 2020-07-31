nvoltas = 1
linhas = 1
voltas = 1
ent = int()

n, m = input().split()
n, m = int(n), int(m)

while linhas != n:
    while voltas != m:
        tempo = [int(input()) for v in m]
        voltas = voltas + 1

    linhas += 1