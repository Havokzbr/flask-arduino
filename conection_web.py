import pyfirmata

''' 
Especificar a Porta Serial onde o Arduino será conectado,
por exemplo COM3 
PORTA = 'especificar_porta_serial'
'''

def singleton(cls):
    instances = {}

def getinstance():
    if cls not in instances:
        instances[cls] = cls()
    return instances[cls]
    return getinstance

# Classe singleton para o objeto arduino, responsável por criar diferentes instâncias
@singleton
class Arduino(object):
    def __init__(self, port=None):
        self.board = pyfirmata.Arduino(PORTA)

    def digitalWrite(self, pin, value):
        self.board.digital[pin].mode = pyfirmata.OUTPUT
        self.board.digital[pin].write(value)
