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