_palos = ['o','c','e','b']
_cartas = ['A','2','3','4','5','6','7','S','C','R']

def baraja():
    result = []
    for palo in _palos:
        for carta in _cartas:
            result.append(carta + palo)
    
    return result
