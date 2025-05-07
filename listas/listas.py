## o tamano de uma lista é igual à quantidade de elementos que ela contém

## programa calculo de media
"""
notas = [6, 8, 9, 3, 6]
soma = 0
x = 0
while x < 5:
    soma += notas[x]
    x += 1
print(f"Média: {soma / x:5.2f}")
"""

## simulação de uma fila 
"""
ultimo = 10
fila = list(range(1,ultimo + 1))

while True:
    print(f"\n Existem {len(fila)} clientes na fila")
    print(f"fila atual {fila}")
    print("Digite f para inserir um cliente ao fim da fila.")
    print("ou a para realizar o atendimento. s para sair")
    operacao = input("Operação (f, a ou s): ")
    if operacao == "a":
        if len(fila) >= 0 :
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido!")
        else:
            print("fila vazia amigos")
    elif operacao == "f":
        ultimo += 1
        fila.append(ultimo)
    elif operacao == "s":
        break
    else:
        print("operação invalida! Digite apenas F, A ou S!")

        

"""