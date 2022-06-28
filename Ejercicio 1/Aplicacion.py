from tkinter import *
from tkinter import ttk, font

class Aplicacion():
    __ventana = None
    __altura = None
    __peso = None
    __imc = None
    __estado = None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title("Calculadora de IMC")
        self.__ventana.resizable(False, False)
        fuente = font.Font(weight='bold')
        self.marco = ttk.Frame(self.__ventana, borderwidth=1, relief='flat', padding=(10,10,10,10))
        #/-----------------------------------------------------------------------------------/
        self.__altura = StringVar()
        self.__peso = StringVar()
        self.__imc = StringVar()
        self.__estado = StringVar()
        self.__imc.set('-')
        self.__altura.set('')
        self.__peso.set('')

        self.alturaLbl = ttk.Label(self.marco, text="Altura:", font=fuente, padding=(4,4))
        self.pesoLbl = ttk.Label(self.marco, text="Peso:", font=fuente, padding=(4, 4))
        self.entradaAltura = ttk.Entry(self.marco, textvariable=self.__altura, width=40)
        self.entradaPeso = ttk.Entry(self.marco, textvariable=self.__peso, width=40)
        self.cmLbl = ttk.Label(self.marco, text="cm", font=fuente)
        self.kgLbl = ttk.Label(self.marco, text="kg", font=fuente)
        self.separador = ttk.Separator(self.marco, orient=HORIZONTAL)
        self.botonCalc = ttk.Button(self.marco, text="Calcular", padding=(4,4), command=self.calcularIMC)
        self.botonLimpiar = ttk.Button(self.marco, text="Limpiar", padding=(4,4), command=self.limpiar)
        self.resultadoLabler = ttk.Label(self.marco, text="Tu indice de Masa Corporal (IMC) es:", font=fuente)
        self.imcLbl = ttk.Label(self.marco, textvariable=self.__imc, font=fuente)
        self.estadoLbl = ttk.Label(self.marco, textvariable=self.__estado, font=fuente)
        # /-----------------------------------------------------------------------------------/
        self.marco.grid(column=0, row=0)
        self.alturaLbl.grid(column=0, row=0)
        self.pesoLbl.grid(column=0, row=1)
        self.entradaAltura.grid(column=1, row=0, columnspan=2)
        self.entradaPeso.grid(column=1, row=1, columnspan=2)
        self.cmLbl.grid(column=3, row=0)
        self.kgLbl.grid(column=3, row=1)
        self.separador.grid(column=0, row=3, columnspan=3)
        self.botonCalc.grid(column=1, row=3)
        self.botonLimpiar.grid(column=2, row=3)
        self.resultadoLabler.grid(column=0, row=4, columnspan=3)
        self.imcLbl.grid(column=3, row=4)
        self.estadoLbl.grid(column=1, row=5, columnspan=3)
        self.__ventana.mainloop()

    def calcularIMC(self):
        try:
            alt = float(self.entradaAltura.get())/100
            peso = float(self.entradaPeso.get())
            imc = peso/(alt*alt)
            self.establecerEstado(imc)
            self.__imc.set('{:.3}'.format(imc))
        except ValueError:
            self.limpiar()
    def limpiar(self):
        self.__peso.set('')
        self.__altura.set('')
        self.__imc.set('')
        self.__estado.set('')
        self.entradaAltura.focus_set()
    def establecerEstado(self, imc):
        if imc > 0 and imc < 18.5:
            self.__estado.set("Peso Inferior al Normal")
        elif imc > 18.5 and imc < 25:
            self.__estado.set("Peso Normal")
        elif imc > 25 and imc < 30:
            self.__estado.set("Peso Superior al Normal")
        else:
            self.__estado.set("Obesidad")
