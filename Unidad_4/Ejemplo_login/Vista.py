
# Importar librerias básicas
from PyQt5.QtWidgets import QApplication,QMainWindow, QDialog, QMessageBox;
from PyQt5.uic import loadUi;

class VentanaPrincipal(QMainWindow):
    #constructor
    def __init__(self, ppal=None):
        super(VentanaPrincipal,self).__init__(ppal)
        loadUi('VentanaLogin.ui',self)
        self.setup()
    #metodo para configurar las senales-slots y otros de la interfaz
    def setup(self):
        #se programa la senal para el boton
        self.boton_ingresar.clicked.connect(self.accion_ingresar)
    def asignarControlador(self,c):
        self.__controlador = c
    def accion_ingresar(self):
        print("Boton presionado")
        usuario = self.campo_usuario.text()
        password = self.campo_password.text()
        #esta informacion la debemos pasar al controlador
        resultado = self.__controlador.validar_usuario(usuario,password)
        #se crea la ventana de resultado
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Resultado")
        #se selecciona el resultado de acuerdo al resultado de la operacion
        if resultado == True:
            msg.setText("Usuario Valido")
        else:
            msg.setText("Usuario no Valido")
        #se muestra la ventana
        msg.show()
        
        
        