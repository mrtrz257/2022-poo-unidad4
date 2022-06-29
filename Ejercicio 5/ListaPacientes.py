import tkinter as tk
from Paciente import Paciente

class ListaPacientes(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.lb.yview())
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=2)
    def insertar(self, paciente, index=tk.END):
        texto = '{}, {}'.format(paciente.getApellido(), paciente.getNombre())
        self.lb.insert(index, texto)
    def borrar(self, index):
        self.lb.delete(index, index)
    def modificar(self, paciente, index):
        self.borrar(index)
        self.insertar(paciente, index)
    def bind_double_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)
