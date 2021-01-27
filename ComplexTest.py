import unittest
import Calculator as calc

class TestComplexCalculator(unittest.TestCase):

    def test_sumar(self):
        c1, c2 = (-6, 8), (10, -7)
        self.assertEqual(calc.sumar(c1, c2), (4,1))

    def test_restar(self):
        c1, c2 = (-6, 8), (10, -7)
        self.assertEqual(calc.restar(c1, c2), (-16,15))

    def test_conjugado(self):
        c1 = (-9, 8)
        self.assertEqual(calc.conjugado(c1), (-9,-8))

    def test_multiplicar(self):
        c1, c2 = (3, -2), (1,2)
        self.assertEqual(calc.multiplicar(c1, c2),(7, 4))

    def test_dividir(self):
        c1, c2 = (-2, 1), (1,2)
        self.assertEqual(calc.dividir(c1, c2),(0, 1))

    def test_modulo(self):
        c1 = (10, 5)
        self.assertEqual(calc.modulo(c1), 11)

    def test_PolarCartesiano(self):
        c1 = (1, 1)
        self.assertEqual(calc.PolarCartesiano(c1), (0,0))

    def test_CartesianoPolar(self):
        c1 = (1, 1)
        self.assertEqual(calc.CartesianoPolar(c1), (1,0))

    def test_ComplexToString(self):
        c1 = (2,4)
        self.assertEqual(calc.ComplextToString(c1), "2+4i")

if __name__ == '__main__':
    unittest.main()