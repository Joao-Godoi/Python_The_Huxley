ig, ia, enc, iden, struc = input().split()
ig, ia, enc, iden, struc = int(ig), int(ia), int(enc), int(iden), int(struc)

if (ig == 1 or ia == 1) and (enc == 1 and iden == 1) and (struc == 1):
    print("AVALIADO")
    
else:
    print("0")