from Paciente import Paciente

class ManejadorPacientes:
    indice = 0
    __listaPacientes = None
    def __init__(self):
        self.__listaPacientes = []
    def agregarPaciente(self, paciente):
        paciente.rowid = ManejadorPacientes.indice
        ManejadorPacientes.indice += 1
        self.__listaPacientes.append(paciente)
    def getListaPaciente(self):
        return self.__listaPacientes
    def borrarPaciente(self, paciente):
        indice = self.obtenerIndicePaciente(paciente)
        self.__listaPacientes.pop(indice)
    def actualizarPaciente(self, paciente):
        indice = self.obtenerIndicePaciente(paciente)
        self.__listaPacientes[indice] = paciente
    def obtenerIndicePaciente(self, paciente):
        bandera = False
        i = 0
        while not bandera and i < len(self.__listaPacientes):
            if self.__listaPacientes[i].rowid == paciente.rowid:
                bandera = True
            else:
                i += 1
        return i
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            pacientes=[paciente.toJSON() for paciente in self.__listaPacientes]
        )
        return d
