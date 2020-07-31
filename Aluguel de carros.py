dias = int(input("Digite a quantidade de dias de locacao:\n"))
km = float(input("Digite a quantidade de km rodados:\n"))

total_dias = dias * 30
total_km = km * 0.01
total = (total_dias + total_km) * 0.9

print("Valor a pagar pelo aluguel: R$ %.6f" % total)