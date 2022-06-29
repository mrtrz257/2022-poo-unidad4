import tkinter as tk
from FormularioPaciente import FormularioPaciente

class ActualizarFormaPaciente(FormularioPaciente):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.btn_save = tk.Button(self, text="Guardar")
        self.btn_delete = tk.Button(self, text="Borrar")
        self.btn_IMC = tk.Button(self, text="Ver IMC")
        self.btn_save.pack(side=tk.RIGHT, ipadx=4, padx=4, pady=4)
        self.btn_delete.pack(side=tk.RIGHT, ipadx=4, padx=4, pady=4)
        self.btn_IMC.pack(side=tk.RIGHT, ipadx=4, padx=4, pady=4)
    def bind_save(self, callback):
        self.btn_save.config(command=callback)
    def bind_delete(self, callback):
        self.btn_delete.config(command=callback)
    def bind_IMC(self, callback):
        self.btn_IMC.config(command=callback)
