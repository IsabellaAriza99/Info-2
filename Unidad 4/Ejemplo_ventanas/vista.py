#importamos las librerías necesarias
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.uic import loadUi;

'''
QMainWindow: Es una clase que proporciona una ventana principal para aplicaciones GUI.

loadUi: Esta función permite cargar un archivo .ui creado con Qt Designer. 
El archivo .ui define la estructura y diseño de la interfaz gráfica.
'''

#Creamos una clase ventana, que se hereda de la clase "QMainWindow"
class Ventana(QMainWindow):
    def __init__(self): #Constructor de la clase
        #Inicializa la ventana
        QMainWindow.__init__(self)
        loadUi(r"Unidad 4\Ejemplo_ventanas\view.ui",self) #Lee el archivo de QtDesigner
        
        self.setWindowTitle("Ejemplo") #Añadimos un título a nuestra ventana
        self.setup()

    def setup(self):
        self.boton_ventana.clicked.connect(self.abrirVentana) #cuando el botón se presiona, se ejecutará el método.
        self.boton_salir.clicked.connect(lambda:self.close())#Función predeterminada para salir

    def abrirVentana(self):
        ventana_emergente=ventanaEmergente()
        ventana_emergente.show()

class ventanaEmergente(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi(r"Unidad 4\Ejemplo_ventanas\view2.ui",self) #Lee el archivo de QtDesigner
        
        self.setWindowTitle("Ventana emergente") #Añadimos un título a nuestra ventana
        self.setup()

    def setup(self):
        self.buttonBox.accepted.connect(self.enviarInfo)
        self.buttonBox.rejected.connect(lambda:self.close())

    def enviarInfo(self):
        self.label.setText('Ventana emergente')

# se crea la instancia de la aplicación
app = QApplication(sys.argv)
# se crea la instancia de la ventana
miVentana = Ventana()
# se muestra la ventana 
miVentana.show()
# se entrega el control al sistema operativo
sys.exit(app.exec_())