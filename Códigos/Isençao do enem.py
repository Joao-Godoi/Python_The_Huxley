rela_esnmed = input()
ence = input()
nota_ence = int(input())
tipo_esco = input()
renda = float(input())

if ((rela_esnmed != "CLD") or (rela_esnmed != 'CVC') or (rela_esnmed != 'CSC') or (rela_esnmed != 'NCC')): print("Informacao sobre ensino medio invalida")

elif (rela_esnmed == 'CVC'): print("Voce terah direito a isencao") 

elif (ence == 's') and (nota_ence >= 400): print("Voce terah direito a isencao")

elif ((tipo_esco == 'PUB') or (tipo_esco == 'PCB')) and (renda <= 1431): print("Voce terah direito a isencao")

elif (tipo_esco == 'PUB') or (tipo_esco == 'PCB') and (renda > 1431): print("Infelizmente voce nao tem direito a isencao")

elif (tipo_esco == 'PSB') or (tipo_esco == 'PPS') or (tipo_esco == 'PPB') or (tipo_esco == 'NFE'): print("Infelizmente voce nao tem direito a isencao")
