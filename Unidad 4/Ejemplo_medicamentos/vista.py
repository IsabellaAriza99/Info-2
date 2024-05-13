from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp
from modelo import medicamento


class VentanaPrincipal(QMainWindow):
    def __init__(self): #Constructor de la clase
        QMainWindow.__init__(self)
        loadUi('Ejemplo_medicamentos\Ventana_ppal.ui',self)
        self.__listaMedActual = {}
        self.setup()

    def setup(self):
        self.Ingresar_Paciente.clicked.connect(self.abrirVentanaIngreso)
        self.ingresarDr.clicked.connect(self.abrirVentDroga)

    def abrirVentanaIngreso(self):
        ventana_ingreso=VentanaIngreso(self)
        self.hide()
        ventana_ingreso.show()

    def abrirVentDroga(self):
        ventana_droga = VentanaDroga(self)
        ventana_droga.show()

    def recibir_infoPac(self,nombre,cedula):
        resultado=self.__miControlador.recibirInfoPac(nombre,cedula,self.__listaMedActual)
        if resultado:
            mensaje = "Paciente agregado"
        else:
            mensaje = "Paciente ya existe!!!!"

        msj= QMessageBox(self)
        msj.setIcon(QMessageBox.Warning) #Information
        msj.setText(mensaje)
        msj.show()
            
        
    def recibir_infoDroga(self,lista):    
        self.__listaMedActual=lista

        

    def asignarControlador(self,control):
        self.__miControlador = control

class VentanaIngreso(QDialog):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi('Ejemplo_medicamentos\Ventana_Ingreso.ui',self)
        self.__ventanaPadre = ppal
        self.setup()

    def setup(self):
        self.nombre.setValidator(QRegExpValidator(QRegExp("[a-zA-Z- ]+")))
        validar=QIntValidator()
        self.cedula.setValidator(validar)
        self.boton.accepted.connect(self.enviarInfo)
        self.boton.rejected.connect(self.cerrar)


    def enviarInfo(self):
        nombre=self.nombre.text()
        cedula=self.cedula.text()
        self.__ventanaPadre.recibir_infoPac(nombre,cedula)
        self.__ventanaPadre.show()


    def cerrar(self):
        self.__ventanaPadre.show()


class VentanaDroga (QDialog):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("Ejemplo_medicamentos\Ventana_Droga.ui",self)
        self.__ListaDroga = {}
        self.__ventanaPadre = ppal
        self.setup()

    def setup(self):
        self.agregarDroga.clicked.connect(self.agregar_droga)
        self.botonD.accepted.connect(self.enviarInfoDroga)
        self.botonD.rejected.connect(self.cerrar)

    def enviarInfoDroga(self):
        self.__ventanaPadre.recibir_infoDroga(self.__ListaDroga)
        self.__ventanaPadre.show()
        
    def agregar_droga(self):
        droga = self.droga.text()
        cantidadMed = self.cantidad.text()

        if droga not in self.__ListaDroga:
            m=medicamento()
            m.AsignarNombre(droga)
            m.AsignarDosis(cantidadMed)
            self.__ListaDroga[droga] = m
            mensaje = "Ingresó medicamento"
        else:
            mensaje = "ya existe el medicamento"
        
        msj = QMessageBox(self)
        msj.setIcon(QMessageBox.Information)
        msj.setText(mensaje)
        msj.show()

        self.droga.setText("")
        self.cantidad.setValue(0)

    def cerrar(self):
        self.__ventanaPadre.show()
        



        
