#importamos las librerías necesarias
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi;

'''
QMainWindow: Es una clase que proporciona una ventana principal para aplicaciones GUI.

loadUi: Esta función permite cargar un archivo .ui creado con Qt Designer. 
El archivo .ui define la estructura y diseño de la interfaz gráfica.
'''

#Creamos una clase ventana, que se hereda de la clase "QMainWindow"
class Ventana(QMainWindow):
    def __init__(self): #Constructor de la clase ventana
        QMainWindow.__init__(self) # inicializa el constructor de la clase base QMainWindow.
        loadUi(r"Unidad 4\Ejemplo1\view.ui",self) #Lee el archivo de QtDesigner

# se crea la instancia de la aplicación
app = QApplication(sys.argv)
# se crea la instancia de la ventana
miVentana = Ventana()
# se muestra la ventana 
miVentana.show()
# se entrega el control al sistema operativo
sys.exit(app.exec_())