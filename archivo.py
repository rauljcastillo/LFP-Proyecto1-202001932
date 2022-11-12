from tokens import Tokens
from Almacenar import Errores
import webbrowser

class Analizar:
    t_Estilo=r'\/(Texto)' 
    def __init__(self,cadena) -> None:
        self.columna=1
        self.linea=1
        self.cadena=cadena
        self.estado=0
        self.contador=0
        self.paso=False
        self.error=[]
        self.token=[]
        self.colors=[]
        self.tkn=""
        self.texto=""
        self.temporal=[]

        self.palabras_reservadas={
            "Tipo": "t_TIPO",
            "Operacion": "t_Operacion",
            "SUMA": "t_SUMA",
            "RESTA": "t_RESTA",
            "MULTIPLICACION": "t_MULTIPLICACION",
            "DIVISION": "t_DIVISION",
            "POTENCIA": "t_POTENCIA",
            "RAIZ": "t_RAIZ",
            "INVERSO": "t_INVERSO",
            "SENO": "t_SENO",
            "COSENO": "t_COSENO",
            "TANGENTE": "t_TANGENTE",
            "MOD": "t_MOD",
            "Numero":"t_Numero",
            "Texto": "t_Texto",
            "Estilo": "t_Estilo",
            "Color": "t_id",
            "Titulo": "t_titulo",
            "Descripcion": "t_Des",
            "Contenido": "t_cont",
            "Tamanio": "t_tam",
            "Funcion": "tFuncion",
            "ESCRIBIR": "tID"
        }

        self.signos={
            "=": "t_ASIGNACION",
            "<": "t_ABIERTO",
            ">": "t_CERRADO",
            ".": "t_PUNTO",
            "/": "t_DIVISION",
            "[": "cAbierto",
            "]": "cCerrado"
        }
        self.colores={
            "ROJO": "#FA6060",
            "NARANJA": "orange",
            "AMARILLO": "yellow",
            "VERDE": "green",
            "AZUL": "#4CB7FC",
            "MORADO": "#914CFC",
            "NEGRO": "black",
            "GRIS": "#CCCCCC"
        }


    
    def Estado0(self,caracter:str):
        if caracter=="<":
            self.columna+=1
            self.token.append(Tokens(caracter,self.signos[caracter],self.linea,self.columna))
            

        elif caracter.isalpha():
            self.columna+=1
            self.tkn+=caracter
            if self.tkn in self.palabras_reservadas:
                if self.palabras_reservadas[self.tkn]=="t_Texto":
                    if  not self.paso:
                        self.estado=2
                        self.paso=True
                    self.token.append(Tokens(self.tkn,self.palabras_reservadas[self.tkn],self.linea,self.columna))
                    self.tkn=""
                    return
                elif self.palabras_reservadas[self.tkn]=="t_Estilo":
                    self.estado=3
                elif self.palabras_reservadas[self.tkn]=="tFuncion":
                    self.estado=4
                self.token.append(Tokens(self.tkn,self.palabras_reservadas[self.tkn],self.linea,self.columna))
                self.tkn=""
        elif caracter.isdigit():
            self.estado=1
            self.columna+=1
            self.tkn+=caracter

        elif caracter=="=":
            self.columna+=1
            self.token.append(Tokens(caracter,self.signos[caracter],self.linea,self.columna))
            
        elif caracter==" ":
            self.columna+=1

        elif caracter=="/":
            self.columna+=1
            self.token.append(Tokens(caracter,self.signos[caracter],self.linea,self.columna))

        elif caracter==">":
            self.columna+=1
            self.paso=False
            self.token.append(Tokens(caracter,self.signos[caracter],self.linea,self.columna))
            
        
        elif caracter=="\n":
            self.linea+=1
            self.columna=1
        elif caracter=="\t":
            self.columna+=4
        
        else:
            self.columna+=1
            self.error.append(Errores(self.linea,self.columna,caracter,"Error"))
            




    def Estado1(self,caracter:str):
        if caracter.isdigit():
            self.columna+=1
            self.tkn+=caracter
            
        elif caracter==".":
            self.columna+=1
            self.tkn+=caracter
            
        elif caracter==" ":
            self.estado=0
            self.token.append(Tokens(self.tkn,"t_Digito",self.linea,self.columna))
            self.columna+=1
            self.tkn=""
        elif caracter=="<":
            self.columna+=1
            self.token.append(Tokens(self.tkn,"t_Digito",self.linea,self.columna-1))
            self.token.append(Tokens(caracter,self.signos[caracter],self.linea,self.columna))
            self.estado=0
            self.tkn=""
        else:
            self.columna+=1
            self.error.append(Errores(self.linea,self.columna,caracter,"Error"))
     
    def Estado2(self,char:str):
        if char=="\n":
            self.linea+=1
            self.columna=1
            self.tkn=""
            self.texto+=char
        elif char=="\t":
            self.columna+=4
        elif char==">":
            self.columna+=1
            self.token.append(Tokens(char,self.signos[char],self.linea,self.columna))

        elif char=="<" or char=="/":
            self.columna+=1

            self.tkn+=char
            if self.tkn=="</":
                self.estado=0
                self.tkn=""
                return
            self.token.append(Tokens(char,self.signos[char],self.linea,self.columna))
             
        else:
            self.texto+=char


    def Estado3(self,char:str):
        if char.isalpha():
            self.columna+=1
            self.tkn+=char
            if self.tkn in self.palabras_reservadas:
                self.token.append(Tokens(self.tkn,self.palabras_reservadas[self.tkn],self.linea,self.columna))  
                self.tkn=""
            elif self.tkn in self.colores:
                self.token.append(Tokens(self.tkn,self.colores[self.tkn],self.linea,self.columna))
                self.colors.append(self.colores[self.tkn])
                
                self.tkn=""
            
        elif char==">" or char=="<":
            self.columna+=1
            self.token.append(Tokens(char,self.signos[char],self.linea,self.columna))
            

        elif char=="=":
            self.columna+=1
            self.token.append(Tokens(char,self.signos[char],self.linea,self.columna))
            
        
        elif char==" ":
            self.tkn=""
            self.columna+=1
        elif char=="\n":
            self.linea+=1
            self.tkn=""
            self.columna=1
        elif char=="\t":
            self.columna+=4
        elif char.isdigit():
            self.columna+=1
            self.tkn+=char
        elif char==".":
            self.tkn+=char
            self.columna+=1
        elif char=="/":
            self.columna+=1
            self.colors.append(self.tkn)
            self.token.append(Tokens(char,self.signos[char],self.linea,self.columna))
            self.tkn=""
        else:
            self.columna+=1
            self.error.append(Errores(self.linea,self.columna,char,"Error"))

    def Estado4(self,char:str):
        if char.isalpha():
            self.columna+=1
            self.tkn+=char
            if self.tkn in self.palabras_reservadas:
                if self.palabras_reservadas[self.tkn]=="tID":
                    self.token.append(Tokens(self.tkn,self.palabras_reservadas[self.tkn],self.linea,self.columna))  
                    self.tkn=""
                elif self.palabras_reservadas[self.tkn]=="t_titulo":
                        
                    self.token.append(Tokens(self.tkn,self.palabras_reservadas[self.tkn],self.linea,self.columna))  
                    self.tkn=""
                elif self.palabras_reservadas[self.tkn]=="t_Des":
                    self.token.append(Tokens(self.tkn,self.palabras_reservadas[self.tkn],self.linea,self.columna))  
                    self.tkn=""
                elif self.palabras_reservadas[self.tkn]=="t_cont":
                    self.token.append(Tokens(self.tkn,self.palabras_reservadas[self.tkn],self.linea,self.columna))  
                    self.tkn=""
                elif self.palabras_reservadas[self.tkn]=="tFuncion":
                    self.estado=0
                    self.token.append(Tokens(self.tkn,self.palabras_reservadas[self.tkn],self.linea,self.columna))  
                    self.tkn=""


            elif self.tkn.capitalize() in self.palabras_reservadas:
                self.temporal.append(self.tkn)
            
        elif char==">" or char=="<":
            self.columna+=1
            if char=="<" and self.cadena[self.contador+1]=="/" and self.cadena[self.contador+2]=="T":
                self.temporal.append(self.tkn)     
            self.token.append(Tokens(char,self.signos[char],self.linea,self.columna))
        elif char=="=":
            self.columna+=1
            self.token.append(Tokens(char,self.signos[char],self.linea,self.columna))
            
        elif char==" ":
            self.columna+=1
        elif char=="\n":
            self.linea+=1
            self.tkn=""
            self.columna=1
        elif char=="\t":
            self.columna+=4
        elif char=="[" or char=="]":
            self.columna+=1
            self.token.append(Tokens(char,self.signos[char],self.linea,self.columna))

        elif char=="/":
            self.columna+=1
            self.token.append(Tokens(char,self.signos[char],self.linea,self.columna))
            self.tkn=""
        else:
            self.columna+=1
            self.error.append(Errores(self.linea,self.columna,char,"Error"))

    def recorrer(self):
        while self.contador< len(self.cadena):
            a=self.cadena[self.contador]
            if self.estado==0:
                self.Estado0(a)
            elif self.estado==1:
                self.Estado1(a)
            elif self.estado==2:
                self.Estado2(a)
            elif self.estado==3:
                self.Estado3(a)
            elif self.estado==4:
                self.Estado4(a)
            self.contador+=1         



    def generarOp(self,lista):
        contador=1
        html="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Operaciones</title>
    <style>
        body {

    font-family: Arial, Helvetica, sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;

}

span {
    
    font-weight: 700;
    font-size: 14pt;
    
}

#text:hover {
    box-shadow:  0px 8px 24px rgba(95, 95, 95, 0.2);
}
"""
        html+="#text {"+"\n"
        html+="    border-radius: 15px;"+"\n"
        html+="    padding-top: 12px;"+"\n"
        html+="    text-align: center;"+"\n"
        html+="    width: 40%;"+"\n"
        html+="    min-height: 10px;"+"\n"
        html+="    background-color: white;"+"\n"
        html+="    box-shadow:  0px 8px 24px rgba(149, 157, 165, 0.2);"+"\n"
        html+="}"+"\n"
        html+="#texto p {"+"\n"
        html+=f"    color: {self.colors[2]};"+"\n"
        html+="}"+"\n"
        html+="#texto {"+"\n"
        html+="    width: 30%;"+"\n"
        html+="    min-height: 20px;"+ "\n"
        html+="    border-radius: 15px;"+"\n"
        html+="    box-shadow:  0px 8px 24px rgba(95, 95, 95, 0.2);"+"\n"
        html+="    margin: 20px;"+"\n"
        html+="    text-align: center;"+ "\n"
        
        html+=f"    font-size: {self.colors[3]}pt;"+"\n"
        html+="}"+ "\n"
        html+="#text p {"+"\n"
        html+=f"    font-size: {self.colors[5]}pt;"+"\n"
        html+=f"    color: {self.colors[4]};"+"\n"
        html+="}"+"\n"
        html+="h1 {"+"\n"
        html+=f"    color: {self.colors[0]};"+"\n"
        html+=f"    font-size: {self.colors[1]}pt;"+"\n"
        html+="}"+"\n"
        html+="    </style>"+"\n"
        html+="</head>"+"\n"
        html+="<body>"+"\n"
        html+=f'<h1>{self.temporal[0]}</h1>'+"\n"

        html+='    <div id="texto">'+"\n"
        html+=f'        <p>{self.texto}</p>'+"\n"
        html+="    </div>"+"\n"
        html+='    <div id="text">'+"\n"

        for elem in lista:
            html+=f"        <span>Operacion {contador}</span>"+"\n"
            html+=f"        <p>{elem}</p>"+"\n"
            contador+=1
        html+="    </div>"+"\n"
        html+="</body>"+"\n"
        html+="</html>"
        file=open("./Operaciones.html","w+")
        file.write(html)
        file.close()
        webbrowser.open_new_tab("Operaciones.html")

    def generarTkns(self):
        contador=1
        html="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tabla de tokens</title>
    <style>
        body {
            background-color: #C8EEFF;
            font-family: Arial, Helvetica, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
    }

        #contenedor {
            display: flex;
            width: 50%;
            background-color: white;
            padding: 0px,10px,10px;
            justify-content: center;
            box-shadow: 0px 7px 29px 0px gray;
    }

        table {
            width: 100%;
            text-align: center;
        }

        th,td {
            padding: 8px;
            height: 20px;
        }

        thead {
            background-color: aquamarine;
        }
    </style>
</head>
<body>
    <h1>Tabla de Tokens</h1>
    <div id="contenedor">
    <table>
        <thead>
            <tr>
                <th>No</th>
                <th>Token</th>
                <th>Valor</th>
                <th>Linea</th>
                <th>Columna</th>
            </tr>
        </thead>
"""
        for token in self.token:
            html+='            <tr>\n'
            html+=f'               <td>{contador}</td>\n'
            html+=f'               <td>{token.tkn}</td>\n'
            html+=f'               <td>{token.valor}</td>\n'
            html+=f'               <td>{token.linea}</td>\n'
            html+=f'               <td>{token.columna}</td>\n'
            html+='            </tr>\n'
            contador+=1
        html+='        </table>\n'
        html+='    </div>\n'
        html+='</body>\n'
        html+='</html>\n'
        file=open("Tokens.html","w+")
        file.write(html)
        file.close()
        webbrowser.open_new_tab("Tokens.html")

    def errores(self):
        contador=1
        html="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Errores</title>
    <style>
        body {
            background-color: #C8EEFF;
            font-family: Arial, Helvetica, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
    }

        #contenedor {
            display: flex;
            width: 50%;
            background-color: white;
            padding: 0px,10px,10px;
            justify-content: center;
            box-shadow: 0px 7px 29px 0px gray;
    }

        table {
            width: 100%;
            text-align: center;
        }

        th,td {
            padding: 8px;
            height: 20px;
        }

        thead {
            background-color: aquamarine;
        }
    </style>
</head>
<body>
    <h1>Tabla de errores</h1>
    <div id="contenedor">
    <table>
        <thead>
            <tr>
                <th>No</th>
                <th>Lexema</th>
                <th>Fila</th>
                <th>Columna</th>
                <th>Tipo</th>
            </tr>
        </thead>
"""

        for er in self.error:
            html+='            <tr>\n'
            html+=f'               <td>{contador}</td>\n'
            html+=f'               <td>{er.lexema}</td>\n'
            html+=f'               <td>{er.fila}</td>\n'
            html+=f'               <td>{er.columna}</td>\n'
            html+=f'               <td>{er.tipo}</td>\n'
            html+='            </tr>\n'
            contador+=1
        html+='        </table>\n'
        html+='    </div>\n'
        html+='</body>\n'
        html+='</html>\n'
        file=open("./Errores.html","w+")
        file.write(html)
        file.close()
        webbrowser.open_new_tab("Errores.html")