from tkinter import *
from tkinter import ttk, font

class Aplicacion():
    __ventana = None
    __precioBase = None
    __porcentajeIva = None
    __valorIva = None
    __precioFinal = None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title("Cálculo de Iva")
        self.__ventana.resizable(False, False)
        fuente = font.Font(weight="normal")
        self.marco = ttk.Frame(self.__ventana, borderwidth=4, relief="groove", padding=(10, 10))
        # /-----------------------------------------------------------------------------------/
        self.__precioBase = StringVar()
        self.__porcentajeIva = StringVar()
        self.__valorIva = StringVar()
        self.__precioFinal = StringVar()

        self.PrecioSinIvaLbl = ttk.Label(self.marco, text="Precio sin IVA", font=fuente, padding=(5,5))
        self.IVALbl = ttk.Label(self.marco, text="IVA", font=fuente, padding=(5, 5))
        self.PrecioConIvaLbl = ttk.Label(self.marco, text="Precio con IVA", font=fuente, padding=(5,5))

        self.PrecioSinIvaEntry = ttk.Entry(self.marco, textvariable=self.__precioBase, width=15)
        self.IVAEntry = ttk.Entry(self.marco, width=15, textvariable=self.__valorIva)
        self.PrecioConIvaEntry = ttk.Entry(self.marco, width=15, textvariable=self.__precioFinal)

        self.calcularBoton = ttk.Button(self.marco, text="Calcular", padding=(5,5), command=self.calcularPrecio)
        self.SalirBoton = ttk.Button(self.marco, text="Salir", padding=(5,5), command=quit)
        # /-----------------------------------------------------------------------------------/
        self.marco.grid(column=0, row=0)
        self.PrecioSinIvaLbl.grid(column=0, row=0)
        self.PrecioSinIvaEntry.grid(column=1, row=0)
        ttk.Radiobutton(self.marco, text="IVA 21%", value=0, variable=self.__porcentajeIva).grid(column=0, row=1, sticky='w', padx=15)
        ttk.Radiobutton(self.marco, text="IVA 10.5%", value=1, variable=self.__porcentajeIva).grid(column=0, row=2, sticky='w', padx=15)
        self.IVALbl.grid(column=0, row=3)
        self.IVAEntry.grid(column=1, row=3)
        self.PrecioConIvaLbl.grid(column=0, row=4)
        self.PrecioConIvaEntry.grid(column=1, row=4)
        self.calcularBoton.grid(column=0, row=5)
        self.SalirBoton.grid(column=1, row=5)
        self.__ventana.mainloop()

    def calcularPrecio(self):
        try:
            iva = 0.0
            precioFinal = 0.0
            precioBase = float(self.__precioBase.get())
            valor = self.__porcentajeIva.get()
            if valor=='0':
                iva = precioBase*(21/100)
                precioFinal = iva+precioBase
            elif valor=='1':
                iva = precioBase*(10.5/100)
                precioFinal = iva + precioBase
            self.__valorIva.set('{}'.format(iva))
            self.__precioFinal.set('{}'.format(precioFinal))
        except ValueError:
            self.__precioBase.set('')
            self.__valorIva.set('')
            self.__precioFinal.set('')

def testApp():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    testApp()
