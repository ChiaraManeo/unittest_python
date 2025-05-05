import unittest
from main import somar, subtrair, multiplicar, dividir

class TestOperacoesMatematicas(unittest.TestCase):
    
    def test_somar(self):
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(-1, 1), 0)

    def test_subtrair(self):
        self.assertEqual(subtrair(10, 5), 5)
        self.assertEqual(subtrair(-1, -1), 0)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 4), 12)
        self.assertEqual(multiplicar(-2, 2), -4)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertAlmostEqual(dividir(7, 3), 2.333333, places=5)

    def test_dividir_por_zero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)

if __name__ == '__main__':
    unittest.main()