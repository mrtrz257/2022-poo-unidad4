import tkinter as tk
from tkinter import messagebox
from Paciente import Paciente

class FormularioPaciente(tk.LabelFrame):
    fields = ("Apellido", "Nombre", "Telefono", "Altura", "Peso")
    def __init__(self, master, **kwargs):
        super().__init__(master, text="Paciente", padx=8, pady=8, **kwargs)
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
    def mostrarDatos(self, paciente):
        values = (paciente.getApellido(), paciente.getNombre(), paciente.getTelefono(), paciente.getAltura(), paciente.getPeso())
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)
    def crearPacienteDesdeForm(self):
        values = [e.get() for e in self.entries]
        paciente = None
        try:
            paciente = Paciente(*values)
        except ValueError as e:
            messagebox.showerror("ERROR", str(e), parent=self)
        return paciente
    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)
