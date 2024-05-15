import unittest
from src.logica.EcuacionSegundoGrado import EcuacionSegundoGrado

class TestEcuacionSegundoGrado(unittest.TestCase):

    def setUp(self):
        self.calculoRaices = EcuacionSegundoGrado()

    def tearDown(self):
        self.calculoRaices = None

    def test_calculoESG_dosNumeros_retornaSolucion(self):
        #ARRANGE
        a=3
        b=-5
        c=1
        resultadoEsperadoRaiz1 = 1.43
        resultadoEsperadoRaiz2 = 0.23

        #DO
        resultadoActualRaiz1, resultadoActualRaiz2 = self.calculoRaices.calculoEcuacionSegundoGrado(a,b,c)

        #ASSERT
        self.assertAlmostEqual(resultadoEsperadoRaiz1, resultadoActualRaiz1, 2)
        self.assertAlmostEqual(resultadoEsperadoRaiz2, resultadoActualRaiz2, 2)


if __name__ == '__main__':
    unittest.main()
