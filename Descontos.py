ent = float(input("Preço do produto: R$"))
desc = float(input("De qunato é o desconto: "))

desconto = (ent * desc) / 100
pfinal = ent - desconto

print("\nO preço final é de %.2f reais" %(pfinal))
