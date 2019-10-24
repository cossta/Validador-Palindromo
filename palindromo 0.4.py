""" Importando Tkinter """
from tkinter import *
from tkinter import messagebox 
from tkinter import filedialog
import time
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
ultimoPilaY = 295

"""Colores utilizados:
    
    1. Hexadecimal: 2a1a5e  <::> RGB = #422694
    2. Hexadecimal: f45905  <::>
    3. Hexadecimal: fb9224  <::> rgb(251, 146, 36)
    4. Hexadecimal: fbe555  <::>
    5. Hexadecimal: dfddc7  <::>
    6. Hexadecimal: 16ed48 (Verde)
    7. Hexadecimal: cb3234 (Rojo)

    El orden de los colores va desde el más oscuro hasta el más claro"""

root = Tk()
root.title("Palindromo Con Pila PRO")
root.resizable(False,False)
root.config(background='#fb9224')
miFrame = Frame(root, width=720, height=500)
miFrame.pack()

"""----------------- Todos los Canvas ----------------------------"""
Estado1 = Canvas(root, width=120, height=130)
Estado2 = Canvas(root, width=120, height=130)
Estado3 = Canvas(root, width=120, height=120)
Flecha1 = Canvas(root, width=90, height=10)
FlechaInicial = Canvas(root, width=60, height=10)
Flecha2 = Canvas(root, width=90, height=10)
PilaLineas = Canvas(root,bg="#2a1a5e", width=40, height=290)
A_Numeral_p1 = Canvas(root,width=80,height=25)
B_Numeral_p1 = Canvas(root, width=80,height=25)
rec = Canvas(root, width=30, height=30)
AA = Canvas(root, width=80,height=25)
AB = Canvas(root,width=80,height=25)
BA = Canvas(root, width=80,height=25)
BB = Canvas(root, width=80,height=25)
C_Numeral = Canvas(root, width=80,height=25)
C_B = Canvas(root, width=80,height=25)
C_A = Canvas(root, width=80,height=25)
B_LAMBDA = Canvas(root, width=80,height=25)
A_LAMBDA = Canvas(root, width=80,height=25)
LAMBDA_Numeral = Canvas(root, width=80,height=25)
"""----------------- Fin de Todos los Canvas ----------------------"""

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

def VerificarPalindromo(tiempo):
    ultimoPilaY = 295
    all_canvas()
    FlechaInicial.place(x=11,y=255)
    FlechaInicial.create_line(0,7,70,7, width=3.0, fill="#2a1a5e")
    FlechaInicial.create_line(50,2,60,7, fill="#2a1a5e", width=3.0)
    FlechaInicial.create_line(60,7,50,12, fill="#2a1a5e", width=3.0)
    FlechaInicial.update()
    estadosCanvas()
    pintarElementosPila(ultimoPilaY, "#")
    ultimoPilaY -= 25
 
    pilaPalindromo = Palindro.get()
    Palindromo=Pila()
    estado = 1
    color=1
    entrada = 1
    for i in range(0,len(pilaPalindromo)):
        all_canvas()
        estadosCanvas()
        transicion=pilaPalindromo[i]
        print(transicion)
        topePila=Palindromo.desapilar()
        if estado == 1:
            Estado1.create_oval(25,35,100,110, fill="#2a1a5e")
            Estado1.create_text(63,75,text="P", fill="#f45905", font=("",24))
            Estado1.create_line(32,10,32,50, fill="#f45905", width=3.0)
            Estado1.create_line(32,10,93,10, fill="#f45905", width=3.0)
            Estado1.create_line(93,10,93,50, fill="#f45905", width=3.0)
            Estado1.create_line(88,37,93,50, fill="#f45905", width=3.0)
            Estado1.create_line(98,37,93,50, fill="#f45905", width=3.0)
            if transicion=="a" and topePila=="#":
                Palindromo.apilar("#")
                Palindromo.apilar("a")
                A_Numeral_p1.place(x=73,y=160)
                A_Numeral_p1.create_text(40,15,text="a, #/#a", fill="#f45905",font=("",16))
                A_Numeral_p1.update()
                pintarElementosPila(ultimoPilaY, "a")
                ultimoPilaY -= 25
            elif transicion=="b" and topePila=="#":
                Palindromo.apilar("#")
                Palindromo.apilar("b")
                B_Numeral_p1.place(x=73,y=139)
                B_Numeral_p1.create_text(40,15,text="b, #/#b", fill="#f45905",font=("",16))
                B_Numeral_p1.update()
                pintarElementosPila(ultimoPilaY, "b")
                ultimoPilaY -= 25
            elif transicion=="a" and topePila=="a":
                Palindromo.apilar("a")
                Palindromo.apilar("a")
                AA.place(x=73,y=118)
                AA.create_text(40,15,text="a, a/aa", fill="#f45905",font=("",16))
                AA.update()
                pintarElementosPila(ultimoPilaY, "a")
                ultimoPilaY -= 25
            elif transicion=="b" and topePila=="a":
                Palindromo.apilar("a")
                Palindromo.apilar("b")
                AB.place(x=73,y=97)
                AB.create_text(40,15,text="b, a/ab", fill="#f45905",font=("",16))
                AB.update()
                pintarElementosPila(ultimoPilaY, "b")
                ultimoPilaY -= 25
            elif transicion=="a" and topePila=="b":
                Palindromo.apilar("b")
                Palindromo.apilar("a")
                BA.place(x=73,y=76)
                BA.create_text(40,15,text="a, b/ba", fill="#f45905",font=("",16))
                BA.update()
                pintarElementosPila(ultimoPilaY, "a")
                ultimoPilaY -= 25
            elif transicion=="b" and topePila=="b":
                Palindromo.apilar("b")
                Palindromo.apilar("b")
                BB.place(x=73,y=55)
                BB.create_text(40,15,text="b, b/bb", fill="#f45905",font=("",16))
                BB.update()
                pintarElementosPila(ultimoPilaY, "b")
                ultimoPilaY -= 25
            elif transicion=="c" and topePila=="#":
                Flecha1.place(x=151,y=255)
                Flecha1.create_line(0,7,100,7, width=3.0, fill="#f45905")
                Flecha1.create_line(80,2,90,7, fill="#f45905", width=3.0)
                Flecha1.create_line(90,7,80,12, fill="#f45905", width=3.0)
                Flecha1.update()
                Palindromo.apilar("#")
                C_Numeral.place(x=158,y=220)
                C_Numeral.create_text(40,15,text="c, #/#", fill="#f45905",font=("",16))
                C_Numeral.update()
                estado = 2
            elif transicion=="c" and topePila=="b":
                Flecha1.place(x=151,y=255)
                Flecha1.create_line(0,7,100,7, width=3.0, fill="#f45905")
                Flecha1.create_line(80,2,90,7, fill="#f45905", width=3.0)
                Flecha1.create_line(90,7,80,12, fill="#f45905", width=3.0)
                Flecha1.update()
                Palindromo.apilar("b")
                C_B.place(x=158,y=199)
                C_B.create_text(40,15,text="c, b/b", fill="#f45905",font=("",16))
                C_B.update()
                estado = 2
            elif transicion=="c" and topePila=="a":
                Estado1.place(x=50,y=190)
                Estado1.create_line(32,10,32,50, fill="#2a1a5e", width=3.0)
                Estado1.create_line(32,10,93,10, fill="#2a1a5e", width=3.0)
                Estado1.create_line(93,10,93,50, fill="#2a1a5e", width=3.0)
                Estado1.create_line(88,37,93,50, fill="#2a1a5e", width=3.0)
                Estado1.create_line(98,37,93,50, fill="#2a1a5e", width=3.0)
                Estado1.update()
                Flecha1.place(x=151,y=255)
                Flecha1.create_line(0,7,100,7, width=3.0, fill="#f45905")
                Flecha1.create_line(80,2,90,7, fill="#f45905", width=3.0)
                Flecha1.create_line(90,7,80,12, fill="#f45905", width=3.0)
                Flecha1.update()
                Palindromo.apilar("a")
                C_A.place(x=158,y=178)
                C_A.create_text(40,15,text="c, a/a", fill="#f45905",font=("",16))
                C_A.update()
                estado = 2
            else:
                Palindromo.apilar(topePila)
                Estado3.create_oval(20,20,100,100, fill="#cb3234")
                Estado3.create_oval(25,25,95,95, fill="#2a1a5e")
                Estado3.create_text(60,62,text="R", fill="#cb3234", font=("",24))
                Estado3.update()

                speaker.Speak("La Expresión No Es Válida. El Color Rojo Lo Índica")
                return False
        elif estado == 2:
            if color==1:
                estadosCanvas()
                color = 2
            Estado2.place(x=220,y=190)
            Estado2.create_oval(25,35,100,110, fill="#2a1a5e")
            Estado2.create_text(63,75,text="Q", fill="#f45905", font=("",24))
            Estado2.create_line(32,10,32,50, fill="#f45905", width=3.0)
            Estado2.create_line(32,10,93,10, fill="#f45905", width=3.0)
            Estado2.create_line(93,10,93,50, fill="#f45905", width=3.0)
            Estado2.create_line(88,37,93,50, fill="#f45905", width=3.0)
            Estado2.create_line(98,37,93,50, fill="#f45905", width=3.0)
            Estado2.update()
            if transicion=="a" and topePila=="a":
                if entrada==1:
                    ultimoPilaY -= 25
                    entrada=2
                # pass               
                # ultimoPilaY += 25
                quitarElementosPila(ultimoPilaY, "a")
                ultimoPilaY += 25
                A_LAMBDA.place(x=243,y=139)
                A_LAMBDA.create_text(40,15,text="a, a/y", fill="#f45905",font=("",16))
                A_LAMBDA.update()
            elif transicion=="b" and topePila=="b":
                # pass              
                # ultimoPilaY += 25
                if entrada==1:
                    ultimoPilaY -= 25
                    entrada=2
                quitarElementosPila(ultimoPilaY, "b")
                ultimoPilaY += 25
                B_LAMBDA.place(x=243,y=160)
                B_LAMBDA.create_text(40,15,text="b, b/y", fill="#f45905",font=("",16))
                B_LAMBDA.update()
            else:
                Palindromo.apilar(topePila)
                Estado3.create_oval(20,20,100,100, fill="#cb3234")
                Estado3.create_oval(25,25,95,95, fill="#2a1a5e")
                Estado3.create_text(60,62,text="R", fill="#cb3234", font=("",24))
                Estado3.update()

                speaker.Speak("La Expresión No Es Válida. El Color Rojo Lo Índica")
                return False
        time.sleep(tiempo)
    topePila=Palindromo.desapilar()
    if topePila=="#":
            Palindromo.apilar("#")
            estado = 3
    if estado == 3:
        estadosCanvas()
        all_canvas()
        Estado3.create_oval(20,20,100,100, fill="#16ed48")
        Estado3.create_oval(25,25,95,95, fill="#2a1a5e")
        Estado3.create_text(60,62,text="R", fill="#16ed48", font=("",24))
        Estado3.update()
        
        speaker.Speak("La Expresión Es Válida. El Color Verde Lo Índica")
        return True
    else:
        Estado3.create_oval(20,20,100,100, fill="#cb3234")
        Estado3.create_oval(25,25,95,95, fill="#2a1a5e")
        Estado3.create_text(60,62,text="R", fill="#cb3234", font=("",24))
        Estado3.update()

        speaker.Speak("La Expresión No Es Válida. El Color Rojo Lo Índica")
        return False
            
"""--------------- Fin de la Clase del Automata -------------------------------"""
LabelPalindromo = Label(miFrame, text="Palindromo Con Pila PRO", font=("Full Pack 2025",12))
LabelPalindromo.config(justify="center")
LabelPalindromo.place(bordermode=OUTSIDE, x=200, y=10)

Palindro = StringVar()

TextoPalindromo = Entry(miFrame, width=69, textvariable=Palindro)
TextoPalindromo.place(bordermode=OUTSIDE, x=80, y=330)
TextoPalindromo.config(bg="#dfddc7")
# TextoPalindromo


ButtonPalindromoLento = Button(miFrame, text="Verificar Lento", command=lambda:VerificarPalindromo(1))
ButtonPalindromoLento.place(bordermode=OUTSIDE, x=130, y=360)
ButtonPalindromoLento.config(bg="#fbe555")

ButtonPalindromoRapido = Button(miFrame, text="Verificar Rapido", command=lambda:VerificarPalindromo(0.3))
ButtonPalindromoRapido.place(bordermode=OUTSIDE, x=240, y=360)
ButtonPalindromoRapido.config(bg="#fbe555")

def estadosCanvas():
    Estado1.place(x=50,y=190)
    Estado1.create_oval(25,35,100,110, fill="#2a1a5e")
    Estado1.create_text(63,75,text="P", fill="#ffffff", font=("",24))
    Estado1.create_line(32,10,32,50, fill="#2a1a5e", width=3.0)
    Estado1.create_line(32,10,93,10, fill="#2a1a5e", width=3.0)
    Estado1.create_line(93,10,93,50, fill="#2a1a5e", width=3.0)
    Estado1.create_line(88,37,93,50, fill="#2a1a5e", width=3.0)
    Estado1.create_line(98,37,93,50, fill="#2a1a5e", width=3.0)
    Estado1.update()
    
    Estado2.place(x=220,y=190)
    Estado2.create_oval(25,35,100,110, fill="#2a1a5e")
    Estado2.create_text(63,75,text="Q", fill="#ffffff", font=("",24))
    Estado2.create_line(32,10,32,50, fill="#2a1a5e", width=3.0)
    Estado2.create_line(32,10,93,10, fill="#2a1a5e", width=3.0)
    Estado2.create_line(93,10,93,50, fill="#2a1a5e", width=3.0)
    Estado2.create_line(88,37,93,50, fill="#2a1a5e", width=3.0)
    Estado2.create_line(98,37,93,50, fill="#2a1a5e", width=3.0)
    Estado2.update()

    Estado3.place(x=395,y=200)
    Estado3.create_oval(20,20,100,100, fill="#dfddc7")
    Estado3.create_oval(25,25,95,95, fill="#2a1a5e")
    Estado3.create_text(60,62,text="R", fill="#ffffff", font=("",24))
    Estado3.update()

def all_canvas():

    FlechaInicial.place(x=11,y=255)
    FlechaInicial.create_line(0,7,70,7, width=3.0, fill="#2a1a5e")
    FlechaInicial.create_line(50,2,60,7, fill="#2a1a5e", width=3.0)
    FlechaInicial.create_line(60,7,50,12, fill="#2a1a5e", width=3.0)
    FlechaInicial.update()

    Flecha1.place(x=151,y=255)
    Flecha1.create_line(0,7,100,7, width=3.0, fill="#2a1a5e")
    Flecha1.create_line(80,2,90,7, fill="#2a1a5e", width=3.0)
    Flecha1.create_line(90,7,80,12, fill="#2a1a5e", width=3.0)
    Flecha1.update()
    
    Flecha2.place(x=321,y=255)
    Flecha2.create_line(0,7,100,7, width=3.0, fill="#2a1a5e")
    Flecha2.create_line(80,2,90,7, fill="#2a1a5e", width=3.0)
    Flecha2.create_line(90,7,80,12, fill="#2a1a5e", width=3.0)
    Flecha2.update()
    
    A_Numeral_p1.place(x=73,y=160)
    A_Numeral_p1.create_text(40,15,text="a, #/#a", fill="#2a1a5e",font=("",16))
    A_Numeral_p1.update()
    
    B_Numeral_p1.place(x=73,y=139)
    B_Numeral_p1.create_text(40,15,text="b, #/#b", fill="#2a1a5e",font=("",16))
    B_Numeral_p1.update()
    
    AA.place(x=73,y=118)
    AA.create_text(40,15,text="a, a/aa", fill="#2a1a5e",font=("",16))
    AA.update()
    
    AB.place(x=73,y=97)
    AB.create_text(40,15,text="b, a/ab", fill="#2a1a5e",font=("",16))
    AB.update()
    
    BA.place(x=73,y=76)
    BA.create_text(40,15,text="a, b/ba", fill="#2a1a5e",font=("",16))
    BA.update()
    
    BB.place(x=73,y=55)
    BB.create_text(40,15,text="b, b/bb", fill="#2a1a5e",font=("",16))
    BB.update()
    
    C_Numeral.place(x=158,y=220)
    C_Numeral.create_text(40,15,text="c, #/#", fill="#2a1a5e",font=("",16))
    C_Numeral.update()
    
    C_B.place(x=158,y=199)
    C_B.create_text(40,15,text="c, b/b", fill="#2a1a5e",font=("",16))
    C_B.update()

    C_A.place(x=158,y=178)
    C_A.create_text(40,15,text="c, a/a", fill="#2a1a5e",font=("",16))
    C_A.update()
    
    B_LAMBDA.place(x=243,y=160)
    B_LAMBDA.create_text(40,15,text="b, b/y", fill="#2a1a5e",font=("",16))
    B_LAMBDA.update()
    
    A_LAMBDA.place(x=243,y=139)
    A_LAMBDA.create_text(40,15,text="a, a/y", fill="#2a1a5e",font=("",16))
    A_LAMBDA.update()
    
    LAMBDA_Numeral.place(x=323,y=220)
    LAMBDA_Numeral.create_text(40,15,text="y, #/#", fill="#2a1a5e",font=("",16))
    LAMBDA_Numeral.update()

def pintarElementosPila(ultimoPilaY, textoApilar):
    ultimoPilaY -= 25

    PilaLineas.place(x=600,y=55)
    PilaLineas.create_text(22, ultimoPilaY, text=textoApilar, fill="#ffffff", font=("",16))
def quitarElementosPila(ultimoPilaY, textoApilar):
    ultimoPilaY += 25

    PilaLineas.place(x=600,y=55)
    PilaLineas.create_text(22, ultimoPilaY, text=textoApilar, fill="#2a1a5e", font=("",16))
    PilaLineas.create_text(22, ultimoPilaY, text="8", fill="#2a1a5e", font=("",16))
    PilaLineas.create_text(22, ultimoPilaY, text="#", fill="#2a1a5e", font=("",16))
    PilaLineas.create_text(22, ultimoPilaY, text="9", fill="#2a1a5e", font=("",16))
    PilaLineas.create_text(22, ultimoPilaY, text="b", fill="#2a1a5e", font=("",16))
    PilaLineas.create_text(22, ultimoPilaY, text="a", fill="#2a1a5e", font=("",16))
    PilaLineas.create_text(22, ultimoPilaY, text="b", fill="#2a1a5e", font=("",16))
    PilaLineas.create_text(22, ultimoPilaY, text="a", fill="#2a1a5e", font=("",16))

pilaYGlobal = 295
pintarElementosPila(pilaYGlobal, "#")
all_canvas()
estadosCanvas()
root.mainloop()