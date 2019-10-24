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


"""----------------- Fin de Todos los Canvas ----------------------"""
"""--------------- Inicio de Clase de la Pila -------------------------------"""
class todosLosCanvas(object):
    def __init__(self):
        self.Estado1 = Canvas(root, width=120, height=130)
        self.Estado2 = Canvas(root, width=120, height=130)
        self.Estado3 = Canvas(root, width=120, height=120)
        self.Flecha1 = Canvas(root, width=90, height=10)
        self.FlechaInicial = Canvas(root, width=60, height=10)
        self.Flecha2 = Canvas(root, width=90, height=10)
        self.PilaLineas = Canvas(root,bg="#2a1a5e", width=40, height=290)
        self.A_Numeral_p1 = Canvas(root,width=80,height=25)
        self.B_Numeral_p1 = Canvas(root, width=80,height=25)
        self.rec = Canvas(root, width=30, height=30)
        self.AA = Canvas(root, width=80,height=25)
        self.AB = Canvas(root,width=80,height=25)
        self.BA = Canvas(root, width=80,height=25)
        self.BB = Canvas(root, width=80,height=25)
        self.C_Numeral = Canvas(root, width=80,height=25)
        self.C_B = Canvas(root, width=80,height=25)
        self.C_A = Canvas(root, width=80,height=25)
        self.B_LAMBDA = Canvas(root, width=80,height=25)
        self.A_LAMBDA = Canvas(root, width=80,height=25)
        self.LAMBDA_Numeral = Canvas(root, width=80,height=25)
    def pintarNormalEstado1(self):
        self.Estado1.place(x=50,y=190)
        self.Estado1.create_oval(25,35,100,110, fill="#2a1a5e")
        self.Estado1.create_text(63,75,text="P", fill="#ffffff", font=("",24))
        self.Estado1.create_line(32,10,32,50, fill="#2a1a5e", width=3.0)
        self.Estado1.create_line(32,10,93,10, fill="#2a1a5e", width=3.0)
        self.Estado1.create_line(93,10,93,50, fill="#2a1a5e", width=3.0)
        self.Estado1.create_line(88,37,93,50, fill="#2a1a5e", width=3.0)
        self.Estado1.create_line(98,37,93,50, fill="#2a1a5e", width=3.0)
        self.Estado1.update()
    def pintarIluminadoEstado1(self):
        self.Estado1.place(x=50,y=190)
        self.Estado1.create_oval(25,35,100,110, fill="#2a1a5e")
        self.Estado1.create_text(63,75,text="P", fill="#f45905", font=("",24))
        self.Estado1.create_line(32,10,32,50, fill="#f45905", width=3.0)
        self.Estado1.create_line(32,10,93,10, fill="#f45905", width=3.0)
        self.Estado1.create_line(93,10,93,50, fill="#f45905", width=3.0)
        self.Estado1.create_line(88,37,93,50, fill="#f45905", width=3.0)
        self.Estado1.create_line(98,37,93,50, fill="#f45905", width=3.0)
        self.Estado1.update()
    def pintarNormalFlechaEstado1(self):
        self.Estado1.place(x=50,y=190)
        self.Estado1.create_line(32,10,32,50, fill="#2a1a5e", width=3.0)
        self.Estado1.create_line(32,10,93,10, fill="#2a1a5e", width=3.0)
        self.Estado1.create_line(93,10,93,50, fill="#2a1a5e", width=3.0)
        self.Estado1.create_line(88,37,93,50, fill="#2a1a5e", width=3.0)
        self.Estado1.create_line(98,37,93,50, fill="#2a1a5e", width=3.0)
        self.Estado1.update()
    def pintarNormalEstado2(self):
        self.Estado2.place(x=220,y=190)
        self.Estado2.create_oval(25,35,100,110, fill="#2a1a5e")
        self.Estado2.create_text(63,75,text="Q", fill="#ffffff", font=("",24))
        self.Estado2.create_line(32,10,32,50, fill="#2a1a5e", width=3.0)
        self.Estado2.create_line(32,10,93,10, fill="#2a1a5e", width=3.0)
        self.Estado2.create_line(93,10,93,50, fill="#2a1a5e", width=3.0)
        self.Estado2.create_line(88,37,93,50, fill="#2a1a5e", width=3.0)
        self.Estado2.create_line(98,37,93,50, fill="#2a1a5e", width=3.0)
        self.Estado2.update()
    def pintarIluminadoEstado2(self):
        self.Estado2.place(x=220,y=190)
        self.Estado2.create_oval(25,35,100,110, fill="#2a1a5e")
        self.Estado2.create_text(63,75,text="Q", fill="#f45905", font=("",24))
        self.Estado2.create_line(32,10,32,50, fill="#f45905", width=3.0)
        self.Estado2.create_line(32,10,93,10, fill="#f45905", width=3.0)
        self.Estado2.create_line(93,10,93,50, fill="#f45905", width=3.0)
        self.Estado2.create_line(88,37,93,50, fill="#f45905", width=3.0)
        self.Estado2.create_line(98,37,93,50, fill="#f45905", width=3.0)
        self.Estado2.update()
    def pintarNormalEstado3(self):
        self.Estado3.place(x=395,y=200)
        self.Estado3.create_oval(20,20,100,100, fill="#dfddc7")
        self.Estado3.create_oval(25,25,95,95, fill="#2a1a5e")
        self.Estado3.create_text(60,62,text="R", fill="#ffffff", font=("",24))
        self.Estado3.update()
    def pintarIluminadoVerdeEstado3(self):
        self.Estado3.create_oval(20,20,100,100, fill="#16ed48")
        self.Estado3.create_oval(25,25,95,95, fill="#2a1a5e")
        self.Estado3.create_text(60,62,text="R", fill="#16ed48", font=("",24))
        self.Estado3.update()
    def pintarIluminadoRojoEstado3(self):
        self.Estado3.create_oval(20,20,100,100, fill="#cb3234")
        self.Estado3.create_oval(25,25,95,95, fill="#2a1a5e")
        self.Estado3.create_text(60,62,text="R", fill="#cb3234", font=("",24))
        self.Estado3.update()
    def pintarNormalFlechaInicial(self):
        self.FlechaInicial.place(x=11,y=255)
        self.FlechaInicial.create_line(0,7,70,7, width=3.0, fill="#2a1a5e")
        self.FlechaInicial.create_line(50,2,60,7, fill="#2a1a5e", width=3.0)
        self.FlechaInicial.create_line(60,7,50,12, fill="#2a1a5e", width=3.0)
        self.FlechaInicial.update()
    def pintarIluminadoFlechaInicial(self):
        self.FlechaInicial.place(x=11,y=255)
        self.FlechaInicial.create_line(0,7,70,7, width=3.0, fill="#f45905")
        self.FlechaInicial.create_line(50,2,60,7, fill="#f45905", width=3.0)
        self.FlechaInicial.create_line(60,7,50,12, fill="#f45905", width=3.0)
        self.FlechaInicial.update()
    def pintarNormalFlecha1(self):
        self.Flecha1.place(x=151,y=255)
        self.Flecha1.create_line(0,7,100,7, width=3.0, fill="#2a1a5e")
        self.Flecha1.create_line(80,2,90,7, fill="#2a1a5e", width=3.0)
        self.Flecha1.create_line(90,7,80,12, fill="#2a1a5e", width=3.0)
        self.Flecha1.update()
    def pintarIluminadoFlecha1(self):
        self.Flecha1.place(x=151,y=255)
        self.Flecha1.create_line(0,7,100,7, width=3.0, fill="#f45905")
        self.Flecha1.create_line(80,2,90,7, fill="#f45905", width=3.0)
        self.Flecha1.create_line(90,7,80,12, fill="#f45905", width=3.0)
        self.Flecha1.update()
    def pintarNormalFlecha2(self):
        self.Flecha2.place(x=321,y=255)
        self.Flecha2.create_line(0,7,100,7, width=3.0, fill="#2a1a5e")
        self.Flecha2.create_line(80,2,90,7, fill="#2a1a5e", width=3.0)
        self.Flecha2.create_line(90,7,80,12, fill="#2a1a5e", width=3.0)
        self.Flecha2.update()
    def pintarIluminadoFlecha2(self):
        pass
    def pintarNormal_A_Numeral_P1(self):
        self.A_Numeral_p1.place(x=73,y=160)
        self.A_Numeral_p1.create_text(40,15,text="a, #/#a", fill="#2a1a5e",font=("",16))
        self.A_Numeral_p1.update()
    def pintarIluminado_A_Numeral_P1(self):
        self.A_Numeral_p1.place(x=73,y=160)
        self.A_Numeral_p1.create_text(40,15,text="a, #/#a", fill="#f45905",font=("",16))
        self.A_Numeral_p1.update()
    def pintarNormal_B_Numeral_P1(self):
        self.B_Numeral_p1.place(x=73,y=139)
        self.B_Numeral_p1.create_text(40,15,text="b, #/#b", fill="#2a1a5e",font=("",16))
        self.B_Numeral_p1.update()
    def pintarIluminado_B_Numeral_P1(self):
        self.B_Numeral_p1.place(x=73,y=139)
        self.B_Numeral_p1.create_text(40,15,text="b, #/#b", fill="#f45905",font=("",16))
        self.B_Numeral_p1.update()
    def pintarNormalAA(self):
        self.AA.place(x=73,y=118)
        self.AA.create_text(40,15,text="a, a/aa", fill="#2a1a5e",font=("",16))
        self.AA.update()
    def pintarIluminadoAA(self):
        self.AA.place(x=73,y=118)
        self.AA.create_text(40,15,text="a, a/aa", fill="#f45905",font=("",16))
        self.AA.update()
    def pintarNormalAB(self):
        self.AB.place(x=73,y=97)
        self.AB.create_text(40,15,text="b, a/ab", fill="#2a1a5e",font=("",16))
        self.AB.update()
    def pintarIluminadoAB(self):
        self.AB.place(x=73,y=97)
        self.AB.create_text(40,15,text="b, a/ab", fill="#f45905",font=("",16))
        self.AB.update()
    def pintarNormalBA(self):
        self.BA.place(x=73,y=76)
        self.BA.create_text(40,15,text="a, b/ba", fill="#2a1a5e",font=("",16))
        self.BA.update()
    def pintarIluminadoBA(self):
        self.BA.place(x=73,y=76)
        self.BA.create_text(40,15,text="a, b/ba", fill="#f45905",font=("",16))
        self.BA.update()
    def pintarNormalBB(self):
        self.BB.place(x=73,y=55)
        self.BB.create_text(40,15,text="b, b/bb", fill="#2a1a5e",font=("",16))
        self.BB.update()
    def pintarIluminadoBB(self):
        self.BB.place(x=73,y=55)
        self.BB.create_text(40,15,text="b, b/bb", fill="#f45905",font=("",16))
        self.BB.update()
    def pintarNormal_C_Numeral(self):
        self.C_Numeral.place(x=158,y=220)
        self.C_Numeral.create_text(40,15,text="c, #/#", fill="#2a1a5e",font=("",16))
        self.C_Numeral.update()
    def pintarIluminado_C_Numeral(self):
        self.C_Numeral.place(x=158,y=220)
        self.C_Numeral.create_text(40,15,text="c, #/#", fill="#f45905",font=("",16))
        self.C_Numeral.update()
    def pintarNormalCB(self):
        self.C_B.place(x=158,y=199)
        self.C_B.create_text(40,15,text="c, b/b", fill="#2a1a5e",font=("",16))
        self.C_B.update()
    def pintarIluminadoCB(self):
        self.C_B.place(x=158,y=199)
        self.C_B.create_text(40,15,text="c, b/b", fill="#f45905",font=("",16))
        self.C_B.update()
    def pintarNormalCA(self):
        self.C_A.place(x=158,y=178)
        self.C_A.create_text(40,15,text="c, a/a", fill="#2a1a5e",font=("",16))
        self.C_A.update()
    def pintarIluminadoCA(self):
        self.C_A.place(x=158,y=178)
        self.C_A.create_text(40,15,text="c, a/a", fill="#f45905",font=("",16))
        self.C_A.update()
    def pintarNormal_B_Lambda(self):
        self.B_LAMBDA.place(x=243,y=160)
        self.B_LAMBDA.create_text(40,15,text="b, b/y", fill="#2a1a5e",font=("",16))
        self.B_LAMBDA.update()
    def pintarIluminado_B_Lambda(self):
        self.B_LAMBDA.place(x=243,y=160)
        self.B_LAMBDA.create_text(40,15,text="b, b/y", fill="#f45905",font=("",16))
        self.B_LAMBDA.update()
    def pintarNormal_A_Lambda(self):
        self.A_LAMBDA.place(x=243,y=139)
        self.A_LAMBDA.create_text(40,15,text="a, a/y", fill="#2a1a5e",font=("",16))
        self.A_LAMBDA.update()
    def pintarIluminado_A_Lambda(self):
        self.A_LAMBDA.place(x=243,y=139)
        self.A_LAMBDA.create_text(40,15,text="a, a/y", fill="#f45905",font=("",16))
        self.A_LAMBDA.update()
    def pintarNormal_Lambda_Numeral(self):
        self.LAMBDA_Numeral.place(x=323,y=220)
        self.LAMBDA_Numeral.create_text(40,15,text="y, #/#", fill="#2a1a5e",font=("",16))
        self.LAMBDA_Numeral.update()
    def pintarIluminado_Lambda_Numeral(self):
        pass
    
    def pintarElementosPila(self, ultimoPilaY, textoApilar):
        ultimoPilaY -= 25
        self.PilaLineas.place(x=600,y=55)
        self.PilaLineas.create_text(22, ultimoPilaY, text=textoApilar, fill="#ffffff", font=("",16))
    def quitarElementosPila(self, ultimoPilaY, textoApilar):
        ultimoPilaY += 25
        self.PilaLineas.place(x=600,y=55)
        self.PilaLineas.create_text(22, ultimoPilaY, text=textoApilar, fill="#2a1a5e", font=("",16))
        self.PilaLineas.create_text(22, ultimoPilaY, text="8", fill="#2a1a5e", font=("",16))
        self.PilaLineas.create_text(22, ultimoPilaY, text="#", fill="#2a1a5e", font=("",16))
        self.PilaLineas.create_text(22, ultimoPilaY, text="9", fill="#2a1a5e", font=("",16))
        self.PilaLineas.create_text(22, ultimoPilaY, text="b", fill="#2a1a5e", font=("",16))
        self.PilaLineas.create_text(22, ultimoPilaY, text="a", fill="#2a1a5e", font=("",16))
        self.PilaLineas.create_text(22, ultimoPilaY, text="b", fill="#2a1a5e", font=("",16))
        self.PilaLineas.create_text(22, ultimoPilaY, text="a", fill="#2a1a5e", font=("",16))

    def pintandoTodo(self):
        self.pintarNormalEstado1()
        self.pintarNormalEstado2()
        self.pintarNormalEstado3()
        self.pintarNormalFlechaInicial()
        self.pintarNormalFlecha1()
        self.pintarNormalFlecha2()
        self.pintarNormal_A_Numeral_P1()
        self.pintarNormal_B_Numeral_P1()
        self.pintarNormalAA()
        self.pintarNormalAB()
        self.pintarNormalBA()
        self.pintarNormalBB()
        self.pintarNormal_C_Numeral()
        self.pintarNormalCB()
        self.pintarNormalCA()
        self.pintarNormal_B_Lambda()
        self.pintarNormal_A_Lambda()
        self.pintarNormal_Lambda_Numeral()
        
"""--------------- Fin de Clase de la Pila -------------------------------"""
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
    misCanvas = todosLosCanvas()
    misCanvas.pintandoTodo()
    misCanvas.pintarElementosPila(ultimoPilaY, "#")
    misCanvas.pintarIluminadoFlechaInicial()
    ultimoPilaY -= 25
 
    pilaPalindromo = Palindro.get()
    Palindromo=Pila()
    estado = 1
    color=1
    entrada = 1
    for i in range(0,len(pilaPalindromo)):
        misCanvas.pintandoTodo()
        transicion=pilaPalindromo[i]
        print(transicion)
        topePila=Palindromo.desapilar()
        if estado == 1:
            misCanvas.pintarIluminadoEstado1()
            # Estado1.create_oval(25,35,100,110, fill="#2a1a5e")
            # Estado1.create_text(63,75,text="P", fill="#f45905", font=("",24))
            # Estado1.create_line(32,10,32,50, fill="#f45905", width=3.0)
            # Estado1.create_line(32,10,93,10, fill="#f45905", width=3.0)
            # Estado1.create_line(93,10,93,50, fill="#f45905", width=3.0)
            # Estado1.create_line(88,37,93,50, fill="#f45905", width=3.0)
            # Estado1.create_line(98,37,93,50, fill="#f45905", width=3.0)
            if transicion=="a" and topePila=="#":
                Palindromo.apilar("#")
                Palindromo.apilar("a")
                misCanvas.pintarIluminado_A_Numeral_P1()
                # A_Numeral_p1.place(x=73,y=160)
                # A_Numeral_p1.create_text(40,15,text="a, #/#a", fill="#f45905",font=("",16))
                # A_Numeral_p1.update()
                misCanvas.pintarElementosPila(ultimoPilaY,"a")
                # pintarElementosPila(ultimoPilaY, "a")
                ultimoPilaY -= 25
            elif transicion=="b" and topePila=="#":
                Palindromo.apilar("#")
                Palindromo.apilar("b")
                misCanvas.pintarIluminado_B_Numeral_P1()
                # B_Numeral_p1.place(x=73,y=139)
                # B_Numeral_p1.create_text(40,15,text="b, #/#b", fill="#f45905",font=("",16))
                # B_Numeral_p1.update()
                misCanvas.pintarElementosPila(ultimoPilaY,"b")
                # pintarElementosPila(ultimoPilaY, "b")
                ultimoPilaY -= 25
            elif transicion=="a" and topePila=="a":
                Palindromo.apilar("a")
                Palindromo.apilar("a")
                misCanvas.pintarIluminadoAA()
                # AA.place(x=73,y=118)
                # AA.create_text(40,15,text="a, a/aa", fill="#f45905",font=("",16))
                # AA.update()
                misCanvas.pintarElementosPila(ultimoPilaY,"a")
                # pintarElementosPila(ultimoPilaY, "a")
                ultimoPilaY -= 25
            elif transicion=="b" and topePila=="a":
                Palindromo.apilar("a")
                Palindromo.apilar("b")
                misCanvas.pintarIluminadoAB()
                # AB.place(x=73,y=97)
                # AB.create_text(40,15,text="b, a/ab", fill="#f45905",font=("",16))
                # AB.update()
                misCanvas.pintarElementosPila(ultimoPilaY,"b")
                # pintarElementosPila(ultimoPilaY, "b")
                ultimoPilaY -= 25
            elif transicion=="a" and topePila=="b":
                Palindromo.apilar("b")
                Palindromo.apilar("a")
                misCanvas.pintarIluminadoBA()
                # BA.place(x=73,y=76)
                # BA.create_text(40,15,text="a, b/ba", fill="#f45905",font=("",16))
                # BA.update()
                misCanvas.pintarElementosPila(ultimoPilaY,"a")
                # pintarElementosPila(ultimoPilaY, "a")
                ultimoPilaY -= 25
            elif transicion=="b" and topePila=="b":
                Palindromo.apilar("b")
                Palindromo.apilar("b")
                misCanvas.pintarIluminadoBB()
                # BB.place(x=73,y=55)
                # BB.create_text(40,15,text="b, b/bb", fill="#f45905",font=("",16))
                # BB.update()
                misCanvas.pintarElementosPila(ultimoPilaY,"b")
                # pintarElementosPila(ultimoPilaY, "b")
                ultimoPilaY -= 25
            elif transicion=="c" and topePila=="#":
                misCanvas.pintarIluminadoFlecha1()
                # Flecha1.place(x=151,y=255)
                # Flecha1.create_line(0,7,100,7, width=3.0, fill="#f45905")
                # Flecha1.create_line(80,2,90,7, fill="#f45905", width=3.0)
                # Flecha1.create_line(90,7,80,12, fill="#f45905", width=3.0)
                # Flecha1.update()
                Palindromo.apilar("#")
                misCanvas.pintarIluminado_C_Numeral()
                # C_Numeral.place(x=158,y=220)
                # C_Numeral.create_text(40,15,text="c, #/#", fill="#f45905",font=("",16))
                # C_Numeral.update()
                estado = 2
            elif transicion=="c" and topePila=="b":
                misCanvas.pintarIluminadoFlecha1()
                # Flecha1.place(x=151,y=255)
                # Flecha1.create_line(0,7,100,7, width=3.0, fill="#f45905")
                # Flecha1.create_line(80,2,90,7, fill="#f45905", width=3.0)
                # Flecha1.create_line(90,7,80,12, fill="#f45905", width=3.0)
                # Flecha1.update()
                Palindromo.apilar("b")
                misCanvas.pintarIluminadoCB()
                # C_B.place(x=158,y=199)
                # C_B.create_text(40,15,text="c, b/b", fill="#f45905",font=("",16))
                # C_B.update()
                estado = 2
            elif transicion=="c" and topePila=="a":
                misCanvas.pintarNormalFlechaEstado1()
                # Estado1.place(x=50,y=190)
                # Estado1.create_line(32,10,32,50, fill="#2a1a5e", width=3.0)
                # Estado1.create_line(32,10,93,10, fill="#2a1a5e", width=3.0)
                # Estado1.create_line(93,10,93,50, fill="#2a1a5e", width=3.0)
                # Estado1.create_line(88,37,93,50, fill="#2a1a5e", width=3.0)
                # Estado1.create_line(98,37,93,50, fill="#2a1a5e", width=3.0)
                # Estado1.update()
                misCanvas.pintarIluminadoFlecha1()
                # Flecha1.place(x=151,y=255)
                # Flecha1.create_line(0,7,100,7, width=3.0, fill="#f45905")
                # Flecha1.create_line(80,2,90,7, fill="#f45905", width=3.0)
                # Flecha1.create_line(90,7,80,12, fill="#f45905", width=3.0)
                # Flecha1.update()
                Palindromo.apilar("a")
                misCanvas.pintarIluminadoCA()
                # C_A.place(x=158,y=178)
                # C_A.create_text(40,15,text="c, a/a", fill="#f45905",font=("",16))
                # C_A.update()
                estado = 2
            else:
                Palindromo.apilar(topePila)
                misCanvas.pintarIluminadoRojoEstado3()
                # Estado3.create_oval(20,20,100,100, fill="#cb3234")
                # Estado3.create_oval(25,25,95,95, fill="#2a1a5e")
                # Estado3.create_text(60,62,text="R", fill="#cb3234", font=("",24))
                # Estado3.update()

                speaker.Speak("La Expresión No Es Válida. El Color Rojo Lo Índica")
                return False
        elif estado == 2:
            if color==1:
                # estadosCanvas()
                color = 2
            misCanvas.pintarIluminadoEstado2()
            # Estado2.place(x=220,y=190)
            # Estado2.create_oval(25,35,100,110, fill="#2a1a5e")
            # Estado2.create_text(63,75,text="Q", fill="#f45905", font=("",24))
            # Estado2.create_line(32,10,32,50, fill="#f45905", width=3.0)
            # Estado2.create_line(32,10,93,10, fill="#f45905", width=3.0)
            # Estado2.create_line(93,10,93,50, fill="#f45905", width=3.0)
            # Estado2.create_line(88,37,93,50, fill="#f45905", width=3.0)
            # Estado2.create_line(98,37,93,50, fill="#f45905", width=3.0)
            # Estado2.update()
            if transicion=="a" and topePila=="a":
                if entrada==1:
                    ultimoPilaY -= 25
                    entrada=2
                # pass               
                # ultimoPilaY += 25
                misCanvas.quitarElementosPila(ultimoPilaY,"a")
                # quitarElementosPila(ultimoPilaY, "a")
                ultimoPilaY += 25
                misCanvas.pintarNormal_A_Lambda()
                # A_LAMBDA.place(x=243,y=139)
                # A_LAMBDA.create_text(40,15,text="a, a/y", fill="#f45905",font=("",16))
                # A_LAMBDA.update()
            elif transicion=="b" and topePila=="b":
                # pass              
                # ultimoPilaY += 25
                if entrada==1:
                    ultimoPilaY -= 25
                    entrada=2
                misCanvas.quitarElementosPila(ultimoPilaY, "b")
                # quitarElementosPila(ultimoPilaY, "b")
                ultimoPilaY += 25
                misCanvas.pintarIluminado_B_Lambda()
                # B_LAMBDA.place(x=243,y=160)
                # B_LAMBDA.create_text(40,15,text="b, b/y", fill="#f45905",font=("",16))
                # B_LAMBDA.update()
            else:
                Palindromo.apilar(topePila)
                misCanvas.pintarIluminadoRojoEstado3()
                # Estado3.create_oval(20,20,100,100, fill="#cb3234")
                # Estado3.create_oval(25,25,95,95, fill="#2a1a5e")
                # Estado3.create_text(60,62,text="R", fill="#cb3234", font=("",24))
                # Estado3.update()

                speaker.Speak("La Expresión No Es Válida. El Color Rojo Lo Índica")
                return False
        time.sleep(tiempo)
    topePila=Palindromo.desapilar()
    if topePila=="#":
            Palindromo.apilar("#")
            estado = 3
    if estado == 3:
        misCanvas.pintandoTodo()
        # estadosCanvas()
        # all_canvas()
        misCanvas.pintarIluminadoVerdeEstado3()
        # Estado3.create_oval(20,20,100,100, fill="#16ed48")
        # Estado3.create_oval(25,25,95,95, fill="#2a1a5e")
        # Estado3.create_text(60,62,text="R", fill="#16ed48", font=("",24))
        # Estado3.update()
        
        speaker.Speak("La Expresión Es Válida. El Color Verde Lo Índica")
        return True
    else:
        misCanvas.pintarIluminadoRojoEstado3()
        # Estado3.create_oval(20,20,100,100, fill="#cb3234")
        # Estado3.create_oval(25,25,95,95, fill="#2a1a5e")
        # Estado3.create_text(60,62,text="R", fill="#cb3234", font=("",24))
        # Estado3.update()

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

pilaYGlobal = 295
# pintarElementosPila(pilaYGlobal, "#")
# all_canvas()
# estadosCanvas()
misCanvasGlobal=todosLosCanvas()
misCanvasGlobal.pintandoTodo()
misCanvasGlobal.pintarElementosPila(pilaYGlobal, "#")
root.mainloop()