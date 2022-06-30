from Provincia import Provincia
from api import API

class ManejadorProvincias:
    indice = 0
    __listaProvincias = None
    __api = None
    def __init__(self):
        self.__listaProvincias = []
        self.__api = API()
    def agregarProvincia(self, provincia):
        provincia.rowid = ManejadorProvincias.indice
        self.iniciarApi(provincia)
        diccionario = self.getDiccionario()
        self.condicionesMet(provincia, diccionario)
        ManejadorProvincias.indice += 1
        self.__listaProvincias.append(provincia)
    def getListaProvincias(self):
        return self.__listaProvincias
    def obtenerIndiceProvincia(self, provincia):
        bandera = False
        i = 0
        while not bandera and i < len(self.__listaProvincias):
            if self.__listaProvincias[i].rowid == provincia.rowid:
                bandera = True
            else:
                i += 1
        return i
    def actualizarProvincia(self, provincia):
        indice = self.obtenerIndiceProvincia(provincia)
        self.__listaProvincias[indice] = provincia
    def iniciarApi(self, nom):
        self.__api.run(nom)
    def getDiccionario(self):
        return self.__api.getResultado()
    def condicionesMet(self, provincia, diccionario):
        temp = diccionario['main']['temp']
        sens = diccionario['main']['feels_like']
        hum = diccionario['main']['humidity']
        provincia.setInfo(temp, sens, hum)
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            provincia=[provincia.toJSON() for provincia in self.__listaProvincias]
        )
        return d
