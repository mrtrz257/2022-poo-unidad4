class Provincia:
    __nombre = None
    __capital = None
    __cantHabit = None
    __cantDepart = None
    def __init__(self, nom, cap, habit, dep):
        self.__nombre = self.requerido(nom, 'Nombre es un valor requerido')
        self.__capital = self.requerido(cap, 'Capital es un valor requerido')
        self.__cantHabit = self.requerido(habit, 'Cantidad de Habitantes es un valor requerido')
        self.__cantDepart = self.requerido(dep, 'Cantidad de Departamentos es un valor requerido')
    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor
    def getNom(self):
        return self.__nombre
    def getCap(self):
        return self.__capital
    def getHabit(self):
        return self.__cantHabit
    def getDepart(self):
        return self.__cantDepart
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                nombre=self.__nombre,
                capital=self.__capital,
                habitantes=self.__cantHabit,
                departamentos=self.__cantDepart
            )
        )
        return d
