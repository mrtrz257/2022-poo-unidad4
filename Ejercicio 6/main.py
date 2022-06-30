from RepositorioProvincias import RepositorioProvincias
from MostrarProvincia import MostrarProvincia
from Controlador import ControladorProvincia
from objectEncoder import objectEncoder

from api import API

def api():
    consultaAPI = API()
    ciudad = input("Ciudad: ")
    consultaAPI.run(ciudad)
    print(consultaAPI.getResultado())
    r = consultaAPI.getResultado()
    temp = ((r['main']['temp']))
    sens = ((r['main']['feels_like']))
    hum = ((r['main']['humidity']))
    print("{}\n{}\n{}".format(temp, sens, hum))

def main():
    conn = objectEncoder('datos.json')
    repo = RepositorioProvincias(conn)
    lista = MostrarProvincia()
    ctrl = ControladorProvincia(repo, lista)
    lista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()

if __name__ == '__main__':
    #api()
    main()
