a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

area_tri = (a * c) / 2

area_circ = 3.14159 * (c * c)

area_trap = ((a + b) * c) / 2

area_quad = b * b

area_retan = a * b

print("TRIANGULO: %.3f" % area_tri)
print("CIRCULO: %.3f" % area_circ)
print("TRAPEZIO: %.3f" % area_trap)
print("QUADRADO: %.3f" % area_quad)
print("RETANGULO: %.3f" % area_retan)