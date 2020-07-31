prato = input("")
bebida = input()

prato = prato.lower()
bebida = bebida.lower()

if prato == 'estrogonofe' and bebida == 'refrigerante':
    print("14.00")

elif prato == 'estrogonofe' and bebida == 'suco':
    print("13.50")

elif prato == 'lasanha' and bebida == 'refrigerante':
    print("11.00")

elif prato == 'lasanha' and bebida == 'suco':
    print("10.50")