class Fraccion:
    __numerador = None
    __denominador = None
    def __init__(self, num, den=1):
        self.__numerador = int(num)
        if den == 0:
            raise Exception("El Denominador no puede ser 0")
        self.__denominador = int(den)
    def getNum(self):
        return self.__numerador
    def getDen(self):
        return self.__denominador
    def __str__(self):
        return '{}/{}'.format(self.__numerador, self.__denominador)
    def __add__(self, other):
        denom = self.__denominador * other.getDen()
        numer = (self.__numerador * other.getDen()) + (other.getNum() * self.__denominador)
        self.__numerador = numer
        self.__denominador = denom
        return self
    def __sub__(self, other):
        denom = self.__denominador * other.getDen()
        numer = (self.__numerador * other.getDen()) - (other.getNum() * self.__denominador)
        self.__numerador = numer
        self.__denominador = denom
        return self
    def __mul__(self, other):
        denom = self.__denominador * other.getDen()
        numer = self.__numerador * other.getNum()
        self.__denominador = denom
        self.__numerador = numer
        return self
    def __mod__(self, other):
        denom = self.__denominador * other.getNum()
        numer = self.__numerador * other.getDen()
        self.__denominador = denom
        self.__numerador = numer
        return self
    def MCD(self):
        a = self.__numerador
        b = self.__denominador
        while b != 0:
            x = a%b
            a = b
            b = x
        maximo = a
        return maximo
    def Simplificacion(self):
        mcd = self.MCD()
        self.__numerador //= mcd
        self.__denominador //= mcd
        return '{}/{}'.format(self.__numerador, self.__denominador)
