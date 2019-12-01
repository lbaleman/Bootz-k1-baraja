import unittest
from unittest.mock import patch
import baraja

def mi_eligecarta(i,longitud):
    if i == longitud-1:
        return 0
    else:
        return i+1

class BarajaTest(unittest.TestCase):

    def test_crear_baraja(self):
        b = baraja.baraja()
        self.assertEqual(len(b),40)
        self.assertEqual(b[0],'Ao')
        self.assertEqual(b[39],'Rb')

    @patch('baraja.elige_carta', mi_eligecarta)
    def test_mezclar_baraja(self):
        b = ['A','B','C','D','E']
        a = baraja.mezclar(b)
        mezclado = ['A','C','D','E','B']
        self.assertEqual(a,mezclado)

if __name__ == "__main__":
    unittest.main()

    
