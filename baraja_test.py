import unittest
import baraja

class BarajaTest(unittest.TestCase):

    def test_crear_baraja(self):
        b = baraja.baraja()
        self.assertEqual(len(b),40)
        self.assertEqual(b[0],'Ao')
        self.assertEqual(b[39],'Rb')

if __name__ == "__main__":
    unittest.main()

    
