temp = float(input())

t_celsius = (temp - 32) * 5/9
t_kelvin = t_celsius + 273.15

print("Convertendo",temp, "°F temos:")
print(t_celsius,"°C e", t_kelvin, "K")
