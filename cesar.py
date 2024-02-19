class Cesar:
    alfabeto=list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
    def __init__(self,clave):
        if isinstance(clave,int):
            self.clave=clave
        else:
            raise AttributeError(f'{clave} debe ser un entero')
    
      
    def encriptar(self,mensaje):
        mensaje_encriptado="" 
        for caracter in mensaje:
            pos=self.alfabeto.index(caracter)
            pos2=pos+self.clave
            new_caracter=self.alfabeto[pos2]
            mensaje_encriptado+=new_caracter
        return mensaje_encriptado
    

            
