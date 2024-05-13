from Vista import Ventana
import sys
from PyQt5.QtWidgets import QApplication
from Modelo import Modelo


'''
Se importa la clase Ventana desde el módulo Vista. 

QApplication: Importa la clase básica para cualquier aplicación de PyQt5 que tenga una interfaz gráfica de usuario.

Se importa la clase Servicio desde el módulo Modelo
'''

class Controlador(object):
    def __init__(self, modelo):# Recibe instancias del modelo y la asigna a un atributo interno privado.
        self.__mi_modelo = modelo
    def validar_usuario(self, u, p): #Método que delega la verificación de un usuario al modelo 
        return self.__mi_modelo.verificarUsuario(u,p) #Método propio del modelo
    def agregar_usuario(self, u, p): #Método que delega la verificación de un usuario al modelo 
        return self.__mi_modelo.agregarUsuario(u,p) #Método propio del modelo   
#esta clase no cambia ya que en esta simplemente se hacen las conexiones que siempre van
class Principal(object):
    def __init__(self):
        self.__app = QApplication(sys.argv)
        self.__mi_vista = Ventana()
        self.__mi_modelo = Modelo()
        #hacemos enlaces entre las partes
        self.__mi_controlador = Controlador(self.__mi_modelo)
        self.__mi_vista.asignarControlador(self.__mi_controlador) #Se asigna el controlador

    def main(self):
        self.__mi_vista.show()
        sys.exit(self.__app.exec_())   

#se crean los objetos para la ejecucion    
p = Principal()
p.main()   
    
    
    
    
    
    
    
