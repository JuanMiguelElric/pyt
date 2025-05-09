palavra = input("Digite a palavra secreta:")
for x in range(100):
    print()
digitadas =[]
acertos =[]
erros =[]
while True:
    senha = ""
    for letra in palavra:
        senha+= letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print("você acertou")
        break
    tentativa = input("\n Digite uma letra:").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou essa letra")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
        print("X==:==\X : ")
        print("X 0" if erros >= 1 else "x")
        linha2=""
        if erros == 2:
            linha2= " | "
        elif erros == 3:
            linha2=" \| "
        elif erros == 4:
            linha2 = "\|/"
        print(f"X{linha2}")
        linha3="" 
        if erros == 5:
            linha3 += "/"
        elif erros >=6 :
            linha3 += "/ |"
        print(f"x{linha3}")
        print("X\n===================================================")
        if erros == 6:
            print("Enforcado")
            break
