import tkinter as tk
from FormularioProvincias import FormularioProvincia

class InformacionProvincia(FormularioProvincia):
    fields = ("Nombre", "Capital", "Cantidad de Habitantes", "Cantidad de Departamentos/partidos", "Temperatura", "Sensación Termica", "Humedad")
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()
    def crearCampo(self, field):
        return super().crearCampo(field)
