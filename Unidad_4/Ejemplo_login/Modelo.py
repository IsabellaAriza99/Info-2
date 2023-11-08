class Servicio(object):
    def __init__(self):
        self.__usuarios = {}
        #se crea un usuario inicial para arrancar el sistema
        self.__usuarios['1234'] = 'Isabella'
    
    def verificarUsuario(self, u, c):
        try:
            #Si existe la clave se verifica que sea el usuario
            if self.__usuarios[c] == u:
                return True
            else:
                return False
        except: #si la clave no existe se genera KeyError
            return False















