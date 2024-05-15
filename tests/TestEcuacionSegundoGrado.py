import unittest
from src.logica.EcuacionSegundoGrado import EcuacionSegundoGrado

class TestEcuacionSegundoGrado(unittest.TestCase):

    def setUp(self):
        self.calculoRaices = EcuacionSegundoGrado()

    def tearDown(self):
        self.calculoRaices = None

    def test_calculoESG_dosNumeros_retornaSolucion(self):
        #ARRANGE
        a=1
        b=2
        c=1
        resultadoEsperadoRaiz1 = -1
        resultadoEsperadoRaiz2 = -1

        #DO
        resultadoActualRaiz1, resultadoActualRaiz2 = self.calculoRaices.calculoEcuacionSegundoGrado(a,b,c)

        #ASSERT
        self.assertEqual(resultadoEsperadoRaiz1, resultadoActualRaiz1)
        self.assertEqual(resultadoEsperadoRaiz2, resultadoActualRaiz2)


if __name__ == '__main__':
    unittest.main()
