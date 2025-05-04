## agora vamos um pouco de execício de revisão né
print("Digite aqui o valor de tal operação:")
operacao = int(input("1.soma\n2.subtração\n3.multiplicação\n4.divisao"))

if operacao == 1:
    print("você escolheu soma agora você vai digitar os valores que deseja somar")
    soma1 = int(input("primeiro: "))
    soma2 = int(input("segundo: "))
    resultado = soma1 + soma2
    print(resultado)
elif operacao == 2:
    print("você escolheu subtração, agora você vai digitar os vamos que deseja subtrair")
    sub1 = int(input("primeiro: "))
    sub2 = int(input("segundo: "))
    resultado = sub1 - sub2
    print(resultado)
elif operacao == 3:
    print("você escolheu multiplicação, agora você vai digitar os valores que deseja multiplicar")
    multi1 = int(input("primeiro:"))
    multi2 = int(input("segundo"))
    resultado = multi1 * multi2
    print(resultado)
elif operacao == 4:
        print("você escolheu divisão, agora você vai digitar os valores que deseja multiplicar")
        div1 = int(input("primeiro:"))
        div2 = int(input("segundo"))
        resultado = div1 / div2
        print(resultado)
    