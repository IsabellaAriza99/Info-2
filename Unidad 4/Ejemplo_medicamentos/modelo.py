class medicamento:
    def __init__(self):
        self.__droga="" 
        self.__dosis=0

    def AsignarNombre(self,n):
        self.__droga=n 

    def AsignarDosis(self,a):
        self.__dosis=a 

    def VerNombre(self):
        return self.__droga 

    def VerDosis(self):
        return self.__dosis 

class paciente:
    def __init__(self):
        self.__nombre="" 
        self.__cedula=0 

    def AsignarNombre(self,n):
        self.__nombre=n 

    def AsignarCedula(self,c):
        self.__cedula=c 
    
    #metodo para asignar todos los medicamentos
  
    def AsignarMedicamento(self,m):
        self.__medicamentos = m 

    def VerNombre(self):
        return self.__nombre 

    def VerCedula(self):
        return self.__cedula 

class sistema():
    def __init__(self):
        self.__listaPacientes={}

    def validar (self, cedula):
        return cedula not in self.__listaPacientes

    def agregarPaciente(self,nombre,cedula,droga):
        p=paciente()
        p.AsignarNombre(nombre)
        p.AsignarCedula(cedula)
        p.AsignarMedicamento(droga)
        self.__listaPacientes[cedula] = p

    


