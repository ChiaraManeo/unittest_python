import unittest
from main import somar, subtrair, multiplicar, dividir

class TestCalculadora(unittest.TestCase):
    def test_somar(self):
        self.assertEqual(2 + 3, 5)

    def test_subtrair(self):
        self.assertEqual(5 - 3, 2)

class TestOutrasOperacoes(unittest.TestCase):
    def test_multiplicar(self):
        self.assertEqual(3 * 4, 12)

    def test_dividir(self):
        self.assertEqual(10 / 2, 5)

if __name__ == '__main__':
    unittest.main()
