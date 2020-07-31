cont = 0
lp = int(input())
  
while lp >= 0:
    mt = int(input())
    rd = float(input())
    
    if (lp >= 40) and (mt >= 21) and (rd >= 7):
        cont += 1
        
    lp = int(input())
    
print(cont)