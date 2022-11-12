from tkinter import *
import webbrowser
from tkinter import filedialog
from tkinter import messagebox
from archivo import Analizar
from Extraer import Obtener
class Interfaz:
    analizar=False
    def __init__(self) -> None:
        self.vent=Tk()
    
    def ventana(self):
        menu=Menu(self.vent)
        self.vent.config(menu=menu)
        self.vent.geometry("930x600")
        self.txt1=Text(self.vent,height=24,width=90)
        self.txt1.place(x=20,y=40)
        btn1=Button(self.vent,text="Analizar",command=self.analizarA)
        btn1.place(x=20,y=450,width=140,height=40)
        btn2=Button(self.vent,text="Generar operaciones",command=self.ejecutarOp)
        btn2.place(x=180,y=450,width=140,height=40)
        btn3=Button(self.vent,text="Archivo de tokens",command=self.tokens)
        btn3.place(x=760,y=50,width=130,height=40)
        btn4=Button(self.vent,text="Archivo de errores",command=self.errores)
        btn4.place(x=760,y=120,width=130,height=40)
        btn5=Button(self.vent,text="Limpiar",command=self.limpiar)
        btn5.place(x=760,y=190,width=130,height=40)
        File=Menu(menu,tearoff=0)
        Ayuda=Menu(menu,tearoff=0)

        menu.add_cascade(label= "Archivo", menu=File)
        menu.add_cascade(label= "Ayuda",menu=Ayuda)
        File.add_command(label="Abrir",command = self.abrir)
        File.add_command(label="Guardar",command=self.guardar)
        File.add_command(label="Guardar como",command=self.guardarcomo)
        File.add_separator()
        File.add_command(label="Salir",command=self.vent.quit)
        Ayuda.add_command(label="Manual de usuario",command=self.manualUsuario)
        Ayuda.add_command(label="Manual técnico",command=self.manualtec)
        Ayuda.add_command(label="Ayuda")

        self.vent.mainloop()
    def manualUsuario(self):
        webbrowser.open_new_tab("C:/Users/raulc/Desktop/Proyecto 1 LFP/Archivos/Manual_de_usuario.pdf")
    def manualtec(self):
         webbrowser.open_new_tab("C:/Users/raulc/Desktop/Proyecto 1 LFP/Archivos/Manual técnico.pdf")
    def abrir(self):
        file=filedialog.askopenfile()
        if file:
            self.ruta=file.name
            try:
                archivo=open(self.ruta,"r")
                lectura=archivo.read()
                messagebox.showinfo(title="Exito",message="Archivo cargado con éxito")
                self.txt1.delete("1.0","end")
                self.txt1.insert(INSERT,lectura)
                archivo.close()
            except:
                messagebox.showerror(title="Error",message="Error al leer el archivo")

    def analizarA(self):
        try:
            self.cadena=self.txt1.get("1.0","end")
            self.cadena=self.cadena.rstrip().replace("    ","\t")
            if "Tipo" not in self.cadena or "Numero" not in self.cadena or "Estilo" not in self.cadena:
                raise 
            self.obj=Analizar(self.cadena)
            self.obj.recorrer() #Metodo recorrer del analizador
            messagebox.showinfo(title="Exito",message="Archivo analizado con éxito")
            self.analizar=True
        except:
            messagebox.showerror(title="Error",message="Error al analizar el archivo")
            self.txt1.delete("1.0","end")

    def ejecutarOp(self):
        if self.analizar:
            ob1=Obtener(self.cadena)
            arreglo=ob1.datos()
            self.obj.generarOp(arreglo)
        else:
            messagebox.showinfo(title="Error",message="Debe analizar un archivo")
    def tokens(self):
        if self.analizar:
            self.obj.generarTkns()
        else:
            messagebox.showinfo(title="Error",message="Debe analizar un archivo")
    def errores(self):
        if self.analizar:
            self.obj.errores()
        else:
            messagebox.showinfo(title="Error",message="Debe analizar un archivo")
    def limpiar(self):
        self.analizar=False
        self.txt1.delete("1.0","end")
        self.ruta=None

    def guardar(self):
        self.cadena=self.txt1.get("1.0","end")
        try:
            file=open(self.ruta,"w")
            file.write(self.cadena)
            file.close()
            messagebox.showinfo(title="Archivo guardado",message="Archivo guardado")
        except:
            messagebox.showerror("Error",message="Error al guardar")
    def guardarcomo(self):
        self.cadena=self.txt1.get("1.0","end")
        archivos = filedialog.asksaveasfilename(filetypes=[("Archivos lfp",".txt")],defaultextension=".txt")
        if archivos:
            ar=open(archivos,"w")
            ar.write(self.cadena)
            ar.close()


ob1=Interfaz()
ob1.ventana()
