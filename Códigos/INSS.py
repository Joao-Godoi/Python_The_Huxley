sal = float(input(""))

if sal <= 1751.81:
    print("Desconto do INSS: R$ %.2f" %(sal*0.08))

elif 1751.82 <= sal >= 2919.72:
    print("Desconto do INSS: R$ %.2f" %(sal*0.09))

elif sal >= 2919.73 and sal >= 5839.45:
    print("Desconto do INSS: R$ %.2f" %(sal*0.11))

elif sal > 5839.45:
    sal2 = sal - (5839.45*0.11)
    print("Desconto do INSS: R$ %.2f" %(sal2*0.11))
    
