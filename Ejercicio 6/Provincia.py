class Provincia:
    __nombre = None
    __capital = None
    __habitantes = None
    __departamentos = None
    __temperatura = None
    __sensacion = None
    __humedad = None
    def __init__(self, nombre, capital, habitantes, departamentos, temperatura=0.0, sensacion=0.0, humedad=0.0):
        self.__nombre = self.requerido(nombre, 'Nombre es un valor requerido')
        self.__capital = self.requerido(capital, 'Capital es un valor requerido')
        self.__habitantes = self.requerido(habitantes, 'Cantidad de Habitantes es un valor requerido')
        self.__departamentos = self.requerido(departamentos, 'Cantidad de Departamentos es un valor requerido')
        self.__temperatura = float(temperatura)
        self.__sensacion = float(sensacion)
        self.__humedad = float(humedad)
    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor
    def setInfo(self, temperatura, sensacion, humedad):
        self.__temperatura = float(temperatura)
        self.__sensacion = float(sensacion)
        self.__humedad = float(humedad)
    def getNombre(self):
        return self.__nombre
    def getCapital(self):
        return self.__capital
    def getHabit(self):
        return self.__habitantes
    def getDepart(self):
        return self.__departamentos
    def getTemp(self):
        return self.__temperatura
    def getSens(self):
        return self.__sensacion
    def getHum(self):
        return self.__humedad
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                nombre=self.__nombre,
                capital=self.__capital,
                habitantes=self.__habitantes,
                departamentos=self.__departamentos,
                temperatura=self.__temperatura,
                sensacion=self.__sensacion,
                humedad=self.__humedad
            )
        )
        return d
