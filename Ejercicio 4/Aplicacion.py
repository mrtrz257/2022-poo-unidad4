from tkinter import *
from tkinter import ttk, font
from Fraccion import Fraccion
from functools import partial

class Aplicacion():
    __ventana = None
    __entrada = None
    __salida = None
    __band1 = None
    __band2 = None
    __num1 = None
    __num2 = None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title("Calculadora")
        self.__ventana.resizable(False, False)
        fuente = font.Font(weight="normal")
        self.marco = ttk.Frame(self.__ventana, borderwidth=4, relief="groove", padding=(10, 10))

        self.__entrada = StringVar()
        self.__salida = StringVar()
        self.__band1 = False
        self.__band2 = False
        self.__num1 = None
        self.__num2 = None

        self.entradaTxt = ttk.Entry(self.marco, textvariable=self.__entrada, font=fuente, state='readonly')
        self.salidaTxt = ttk.Entry(self.marco, textvariable=self.__salida, font=fuente, state='readonly')

        self.boton0 = ttk.Button(self.marco, text='0', command=partial(self.ponerNumero, '0'))
        self.boton1 = ttk.Button(self.marco, text='1', command=partial(self.ponerNumero, '1'))
        self.boton2 = ttk.Button(self.marco, text='2', command=partial(self.ponerNumero, '2'))
        self.boton3 = ttk.Button(self.marco, text='3', command=partial(self.ponerNumero, '3'))
        self.boton4 = ttk.Button(self.marco, text='4', command=partial(self.ponerNumero, '4'))
        self.boton5 = ttk.Button(self.marco, text='5', command=partial(self.ponerNumero, '5'))
        self.boton6 = ttk.Button(self.marco, text='6', command=partial(self.ponerNumero, '6'))
        self.boton7 = ttk.Button(self.marco, text='7', command=partial(self.ponerNumero, '7'))
        self.boton8 = ttk.Button(self.marco, text='8', command=partial(self.ponerNumero, '8'))
        self.boton9 = ttk.Button(self.marco, text='9', command=partial(self.ponerNumero, '9'))

        self.botonSuma = ttk.Button(self.marco, text='+', command=partial(self.ponerOperador, '+'))
        self.botonResta = ttk.Button(self.marco, text='-', command=partial(self.ponerOperador, '-'))
        self.botonMulti = ttk.Button(self.marco, text='*', command=partial(self.ponerOperador, '*'))
        self.botonDiv = ttk.Button(self.marco, text='%', command=partial(self.ponerOperador, '%'))

        self.botonLimpiar = ttk.Button(self.marco, text='Borrar', command=self.limpiar)
        self.botonFraccion = ttk.Button(self.marco, text='/', command=self.ponerFraccion)
        self.botonResult = ttk.Button(self.marco, text='=', command=self.calcular)

        self.marco.grid(column=0, row=0)
        self.entradaTxt.grid(column=0, row=0, pady=5, columnspan=2)
        self.salidaTxt.grid(column=0, row=1, pady=5, columnspan=2)

        self.boton9.grid(column=2, row=4, ipadx=10)
        self.boton8.grid(column=1, row=4, ipadx=10)
        self.boton7.grid(column=0, row=4, ipadx=10)
        self.boton6.grid(column=2, row=5, ipadx=10)
        self.boton5.grid(column=1, row=5, ipadx=10)
        self.boton4.grid(column=0, row=5, ipadx=10)
        self.boton3.grid(column=2, row=6, ipadx=10)
        self.boton2.grid(column=1, row=6, ipadx=10)
        self.boton1.grid(column=0, row=6, ipadx=10)
        self.boton0.grid(column=0, row=7, ipadx=10)

        self.botonSuma.grid(column=0, row=2, ipadx=10)
        self.botonResta.grid(column=1, row=2, ipadx=10)
        self.botonMulti.grid(column=0, row=3, ipadx=10)
        self.botonDiv.grid(column=1, row=3, ipadx=10)

        self.botonLimpiar.grid(column=2, row=3, ipadx=10)
        self.botonFraccion.grid(column=1, row=7, ipadx=10)
        self.botonResult.grid(column=2, row=7, ipadx=10)
        self.__salida.set('')
        self.__ventana.mainloop()

    def ponerNumero(self, num):
        text = self.__entrada.get()
        text += num
        self.__entrada.set(text)
    def validarOp(self, caracter):
        band = False
        if(caracter == '+'):
            band = True
        elif(caracter == '-'):
            band = True
        elif(caracter == '*'):
            band = True
        elif(caracter == '%'):
            band = True
        return band
    def ponerOperador(self, op):
        text = self.__entrada.get()
        if(not self.__band1):
            text += op
            self.__entrada.set(text)
            self.__band1 = True
            self.__band2 = False
    def crearFraccion(self, num):
        denominador = ''
        numerador = num[0]
        if(len(num) > 1):
            denominador = num[1]
        if(numerador == ''):
            numerador = '0'
        if(denominador == ''):
            denominador = '1'
        fraccion = Fraccion(int(numerador), int(denominador))
        return fraccion
    def validarFrac(self,text):
        band = False
        if('/' not in text or self.__band2 == False):
            band = True
            self.__band2 = True
        return band
    def ponerFraccion(self):
        text = self.__entrada.get()
        if(self.validarFrac(text)):
            text += '/'
            self.__entrada.set(text)
            self.__band3 = False
    def buscar(self, text, lista):
        band = -1
        i = 0
        while band == -1 and i < len(lista):
            if(lista[i] in text):
                band = i
            i+=1
        return band
    def validarCalculo(self, text):
        lista = ['+', '-', '*', '%']
        op = self.buscar(text, lista)
        if(op != -1):
            text = text.split(lista[op])
            num1 = text[0]
            num2 = text[1]
            if(num1 == ''):
                num1 = '0'
            if(num2 == ''):
                num2 = '0'
            num1 = num1.split('/')
            self.__num1 = self.crearFraccion(num1)
            num2 = num2.split('/')
            self.__num2 = self.crearFraccion(num2)
            resultado = lista[op]
        else:
            resultado = '='
            text = text.split('/')
            self.__num1 = self.crearFraccion(text)
        return resultado
    def calcular(self):
        resultado = 0
        text = self.__entrada.get()
        op = self.validarCalculo(text)
        if(op == '+'):
            resultado = self.__num1 + self.__num2
        elif(op == '-'):
            resultado = self.__num1 - self.__num2
        elif(op == '*'):
            resultado = self.__num1 * self.__num2
        elif(op == '%'):
            resultado = self.__num1 % self.__num2
        elif(op == '='):
            resultado = self.__num1
        resultado.Simplificacion()
        self.__salida.set('{}'.format(resultado))
    def limpiar(self):
        self.__entrada.set('')
        self.__band1 = False
        self.__salida.set('')
