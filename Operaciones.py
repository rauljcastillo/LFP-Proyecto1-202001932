import math
class Nodo:
    def __init__(self,tipo,izquierda=None,derecha=None) -> None:
        self.tipo=tipo
        self.izquierda=izquierda
        self.derecha=derecha

    def recursivo(self):
        if isinstance(self.izquierda,Nodo) and isinstance(self.derecha,Nodo):
            if self.tipo=="SUMA":
                return self.izquierda.recursivo()+self.derecha.recursivo()
            elif self.tipo=="RESTA":
                return self.izquierda.recursivo()-self.derecha.recursivo()
            elif self.tipo=="MULTIPLICACION":
                return self.izquierda.recursivo()*self.derecha.recursivo()
            elif self.tipo=="DIVISION":
                return self.izquierda.recursivo()/self.derecha.recursivo()
            elif self.tipo=="POTENCIA":
                return self.izquierda.recursivo()**self.derecha.recursivo()
            elif self.tipo=="RAIZ":
                return self.derecha**(1/self.izquierda.recursivo())
                
        elif isinstance(self.izquierda,float) and isinstance(self.derecha,Nodo):
            if self.tipo=="SUMA":
                return self.izquierda+ self.derecha.recursivo()
            elif self.tipo=="RESTA":
                return self.izquierda- self.derecha.recursivo()
            elif self.tipo=="MULTIPLICACION":
                return self.izquierda*self.derecha.recursivo()
            elif self.tipo=="DIVISION":
                return self.izquierda/ self.derecha.recursivo()
            elif self.tipo=="POTENCIA":
                return self.izquierda**self.derecha.recursivo()
            elif self.tipo=="RAIZ":
                return self.derecha.recursivo()**(1/self.izquierda)


        elif isinstance(self.izquierda,Nodo) and isinstance(self.derecha,float):
            if self.tipo=="SUMA":
                return self.izquierda.recursivo()+ self.derecha
            elif self.tipo=="RESTA":
                return self.izquierda.recursivo()- self.derecha
            elif self.tipo=="MULTIPLICACION":
                return self.izquierda.recursivo()*self.derecha
            elif self.tipo=="DIVISION":
                return self.izquierda.recursivo() / self.derecha
            elif self.tipo=="POTENCIA":
                return self.izquierda.recursivo()**self.derecha
            elif self.tipo=="RAIZ":
                return self.derecha**(1/self.izquierda.recursivo())
            
        elif isinstance(self.izquierda,Nodo) and self.derecha is None:
            if self.tipo=="INVERSO":
                if self.derecha==None:
                    return 1/self.izquierda.recursivo()
                else:
                    print("Error")
            elif self.tipo=="SENO":
                return math.sin(self.izquierda.recursivo())
            elif self.tipo=="COSENO":
                return math.cos(self.izquierda.recursivo())
            elif self.tipo=="TANGENTE":
                return math.tan(self.izquierda.recursivo())
    

        if self.tipo=="RESTA":
            return self.izquierda-self.derecha
        if self.tipo=="MULTIPLICACION":
            return self.izquierda*self.derecha
        if self.tipo=="SUMA":
            return self.izquierda+self.derecha
        if self.tipo=="DIVISION":
            return self.izquierda/self.derecha
        if self.tipo=="INVERSO":
            return 1/self.izquierda
        if self.tipo=="SENO":
            return math.sin(self.izquierda)
        if self.tipo=="COSENO":
            return math.cos(self.izquierda)
        if self.tipo=="TANGENTE":
            return math.tan(self.izquierda)
        if self.tipo=="POTENCIA":
            return self.izquierda**self.derecha
        if self.tipo=="RAIZ":
            return math.pow(self.derecha,1/self.izquierda)

    
    def etiqueta(self):
        if isinstance(self.izquierda,Nodo) and isinstance(self.derecha,float):
            if self.tipo=="SUMA":
                return f"({self.izquierda.etiqueta()})"+"+"+ f"{self.derecha}"
            elif self.tipo=="RESTA":
                return f"({self.izquierda.etiqueta()})"+"-"+f"{self.derecha}"
            elif self.tipo=="MULTIPLICACION":
                return f"({self.izquierda.etiqueta()})"+"*"+f"{self.derecha}"
            elif self.tipo=="POTENCIA":
                return f"({self.izquierda.etiqueta()})"+"^"+f"{self.derecha}"
            elif self.tipo=="DIVISION":
                return f"({self.izquierda.etiqueta()})"+"/"+f"{self.derecha}"
            elif self.tipo=="RAIZ":
                return f"({self.izquierda.etiqueta()})"+"^"+f"(1/{self.derecha})"

        elif isinstance(self.izquierda,float) and isinstance(self.derecha,Nodo):
            if self.tipo=="SUMA":
                return f"{self.izquierda}"+"+"+ f"({self.derecha.etiqueta()})"
            elif self.tipo=="RESTA":
                return f"{self.izquierda}"+"-"+f"({self.derecha.etiqueta()})"
            elif self.tipo=="MULTIPLICACION":
                return f"{self.izquierda}"+"*"+f"({self.derecha.etiqueta()})"
            elif self.tipo=="POTENCIA":
                return f"{self.izquierda}"+"^"+f"({self.derecha.etiqueta()})"
            elif self.tipo=="DIVISION":
                return f"{self.izquierda}"+"/"+f"({self.derecha.etiqueta()})"
            elif self.tipo=="RAIZ":
                return f"{self.izquierda}"+"RAIZ"+f"({self.derecha.etiqueta()})"
        
        elif isinstance(self.izquierda,float) and self.derecha is None:
            if self.tipo=="INVERSO":
                return (f"1/{self.izquierda}")
            if self.tipo=="TANGENTE":
                return (f"TAN({self.izquierda})")
            if  self.tipo=="SENO":
                return (f"SEN({self.izquierda})")
            if self.tipo=="COSENO":
                return (f"COS({self.izquierda})")

        elif isinstance(self.izquierda,Nodo) and self.derecha is None:
            if self.tipo=="INVERSO":
                return (f"1/({self.izquierda.etiqueta()})")
            elif self.tipo=="TANGENTE":
                return (f"TAN({self.izquierda.etiqueta()})")
            elif  self.tipo=="SENO":
                return (f"SEN({self.izquierda.etiqueta()})")
            elif self.tipo=="COSENO":
                return (f"COS({self.izquierda.etiqueta()})")
            

        elif isinstance(self.izquierda,Nodo) and isinstance(self.derecha,Nodo):
            if self.tipo=="SUMA":
                return f"({self.izquierda.etiqueta()})"+"+"+ f"({self.derecha.etiqueta()})"
            elif self.tipo=="RESTA":
                return f"({self.izquierda.etiqueta()})"+"-"+ f"({self.derecha.etiqueta()})"

            elif self.tipo=="MULTIPLICACION":
                return f"({self.izquierda.etiqueta()})"+"*"+ f"({self.derecha.etiqueta()})"
            elif self.tipo=="DIVISION":
                return f"({self.izquierda.etiqueta()})"+"/"+ f"({self.derecha.etiqueta()})"
            elif self.tipo=="POTENCIA":
                return f"({self.izquierda.etiqueta()})"+"^"+ f"({self.derecha.etiqueta()})"
            elif self.tipo=="RAIZ":
                return f"({self.izquierda.etiqueta()})"+"RAIZ"+ f"({self.derecha.etiqueta()})"

        if isinstance(self.derecha,float) and isinstance(self.izquierda,float):
            if self.tipo=="SUMA":
                return (f"{self.izquierda}+{self.derecha}")
            elif self.tipo=="MULTIPLICACION":
                return (f"{self.izquierda}*{self.derecha}")
            elif self.tipo=="RESTA":
                return (f"{self.izquierda}-{self.derecha}")
            elif self.tipo=="DIVISION":
                return (f"{self.izquierda}/{self.derecha}")
            elif self.tipo=="POTENCIA":
                return (f"{self.izquierda}^{self.derecha}")
            elif self.tipo=="RAIZ":
                return (f"{self.izquierda} RAIZ {self.derecha}")



