## presta atenção em como é feito o for em python 

##lista = [8,9,15]

##for e in lista:
 ##   print(e)

##   bem diferente do php onde seria for($i=0; $i>=10; $i++)
"""
l = [5, 9, 13]

for x, e in enumerate(l):

    print(F"{(x)} {e}")
"""
## verificando menor e maior valor 

l = [1, 7, 2, 4]
maxim = l[0]
for e in l:
    if e > maxim:
        maxim = e
print(maxim)