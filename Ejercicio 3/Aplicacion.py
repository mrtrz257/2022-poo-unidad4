from tkinter import *
from tkinter import ttk, font
from api import API

class Aplicacion():
    __ventana = None
    __dolar = None
    __peso = None
    __aviso = None
    __valorVenta = None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Conversor de Moneda')
        self.__ventana.resizable(False, False)
        fuente = font.Font(weight="normal")
        self.marco = ttk.Frame(self.__ventana, borderwidth=4, relief="groove", padding=(10, 10))

        self.__dolar = StringVar()
        self.__peso = StringVar()
        self.__aviso = StringVar()
        self.__peso.set('')
        self.__aviso.set('')

        self.__dolar.trace('w', self.calcular)
        self.dolaresEntry = ttk.Entry(self.marco, textvariable=self.__dolar, width=10)
        self.dolaresLbl = ttk.Label(self.marco, text="dólares", font=fuente, padding=(5, 5))
        self.pesosTxtLbl = ttk.Label(self.marco, text="pesos", font=fuente, padding=(5, 5))
        self.pesoLbl = ttk.Label(self.marco, textvariable=self.__peso, font=fuente, padding=(5, 5))
        self.txt1 = ttk.Label(self.marco, text="es equivalente a", font=fuente, padding=(5, 5))
        self.txt2 = ttk.Label(self.marco, textvariable=self.__aviso)
        self.valorVentaBtn = ttk.Button(self.marco, text="Actualizar Valor de Venta", command=self.obtenerValorVenta, padding=(5,5))
        self.salirBtn = ttk.Button(self.marco, text="Salir", padding=(5,5), command=quit)

        self.marco.grid(column=0, row=0)
        self.salirBtn.grid(column=3, row=4)
        self.valorVentaBtn.grid(column=2, row=4)
        self.dolaresEntry.grid(column=2, row=0)
        self.dolaresLbl.grid(column=3, row=0)
        self.pesosTxtLbl.grid(column=3, row=1)
        self.pesoLbl.grid(column=2, row=1)
        self.txt1.grid(column=0, row=1, columnspan=2)
        self.txt2.grid(column=2, row=5, columnspan=2, sticky=E)
        self.__ventana.mainloop()

    def obtenerValorVenta(self):
        consultaAPI = API()
        consultaAPI.run()
        r = consultaAPI.getResultado()
        valor = (r[0]['casa']['venta'])
        venta = float(valor.replace(',', "."))
        self.__valorVenta = venta

    def calcular(self, *args):
        try:
            dolares = float(self.dolaresEntry.get())
            conversion = dolares*self.__valorVenta
            self.__peso.set('{:.2f}'.format(conversion))
            self.__aviso.set("")
        except ValueError:
            self.__peso.set('-')
            self.__dolar.set('')
        except TypeError:
            self.__aviso.set("Por Favor Actualizar El Valor del Dolar")
