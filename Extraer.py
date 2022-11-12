import re
from Operaciones import Nodo
class Obtener:
    def __init__(self,cadena) -> None:
        self.cadena=cadena
        self.almacen=[]
        self.abierto=0
        self.resultado=[]
        self.operacion=r'\=\s?([A-Z]+)'
        self.numero=r'(\d+\.?\d*)'
    def datos(self):
        b=self.cadena.split("\n")
        for elem in b:
            if elem.count("\t")==1 and "Operacion" in elem:
                self.abierto+=1
                if self.abierto==2:
                    self.realizarOp()
                    self.abierto=0
                    self.almacen.clear()
                
                a=re.findall(self.operacion,elem)
                if a:
                    self.almacen.append(a[0])
            elif elem.count("\t")==2 and "Numero" in elem:
                a=re.findall(self.numero,elem)
                if a:
                    self.almacen.append(float(a[0]))
            elif elem.count("\t")==2 and "Operacion" in elem:
                a=re.findall(self.operacion,elem)
                if a:
                    self.almacen.append(a[0])
            
            elif elem.count("\t")==3 and "Numero" in elem:
                a=re.findall(self.numero,elem)
                if a:
                    self.almacen.append(float(a[0]))
            elif elem.count("\t")==3 and "Operacion" in elem:
                a=re.findall(self.operacion,elem)
                if a:
                    self.almacen.append(a[0])

            elif elem.count("\t")==4 and "Numero" in elem:
                a=re.findall(self.numero,elem)
                if a:
                    self.almacen.append(float(a[0]))
            elif elem.count("\t")==4 and "Operacion" in elem:
                a=re.findall(self.operacion,elem)
                if a:
                    self.almacen.append(a[0])
            elif elem.count("\t")==5 and "Numero" in elem:
                a=re.findall(self.numero,elem)
                if a:
                    self.almacen.append(float(a[0]))
            elif elem.count("\t")==5 and "Operacion" in elem:
                a=re.findall(self.operacion,elem)
                if a:
                    self.almacen.append(a[0])
        
        return self.resultado
    
    def realizarOp(self):
        if len(self.almacen)==3:
            ob1=Nodo(self.almacen[0],self.almacen[1],self.almacen[2])
            a=ob1.etiqueta()
            b=round(ob1.recursivo(),2)
            self.resultado.append(f"{a} = {b}")
        elif len(self.almacen)==4:
            ob1=Nodo(self.almacen[1],self.almacen[2])
            ob2=Nodo(self.almacen[0],ob1,self.almacen[3])
            a=ob2.etiqueta()
            b=round(ob2.recursivo(),2)
            self.resultado.append(f"{a} = {b}")
        elif len(self.almacen)==5:
            if isinstance(self.almacen[1],float) and isinstance(self.almacen[2],str):
                ob1=Nodo(self.almacen[2],self.almacen[3],self.almacen[4])
                ob2=Nodo(self.almacen[0],self.almacen[1],ob1)
                a=ob2.etiqueta()
                b=round(ob2.recursivo(),2)
                self.resultado.append(f"{a} = {b}")
            elif isinstance(self.almacen[1],str):
                ob1=Nodo(self.almacen[1],self.almacen[2],self.almacen[3])
                ob2=Nodo(self.almacen[0],ob1,self.almacen[4])
                a=ob2.etiqueta()
                b=round(ob2.recursivo(),2)
                self.resultado.append(f"{a} = {b}")
        elif len(self.almacen)==7:
            if isinstance(self.almacen[1],str) and isinstance(self.almacen[4],str):
                ob1=Nodo(self.almacen[1],self.almacen[2],self.almacen[3])
                ob2=Nodo(self.almacen[4],self.almacen[5],self.almacen[6])
                ob3=Nodo(self.almacen[0],ob1,ob2)
                a=ob3.etiqueta()
                b=round(ob3.recursivo(),2)
                self.resultado.append(f"{a} = {b}")
            elif isinstance(self.almacen[1],float) and isinstance(self.almacen[4],str):
                ob1=Nodo(self.almacen[4],self.almacen[5],self.almacen[6])
                ob2=Nodo(self.almacen[2],self.almacen[3],ob1)
                ob3=Nodo(self.almacen[0],self.almacen[1],ob2)
                a=ob3.etiqueta()
                b=round(ob3.recursivo(),2)
                self.resultado.append(f"{a} = {b}")
            elif isinstance(self.almacen[1],str) and isinstance(self.almacen[3],str):
                ob1=Nodo(self.almacen[3],self.almacen[4],self.almacen[5])
                ob2=Nodo(self.almacen[1],self.almacen[2],ob1)
                ob3=Nodo(self.almacen[0],ob2,self.almacen[6])
                a=ob3.etiqueta()
                b=round(ob3.recursivo(),2)
                self.resultado.append(f"{a} = {b}")
        elif len(self.almacen)==6:
            if self.almacen[0]=="INVERSO" or "TANGENTE" or "COSENO" or "SENO":
                if isinstance(self.almacen[2],float) and isinstance(self.almacen[3],str):
                    ob1=Nodo(self.almacen[3],self.almacen[4],self.almacen[5])
                    ob2=Nodo(self.almacen[1],self.almacen[2],ob1)
                    ob3=Nodo(self.almacen[0],ob2)
                    a=ob3.etiqueta()
                    b=round(ob3.recursivo(),2)
                    self.resultado.append(f"{a} = {b}")
                elif isinstance(self.almacen[3],float) and isinstance(self.almacen[4],float):
                    ob1=Nodo(self.almacen[2],self.almacen[3],self.almacen[4])
                    ob2=Nodo(self.almacen[1],ob1,self.almacen[5])
                    ob3=Nodo(self.almacen[0],ob2)
                    a=ob3.etiqueta()
                    b=round(ob3.recursivo(),2)
                    self.resultado.append(f"{a} = {b}")
                elif isinstance(self.almacen[3],float) and isinstance(self.almacen[4],str):
                    ob1=Nodo(self.almacen[2],self.almacen[3])
                    ob2=Nodo(self.almacen[4],self.almacen[5])
                    ob3=Nodo(self.almacen[1],ob1,ob2)
                    ob4=Nodo(self.almacen[0],ob3)
                    a=ob4.etiqueta()
                    b=round(ob4.recursivo(),2)
                    self.resultado.append(f"{a} = {b}")

        elif len(self.almacen)==8:
            if isinstance(self.almacen[1],str) and isinstance(self.almacen[3],str):
                ob1=Nodo(self.almacen[4],self.almacen[5])
                ob2=Nodo(self.almacen[6],self.almacen[7])
                ob3=Nodo(self.almacen[3],ob1,ob2)
                ob4=Nodo(self.almacen[1],self.almacen[2])
                ob5=Nodo(self.almacen[0],ob4,ob3)
                a=ob5.etiqueta()
                b=round(ob5.recursivo(),2)
                self.resultado.append(f"{a} = {b}")
        elif len(self.almacen)==9:
            if isinstance(self.almacen[1],str) and isinstance(self.almacen[3],str):
                ob1=Nodo(self.almacen[5],self.almacen[6])
                ob2=Nodo(self.almacen[7],self.almacen[8])
                ob3=Nodo(self.almacen[4],ob1,ob2)
                ob4=Nodo(self.almacen[3],ob3)
                ob5=Nodo(self.almacen[1],self.almacen[2])
                ob6=Nodo(self.almacen[0],ob5,ob4)
                a=ob6.etiqueta()
                b=round(ob6.recursivo(),2)
                self.resultado.append(f"{a} = {b}")











    