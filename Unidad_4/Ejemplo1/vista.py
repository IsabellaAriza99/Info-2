#importamos las librerías necesarias
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi;

#Creamos una clase ventana, que se hereda de la clase "QMainWindow"
class Ventana(QMainWindow):
    '''Esta es la clase principal'''
    #Inicializamos la ventana y conectamos los botones
    def __init__(self, ppal=None): #Constructor de la clase
        #Inicializa la ventana
        super(Ventana,self).__init__(ppal)
        loadUi("view.ui",self) #Lee el archivo de QtDesigner
        
        self.setWindowTitle("Ejemplo") #Añadimos un título a nuestra ventana
        
        #Conectar botón a función

        self.pushButton.clicked.connect(self.funcion)

        self.pbSalir.clicked.connect(lambda:self.close())

    def funcion(self):
        self.label.setText('Cambio')


# se crea la instancia de la aplicación
app = QApplication(sys.argv)
# se crea la instancia de la ventana
miVentana = Ventana()
# se muestra la ventana 
miVentana.show()
# se entrega el control al sistema operativo
sys.exit(app.exec_())