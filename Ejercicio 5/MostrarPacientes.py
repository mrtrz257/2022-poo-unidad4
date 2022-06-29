import tkinter as tk
from ListaPacientes import ListaPacientes
from ActualizarPaciente import ActualizarFormaPaciente

class MostrarPacientes(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Contactos")
        self.list = ListaPacientes(self, height=15)
        self.form = ActualizarFormaPaciente(self)
        self.btn_new = tk.Button(self, text="AgregarPaciente")
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)
    def setControlador(self, ctrl):
        self.btn_new.config(command=ctrl.crearPaciente)
        self.list.bind_double_click(ctrl.seleccionarPaciente)
        self.form.bind_save(ctrl.modificarPaciente)
        self.form.bind_delete(ctrl.borrarPaciente)
        self.form.bind_IMC(ctrl.calcularIMC)
    def agregarPaciente(self, paciente):
        self.list.insertar(paciente)
    def modificarPaciente(self, paciente, index):
        self.list.modificar(paciente, index)
    def borrarPaciente(self, index):
        self.form.limpiar()
        self.list.borrar(index)
    def obtenerDatos(self):
        return self.form.crearPacienteDesdeForm()
    def verPacienteEnFormulario(self, paciente):
        self.form.mostrarDatos(paciente)
