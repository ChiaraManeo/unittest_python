import unittest
from test_main import TestOperacoesMatematicas 
from test_main import TestCalculadora

suite = unittest.TestSuite()

suite.addTest(TestCalculadora('test_somar'))
suite.addTest(TestOutrasOperacoes('test_dividir'))

runner = unittest.TextTestRunner()
runner.run(suite)
