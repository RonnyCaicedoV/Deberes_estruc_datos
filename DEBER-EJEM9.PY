#Elabore pseudocódigo para el caso en que se desean escribir los números 
# del 1 al 100

class Ejemwhile:
    def __init__(self):
        pass
    
    def pseudo (self):
        Numero=  int(input("Digite su  numero: "))
        while Numero <= 100 :
            print("Su numero ha sido ingresado con exito: ",Numero)
            Numero= Numero+1
        
      
        
        
        
            
ejewhile= Ejemwhile()
ejewhile.pseudo()