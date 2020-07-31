n1 = float(input("Informe a primeira nota:"))
n2 = float(input("Informe a segunda nota:"))
n3 = float(input("Informe a segunda nota:"))

med = (n1 + n2 + n3) / 3

if med >= 7:
    print("Aprovado com media %.1f" % med)
    
elif med >= 5 and med < 7:
    print("Recuperacao com media %.1f" % med)
    
elif med < 5:
    print("Reprovado com media %.1f" % med)