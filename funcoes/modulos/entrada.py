## Programa Modulo entrada

def valida_inteiro(mensagem, minimo, maximo):
    while True:
        try:
            v = int(input(mensagem))
            if v >= minimo and v <= maximo:
                return v
            else:
                print(f"Digite um valor ente {minimo} e {maximo}")
        except ValueError:
            print("Você deve digitar um numero inteiro")