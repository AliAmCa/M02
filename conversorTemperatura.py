
def conversor(temp, sistema):
    if sistema ==1: #/Grados a Fahr
        
        return temp *2/5 + 32
    
    else: #Farh a Grados
        return (temp-32)* 5/9
    
    
def opcionConversion(cadena):
    if cadena=='c' or cadena=='C':
        return 1
    else:
        return 2


def validarNum():
    cadena = input("Indique la cantidad a convertir: ")
    isValid=False
    while not isValid:

        if cadena.isdigit():
            isValid=True
        else:
            print( "Los datos introducidos no son validos, vuelva a introducirlos en un formato válido")
            cadena = input("Indique la cantidad a convertir: ")
            
    return int(cadena)

strOpcion= input("Indique el sistema desde el que quiere convertir: (C o F)")

opcion= opcionConversion(strOpcion)

num= validarNum()

conversion= conversor(num,opcion)
if opcion==1:
    print("{} grados Celsius son {} grados Farhenheit".format(num,conversion))
else:
    
      print("{} grados Farhenheit son {} grados Celsius".format(num,conversion))    

