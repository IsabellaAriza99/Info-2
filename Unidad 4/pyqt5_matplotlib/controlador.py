from PyQt5.QtWidgets import QApplication
import sys
from vista import VentanaPrincipal
from modelo import sistema

class Coordinador(object):
    def __init__(self,vista,sistema):
        self.__mi_vista=vista
        self.__mi_sistema=sistema

    def datos_slide1(self, valor1):
        return self.__mi_sistema.ampliarSenal(valor1)
    def datos_slide2(self, valor2):
        return self.__mi_sistema.frecuenciaSenal(valor2)


class Principal(object):
    def __init__(self):        
        self.__app=QApplication(sys.argv)
        self.__mi_vista=VentanaPrincipal()
        self.__mi_sistema=sistema()
        self.__mi_controlador=Coordinador(self.__mi_vista,self.__mi_sistema)
        self.__mi_vista.asignarControlador(self.__mi_controlador)
    def main(self):
        self.__mi_vista.show()
        sys.exit(self.__app.exec_())  

p=Principal()
p.main()