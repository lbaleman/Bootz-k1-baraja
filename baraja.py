import random
_palos = ['o','c','e','b']
_cartas = ['A','2','3','4','5','6','7','S','C','R']

def baraja():
    result = []
    for palo in _palos:
        for carta in _cartas:
            result.append(carta + palo)
    return result

def elige_carta(i,longitud):
    return random.randint(0, longitud-1)


def mezclar(b):
    for i in range(len(b)):
        azar = elige_carta(i, len(b))
        aux  = b[i]
        b[i] = b[azar]
        b[azar] = aux

    return b

class Baraja():
    naipes = []
    __palos = ['o','c','e','b']
    __cartas = ['A','2','3','4','5','6','7','S','C','R']

    def __init__(self):
        self.naipes = []
        for palo in self.__palos:
            for carta in self.__cartas:
                self.naipes.append(carta + palo)

    def elige_carta(self, i):
        return random.randint(0, len(self.naipes)-1)

    # No hace falta poner def mezclar(self, naipe), porque naipe es un atributo de la clase y ya la tenemos creada#
    # seria redundante. Mi instancia va a estar definida por sus naipes. No hace falta return porque al tener#
    # self delante es un atributo referido a nuestra variable
    def mezclar(self):
        for i in range(len(self.naipes)):
            azar = self.elige_carta(i)
            aux  = self.naipes[i]
            self.naipes[i] = self.naipes[azar]
            self.naipes[azar] = aux

    def repartir(self, cartas, jugadores):
        jugadas = []
        for i in range(jugadores):
            jugadas.append([])
            for j in range(cartas):
                jugadas[i].append(self.naipes[j*jugadores + i])

        repartidas = cartas*jugadores
        self.naipes = self.naipes[repartidas:]

        return jugadas
    
    def repartirRamon(self, cartas, jugadores):
        jugadas=[]
        for i in range(jugadores):
            jugadas.append([])
        
        for j in range(cartas):
            for item in jugadas:
                cartas=self.naipes.pop(0)
                item.append(cartas)
        return jugadas

     
    