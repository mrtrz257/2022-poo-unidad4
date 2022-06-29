import tkinter as tk
from Paciente import Paciente

class mostrarIMC(tk.Toplevel):
    fields = ("IMC", "Composición Corporal")
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.paciente = None
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack(pady=20, padx=20)
    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=25, state="readonly")
        label.grid(row=position, column=0)
        entry.grid(row=position, column=1)
        return entry
    def mostrar(self):
        self.grab_set()
        self.wait_window()
        return self.paciente
