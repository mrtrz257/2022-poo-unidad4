import tkinter as tk
from tkinter import messagebox
from Provincia import Provincia

class FormularioProvincia(tk.LabelFrame):
    fields = ("Nombre", "Capital", "Cantidad de Habitantes", "Cantidad de Departamentos/partidos")
    def __init__(self, master, **kwargs):
        super().__init__(master, text="Provincia", padx=8, pady=8, **kwargs)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()
    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=25)
        label.grid(row=position, column=0)
        entry.grid(row=position, column=1)
        return entry
    def mostrarDatos(self, provincia):
        values = (provincia.getNombre(), provincia.getCapital(), provincia.getHabit(), provincia.getDepart(), provincia.getTemp(), provincia.getSens(), provincia.getHum())
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)
    def crearProvincia(self):
        values = [e.get() for e in self.entries]
        provincia = None
        try:
            provincia = Provincia(*values)
        except ValueError as e:
            messagebox.showerror("ERROR", str(e), parent=self)
        return provincia
    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)
