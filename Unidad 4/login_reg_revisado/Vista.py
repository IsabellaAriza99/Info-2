
# Importar librerias básicas
from PyQt5.QtWidgets import QMainWindow,QDialog, QMessageBox;
from PyQt5.uic import loadUi;

'''
QMainWindow: Es una clase que proporciona una ventana principal para aplicaciones GUI.

loadUi: Esta función permite cargar un archivo .ui creado con Qt Designer. 
El archivo .ui define la estructura y diseño de la interfaz gráfica.

QMessageBox: Es una clase que proporciona un cuadro de diálogo para mostrar mensajes.
'''

class Ventana(QMainWindow):
    def __init__(self): #Constructor de la clase
        QMainWindow.__init__(self)
        loadUi(r'C:\Users\isabe\OneDrive\Documentos\Info-2\Unidad 4\login_reg_revisado\VentanaLogin.ui',self)
        self.setup()

    def setup(self): # Llama al método setup, que está definido más adelante en la clase.
        #se programa la senal para el boton
        self.boton_ingresar.clicked.connect(self.accion_ingresar) #cuando el botón se presiona, se ejecutará el método accion_ingresar.
        self.boton_registrar.clicked.connect(self.accion_registrar)
    def asignarControlador(self,c): #Guarda un controlador para posteriormente hacer validaciones
        self.__controlador = c

    def accion_ingresar(self):
        #Extraer el texto de los campos campo_usuario y campo_password.
        usuario = self.campo_usuario.text()
        password = self.campo_password.text()
        #esta informacion la debemos pasar al controlador
        resultado = self.__controlador.validar_usuario(usuario,password) #Función de validación del controlador
        #Se crea la ventana de resultado
        msg = QMessageBox(self)
        msg.setWindowTitle("Resultado")
        #se selecciona el resultado de acuerdo al resultado de la operacion
        if resultado == True:
            msg.setText("Usuario Valido")
        else:
            msg.setText("Usuario no Valido")
        #se muestra la ventana
        msg.show()

    def recibir_info(self, u,p):
        resultado = self.__controlador.agregar_usuario(u,p)
        msg = QMessageBox(self)
        msg.setWindowTitle("Resultado")
        #se selecciona el resultado de acuerdo al resultado de la operacion
        if resultado == True:
            msg.setText("Usuario existente")
        else:
            #self.__controlador.agregar_usuario(u,p) 
            msg.setText("Usuario registrado con éxito")
        #se muestra la ventana
        msg.show()

    def accion_registrar(self):
        ventana_emergente=ventanaEmergente(self)
        ventana_emergente.show()

class ventanaEmergente(QDialog):
    def __init__(self, ppl=None):  # Añadir el argumento parent
        super().__init__(ppl)
        loadUi(r'C:\Users\isabe\OneDrive\Documentos\Info-2\Unidad 4\login_reg_revisado\ventana_secundaria.ui',self)
        self.setup()
        self.parent = ppl

    def setup(self):
        self.buttonBox.accepted.connect(self.conectarRegistro)
        self.buttonBox.rejected.connect(lambda:self.close())

    def conectarRegistro(self):
        usuario = self.usuario.text()
        password = self.contasena.text()
        self.parent.recibir_info(usuario, password)  # Usar la referencia al padre
        self.close()
