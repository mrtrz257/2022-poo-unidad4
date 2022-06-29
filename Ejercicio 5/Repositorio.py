from Paciente import Paciente
from objectEncoder import objectEncoder
from ManejadorPacientes import ManejadorPacientes

class RepositorioPacientes(object):
    __conn = None
    __manejador = None
    def __init__(self, conn):
        self.__conn = conn
        diccionario=self.__conn.leerJSONArchivo()
        self.__manejador=self.__conn.decodificarDiccionario(diccionario)
    def obtenerListaPacientes(self):
        return self.__manejador.getListaPaciente()
    def agregarPaciente(self, paciente):
        self.__manejador.agregarPaciente(paciente)
        return paciente
    def modificarPaciente(self, paciente):
        self.__manejador.actualizarPaciente(paciente)
        return paciente
    def borrarPaciente(self, paciente):
        self.__manejador.borrarPaciente(paciente)
    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.__manejador.toJSON())
