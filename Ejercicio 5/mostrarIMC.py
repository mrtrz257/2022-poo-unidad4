import tkinter as tk
from Paciente import Paciente

class mostrarIMC(tk.Toplevel):
    def __init__(self, parent, imc, estado):
        super().__init__(parent)
        self.imc = tk.StringVar()
        self.estado = tk.StringVar()
        self.imc.set('{}'.format(imc))
        self.estado.set('{}'.format(estado))
        self.imcLbl = tk.Label(self, text="IMC")
        self.estadoLbl = tk.Label(self, text="Composicion Corporal")
        self.imcEntry = tk.Entry(self, textvariable=self.imc, state="readonly")
        self.estadoEntry = tk.Entry(self, textvariable=self.estado, state="readonly")
        self.volverBtn = tk.Button(self, text="Volver", command=self.destroy)
        self.imcLbl.grid(column=0, row=0, padx=5)
        self.estadoLbl.grid(column=0, row=1, padx=5)
        self.imcEntry.grid(column=1, row=0, padx=10)
        self.estadoEntry.grid(column=1, row=1, padx=10)
        self.volverBtn.grid(column=0, row=2, pady=4)
    def mostrar(self):
        self.grab_set()
        self.wait_window()
