class sistema(object):
    def __init__(self):
       self.nivel1=10
       self.nivel2=10 
    def ampliarSenal(self,valor1):
        self.nivel1 = valor1*0.1
        return self.nivel1

    def frecuenciaSenal(self, valor2):
        self.nivel2 = valor2*0.05
        return self.nivel2