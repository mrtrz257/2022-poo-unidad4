import tkinter as tk
from ListaProvincias import ListaProvincias
from InformacionProvincias import InformacionProvincia

class MostrarProvincia(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Provincias")
        self.list = ListaProvincias(self, height=15)
        self.form = InformacionProvincia(self)
        self.btn_new = tk.Button(self, text="Agregar Provincia")
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)
        self.form.pack(padx=10, pady=10)
    def setControlador(self, ctrl):
        self.btn_new.config(command=ctrl.crearProvincia)
        self.list.bind_double_click(ctrl.seleccionarProvincia)
    def agregarProvincia(self, provincia):
        self.list.insertar(provincia)
    def obtenerDatos(self):
        return self.form.crearProvincia()
    def verProvinciaEnFormulario(self, provincia):
        self.form.mostrarDatos(provincia)
