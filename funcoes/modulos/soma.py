import entrada
l = []

for x in range(10):
    l.append(entrada.valida_inteiro("digite um numero:", 0, 20))
    print(f"soma:{sum(l)}")