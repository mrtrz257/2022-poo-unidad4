from Repositorio import RepositorioPacientes
from MostrarPacientes import MostrarPacientes
from ControladorPacientes import ControladorPacientes
from objectEncoder import objectEncoder

def main():
    conn = objectEncoder('pacientes.json')
    repo = RepositorioPacientes(conn)
    lista = MostrarPacientes()
    ctrl = ControladorPacientes(repo, lista)
    lista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()

if __name__ == '__main__':
    main()
