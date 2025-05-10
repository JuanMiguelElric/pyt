## uma função é recursiva quando podemos chamar ela dentro da sua própria função

def fatorial(n):
    print(f"Calculando o fatorial de {n}")
    if n == 0  or n == 1:
        print(f"Fatorail de {n}=1")
        return 1 
    else:
        return n * fatorial(n - 1)