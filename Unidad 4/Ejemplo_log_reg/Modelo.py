class Modelo(object):
    def __init__(self):
        self.__usuarios = {}
        #se crea un usuario inicial para arrancar el sistema
        self.__usuarios['1234'] = 'Isabella'
        self.__usuarios['admin'] = 'admin'
    
    def verificarUsuario(self, u, p):
        try:
            #Si existe la clave se verifica que sea el usuario
            if self.__usuarios[p] == u:
                return True
            else:
                return False
        except: #si la clave no existe para evitar KeyError
            return False

    def agregarUsuario(self, u, p):
        self.__usuarios[p] = u














