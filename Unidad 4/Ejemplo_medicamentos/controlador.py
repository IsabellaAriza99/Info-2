from vista import VentanaPrincipal
from modelo import sistema
import sys
from PyQt5.QtWidgets import QApplication

class coordinador:
    def __init__(self, vista, modelo):
        self.__miVista = vista
        self.__miModelo = modelo

    def recibirInfoPac(self,nombre,cedula,medicamento):
        resultado = self.__miModelo.validar(cedula)
        if resultado:
            self.__miModelo.agregarPaciente(nombre,cedula,medicamento)
            return True
        else:
            return False


def main():
    app=QApplication(sys.argv)
    Visualizacion=VentanaPrincipal()
    Visualizacion.show()
    miModelo = sistema()
    mi_controlador=coordinador(Visualizacion, miModelo)
    Visualizacion.asignarControlador(mi_controlador)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
        