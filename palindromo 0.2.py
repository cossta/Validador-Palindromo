""" Importando Tkinter """
from tkinter import *
from tkinter import messagebox 
from tkinter import filedialog


"""Colores utilizados:
    
    1. 2a1a5e
    2. f45905
    3. fb9224
    4. fbe555
    5. dfddc7

    El orden de los colores va desde el más oscuro hasta el más claro"""

root = Tk()
miFrame = Frame(root)
root.title("Calculadora")
root.geometry("700x500+100+100")
root.title("Palindromo Con Pila PRO")
root.config(background='#fb9224')
miFrame.pack()


"""--------------- Inicio del Menú -------------------------------"""

def infoAdicional():
    messagebox.showinfo("Informacion de Aplicacion", 
        "Si necesitas ayuda, debes ir a un Psicologo o a un Psiquiatra todo depende de ti y tus necesidades")
def avisoLicencia():
    messagebox.showwarning("Tacaño", "No compraste la licencia, la pirateaste")
def salirDeLaAplicacion():
    valorSalir=messagebox.askquestion("¿Desea salir de la Aplicación?")
    if valorSalir=="yes":
        root.destroy()

barraMenu = Menu(root)
root.config(menu=barraMenu, width=350, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir archivo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como...")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir", command=lambda:salirDeLaAplicacion())

archivoEdicion=Menu(barraMenu,  tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu)

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Ayuda extra...", command=lambda:infoAdicional())
archivoAyuda.add_command(label="Licencia", command=lambda:avisoLicencia())
archivoAyuda.add_command(label="Acerca de...")

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

"""--------------- Fin del Menú -------------------------------"""
"""--------------- Inicio de Clase de la Pila -------------------------------"""
class Pila(object):
    def __init__(self):
        self.items=["#"]
    def apilar(self,dato):
        self.items.append(dato)
    def desapilar(self):
        return self.items.pop()
"""--------------- Fin de Clase de la Pila -------------------------------"""
"""--------------- Inicio de la Clase del Automata -------------------------------"""

def VerificarPalindromo():
    pilaPalindromo = Palindro.get()
    Palindromo=Pila()
    estado = 1
    for i in range(0,len(pilaPalindromo)):
        transicion=pilaPalindromo[i]
        print(transicion)
        topePila=Palindromo.desapilar()
        if estado == 1:
            if transicion=="a" and topePila=="#":
                Palindromo.apilar("#")
                Palindromo.apilar("a")
            elif transicion=="b" and topePila=="#":
                Palindromo.apilar("#")
                Palindromo.apilar("b")
            elif transicion=="a" and topePila=="a":
                Palindromo.apilar("a")
                Palindromo.apilar("a")
            elif transicion=="b" and topePila=="a":
                Palindromo.apilar("a")
                Palindromo.apilar("b")
            elif transicion=="a" and topePila=="b":
                Palindromo.apilar("b")
                Palindromo.apilar("a")
            elif transicion=="b" and topePila=="b":
                Palindromo.apilar("b")
                Palindromo.apilar("b")
            elif transicion=="c" and topePila=="#":
                Palindromo.apilar("#")
                estado = 2
            elif transicion=="c" and topePila=="b":
                Palindromo.apilar("b")
                estado = 2
            elif transicion=="c" and topePila=="a":
                Palindromo.apilar("a")
                estado = 2
            else:
                print("No cumple 2")
                Palindromo.apilar(topePila)
                return False
        elif estado == 2:
            if transicion=="a" and topePila=="a":
                # pass
                print("Soy a")
            elif transicion=="b" and topePila=="b":
                # pass
                print("Soy b")
            else:
                print("No cumple 3")
                Palindromo.apilar(topePila)
                return False
    topePila=Palindromo.desapilar()
    if topePila=="#":
            print("Soy #")
            Palindromo.apilar("#")
            estado = 3
    if estado == 3:
        print("Si cumple")
        return True
    else:
        print("No cumple 4")
        return False
            
                




"""--------------- Fin de la Clase del Automata -------------------------------"""
LabelPalindromo = Label(miFrame, text="Palindromo Con Pila PRO", font=("Full Pack 2025",12))
LabelPalindromo.config(bg="#fb9224", justify="center")
LabelPalindromo.grid(row=1, column=0, columnspan=2,pady=30)
Palindro = StringVar()
TextoPalindromo = Entry(miFrame, width=50, textvariable=Palindro)
TextoPalindromo.grid(row=3, column=0, columnspan=2, pady=30)
TextoPalindromo.config(bg="#dfddc7")
miFrame.config(bg="#fb9224")
ButtonPalindromoLento = Button(miFrame, text="Verificar Lento", command=VerificarPalindromo)
ButtonPalindromoLento.grid(row=4, column=0)
ButtonPalindromoLento.config(bg="#fbe555")
ButtonPalindromoRapido = Button(miFrame, text="Verificar Rapido")
ButtonPalindromoRapido.grid(row=4, column=1)
ButtonPalindromoRapido.config(bg="#fbe555")




root.mainloop()