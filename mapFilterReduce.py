from functools import reduce

def doble(x):
    return x+x


def esPar(x):
    return x%2==0

lista = [1,3,-1,15,9]

listaDobles = map(lambda x: x*2,lista)
listaDobles1= map(doble,lista)

listaPares =filter(lambda x: x%2==0,lista)
listaPares1= filter(esPar,lista)

listaImpares =filter(lambda x: x%2!=0,lista)

sumatorio= reduce(lambda x,y:x+y,lista)

suma100= reduce(lambda x,y: x+y,range(101))

sumatorioDobles= reduce(lambda x,y: x+y+y,lista)

print(list(listaPares))
print(list(listaPares1))
print(sumatorio)
print(sumatorioDobles)
print(suma100)