def retrocontador(e):
    print("{},".format(e),end="")
    
    if e>0:
        retrocontador(e-1)
        
        
        
retrocontador(10)

def sumatorio(e):
    sumatorio=0
    if e>0:
        sumatorio = e + sumatorio(e-1)
    return sumatorio


print("{}".format(sumatorio(4)))