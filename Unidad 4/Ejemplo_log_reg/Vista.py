# Importar librerias básicas
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDialog
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from PyQt5.uic import loadUi

'''
QMainWindow: Es una clase que proporciona una ventana principal para aplicaciones GUI.

loadUi: Esta función permite cargar un archivo .ui creado con Qt Designer. 
El archivo .ui define la estructura y diseño de la interfaz gráfica.

QMessageBox: Es una clase que proporciona un cuadro de diálogo para mostrar mensajes.
'''

class Ventana(QMainWindow):
    def __init__(self): #Constructor de la clase
        QMainWindow.__init__(self)
        loadUi(r'Ejemplo_log_reg\VentanaLogin.ui', self)
        self.setup()


    def setup(self): # Llama al método setup, que está definido más adelante en la clase.
        # Se programa la señal para el botón
        self.boton_ingresar.clicked.connect(self.accion_ingresar) # Cuando el botón se presiona, se ejecutará el método accion_ingresar.
        self.boton_registrarse.clicked.connect(self.abrirVentana)

    def abrirVentana(self):
        ventana_emergente = ventanaEmergente(self)  # Pasar la referencia de la ventana principal
        ventana_emergente.show()

    def asignarControlador(self, c): # Guarda un controlador para posteriormente hacer validaciones
        self.__controlador = c

    def accion_ingresar(self):
        # Extraer el texto de los campos campo_usuario y campo_password.
        usuario = self.campo_usuario.text()
        password = self.campo_password.text()
        # Esta información la debemos pasar al controlador
        resultado = self.__controlador.validar_usuario(usuario, password) # Función de validación del controlador
        # Se crea la ventana de resultado
        msg = QMessageBox(self)
        msg.setWindowTitle("Resultado")
        # Se selecciona el resultado de acuerdo al resultado de la operación
        if resultado:
            msg.setText("Usuario Válido")
        else:
            msg.setText("Usuario no Válido")
        # Se muestra la ventana
        msg.show()

    def recibir_info(self, usuario, password):
        resultado = self.__controlador.validar_usuario(usuario, password)
        # Se crea la ventana de resultado
        msg = QMessageBox(self)
        msg.setWindowTitle("Resultado")
        # Se selecciona el resultado de acuerdo al resultado de la operación
        if resultado:
            msg.setText("El usuario ya estaba registrado")
        else:
            self.__controlador.agregar_usuario(usuario, password)
            msg.setText("Usuario registrado con éxito")
        # Se muestra la ventana
        msg.show()

class ventanaEmergente(QDialog):
    def __init__(self, ppl=None):  # Añadir el argumento parent
        super().__init__(ppl)
        loadUi(r"Ejemplo_log_reg\Ventana_emergente.ui", self) # Lee el archivo de QtDesigner
        self.setWindowTitle("Ventana emergente") # Añadimos un título a nuestra ventana
        self.setup()
        self.parent = ppl  # Guardar la referencia al padre

    def setup(self):
        # self.campo_usuario.setValidator(QRegExpValidator(QRegExp("[a-zA-Z- ]+")))
        self.Registrarse.accepted.connect(self.registro)
        self.Registrarse.rejected.connect(lambda: self.close())

    def registro(self):
        # Extraer el texto de los campos campo_usuario y campo_password.
        #self.campo_usuario.setValidator(QRegExpValidator(QRegExp(r'^[\w\.-]+@[\w\.-]+\.\w+$')))
        self.campo_usuario.setValidator(QRegExpValidator(QRegExp(r'^[a-zA-Z]')))
        usuario = self.campo_usuario.text()
        password = self.campo_password.text()

        if self.campo_usuario.hasAcceptableInput():
            # Pasar la información al controlador si el correo es válido
            self.parent.recibir_info(usuario, password)  # Usar la referencia al padre
            self.close()
        else:
            # Mostrar un mensaje de error si el correo no es válido
            print("Usuario inválido")

