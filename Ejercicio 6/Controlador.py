from ManejadorProvincias import ManejadorProvincias
from MostrarProvincia import MostrarProvincia
from NuevaProvincia import NuevoProvincia

class ControladorProvincia(object):
    def __init__(self, repo, vista):
        self.repo = repo
        self.vista = vista
        self.seleccion = -1
        self.provincia = list(repo.obtenerListaProvincias())
    def crearProvincia(self):
        nuevaProvincia = NuevoProvincia(self.vista).mostrar()
        if nuevaProvincia:
            provincia = self.repo.agregarProvincia(nuevaProvincia)
            self.provincia.append(provincia)
            self.vista.agregarProvincia(provincia)
    def seleccionarProvincia(self, index):
        self.seleccion = index
        provincia = self.provincia[index]
        self.vista.verProvinciaEnFormulario(provincia)
    def start(self):
        for elemento in self.provincia:
            self.vista.agregarProvincia(elemento)
        self.vista.mainloop()
    def salirGrabarDatos(self):
        self.repo.grabarDatos()
