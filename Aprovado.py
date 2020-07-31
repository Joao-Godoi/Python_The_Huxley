n1 = float(input())
n2 = float(input())
n3 = float(input())

med = (n1+n2+n3)/3

if med >= 7:
    print("aprovado")

elif med < 3:
    print("reprovado")

elif 3 <= med < 7:
    print("prova final")