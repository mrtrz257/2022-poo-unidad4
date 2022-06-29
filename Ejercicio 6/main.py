from tkinter import *
from tkinter import ttk, font
from api import API

class Aplicacion():
    __ventana = None
    def __init__(self):
        self.__ventana = Tk()

def testApp():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    #testApp()
    consultaAPI = API()
    ciudad = input("Ciudad: ")
    consultaAPI.run(ciudad)
    print(consultaAPI.getResultado())
    r = consultaAPI.getResultado()
    print('Temperatura: {}'.format(r['main']['temp']))
    print('Sensacion Termica: {}'.format(r['main']['feels_like']))
    print('Humedad: {}'.format(r['main']['humidity']))
