def sumatorioRecursivo(n):
    suma=0
    if n>0:
        suma = n + sumatorio(n-1)
    return suma


print("{}".format(sumatorio(4)))