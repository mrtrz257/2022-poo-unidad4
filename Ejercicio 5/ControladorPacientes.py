from ManejadorPacientes import ManejadorPacientes
from MostrarPacientes import MostrarPacientes
from NuevoPaciente import NuevoPaciente
from mostrarIMC import mostrarIMC

class ControladorPacientes(object):
    def __init__(self, repo, vista):
        self.repo = repo
        self.vista = vista
        self.seleccion = -1
        self.pacientes = list(repo.obtenerListaPacientes())
    def crearPaciente(self):
        nuevoPaciente = NuevoPaciente(self.vista).mostrar()
        if nuevoPaciente:
            paciente = self.repo.agregarPaciente(nuevoPaciente)
            self.pacientes.append(paciente)
            self.vista.agregarPaciente(paciente)
    def seleccionarPaciente(self, index):
        self.seleccion = index
        paciente = self.pacientes[index]
        self.vista.verPacienteEnFormulario(paciente)
    def modificarPaciente(self):
        if self.seleccion==-1:
            return
        rowid = self.pacientes[self.seleccion].rowid
        detallesPaciente = self.vista.obtenerDatos()
        detallesPaciente.rowid = rowid
        paciente = self.repo.modificarPaciente(detallesPaciente)
        self.pacientes[self.seleccion] = paciente
        self.vista.modificarPaciente(paciente, self.seleccion)
        self.seleccion = -1
    def borrarPaciente(self):
        if self.seleccion==-1:
            return
        paciente = self.pacientes[self.seleccion]
        self.repo.borrarPaciente(paciente)
        self.pacientes.pop(self.seleccion)
        self.vista.borrarPaciente(self.seleccion)
        self.seleccion=-1
    def calcularIMC(self):
        if self.seleccion == -1:
            return
        paciente = self.pacientes[self.seleccion]
        calculoIMC = self.repo.calcularIMC(paciente)
        estado = self.repo.estado(calculoIMC)
        imc = mostrarIMC(self.vista).mostrar()
    def start(self):
        for elemento in self.pacientes:
            self.vista.agregarPaciente(elemento)
        self.vista.mainloop()
    def salirGrabarDatos(self):
        self.repo.grabarDatos()
