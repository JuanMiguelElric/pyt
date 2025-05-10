## Cálculo de fatorial

def fatorial(n):
    fat =1
    while n> 1:
        fat *= n
        n -= 1
    return fat


"""
python tem funções para calcular a soma o máximo e o minimo de uma lista
L=[5, 7, 8]
sum(L)
max(L)
min(L)
"""

## variavel global é criada fora do escopo de uma função 

## variável local é criada dentro do escopo de uma função

a = 5
def muda_e_imprime():
    a = 7
    print(f"A dentro da função: {a}")

print(f"a antes de mudar:{a}")

muda_e_imprime()
print(f"a depois de mudar: {a}")

