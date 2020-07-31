nac = input()
ocupa = input()
qtd = int(input())
cali = int(input())

if (ocupa == 'M'):
    print("Liberado")
        
elif (nac == 'E') and (qtd == 0):
    print("Liberado")
    
elif (nac == 'E'):
    print("Barrado")
    
elif (ocupa != 'E') and ((ocupa == 'T') or (ocupa == 'O')) and (cali <= 22):
    print("Liberado")
    
elif (ocupa == 'C') and (qtd <= 2) and (cali <= 38):
    print("Liberado")
    
else:
    print("Barrado")