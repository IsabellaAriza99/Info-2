import sys
import numpy as np
from PyQt5 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi;

class VentanaPrincipal(QMainWindow):
    #constructor
    def __init__(self, ppal=None):
        super(VentanaPrincipal,self).__init__(ppal)
        loadUi('Unidad 4\pyqt5_matplotlib\grafica.ui',self)
        self.setup()
    #metodo para configurar las senales-slots y otros de la interfaz
    def setup(self):
        #se programa la senal para el boton
        self.grafica=Canvas_grafica()
        self.verticalLayout_grafica.addWidget(self.grafica)
        self.slider1.valueChanged.connect(self.slider_uno)
        self.slider2.valueChanged.connect(self.slider_dos)
        self.boton_salir.clicked.connect(lambda:self.close())
        
    def asignarControlador(self,c):
        self.__controlador = c

    def slider_uno(self, event):
        valor1 = self.__controlador.datos_slide1(event)
        self.grafica.datos1(valor1)

    def slider_dos(self, event):
        valor2 = self.__controlador.datos_slide2(event)
        self.grafica.datos2(valor2) 

class Canvas_grafica(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig , self.ax = plt.subplots(facecolor='gray')
        super().__init__(self.fig) 
        self.ax.grid()
        self.ax.margins(x=0)
        self.nivel1 = 10
        self.nivel2 = 1
        self.grafica_datos()

    def datos1(self, valor1):
        self.nivel1 = valor1

    def datos2(self, valor2):
        self.nivel2 = valor2

    def grafica_datos(self):
        plt.title("Grafica en PyQt5 con Matplotlib")
        x = np.arange(-np.pi, 10*np.pi, 0.01) 
        line, = self.ax.plot(x, self.nivel1*np.sin(self.nivel2*x), color='r',linewidth=2)
        self.draw()     
        line.set_ydata(np.sin(x)+24)
        QtCore.QTimer.singleShot(10, self.grafica_datos)



