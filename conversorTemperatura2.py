class Termometro():
    def __init__(self):
        self.__unidad= 'C'
        self.__temperatura=0
        
        
    def __conversor(self, temp, unidad):
        if unidad.upper()=='C': #/Grados a Fahr
        
            return "{}ºF".format(temp *9/5 + 32)
    
        elif unidad.upper()=='F': #Farh a Grados
            return "{}ºC".format((temp-32)* 5/9)
        
        else:
            return "unidad incorrecta"
    
    def __str__(self):
        return "{}º {}".format(self.__temperatura,self.__unidad)
    
        
    def unidad(self, uniM=None):
        if uniM==None:
            return self.__unidad
        else:
            if uniM=='F' or uniM=='C':
                self.__unidad =uniM
                
    def temp(self,temperatura=None):
        if temperatura==None:
            return self.__temperatura
        else:
            self.__temperatura =temperatura
            
    def mide(self,uniM=None):
        if uniM==None or uniM == self.__unidad:
            return self.__str__()
        
        else:
            return self.__conversor(self.__temperatura,self.__unidad)