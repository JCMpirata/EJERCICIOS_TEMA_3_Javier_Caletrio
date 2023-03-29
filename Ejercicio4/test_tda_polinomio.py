import TDA_Polinomio
import unittest

# Pruebas unitarias

class TestPolinomio(unittest.TestCase):
    def test_suma(self):
        polinomio1 = TDA_Polinomio.Polinomio()
        polinomio2 = TDA_Polinomio.Polinomio()
        polinomio1.agregar(1, 2)
        polinomio1.agregar(2, 1)
        polinomio1.agregar(3, 0)
        polinomio2.agregar(1, 2)
        polinomio2.agregar(2, 1)
        polinomio2.agregar(3, 0)
        polinomio_resultante = polinomio1.suma(polinomio2)
        self.assertEqual(polinomio_resultante.evaluar(1), 12)
        self.assertEqual(polinomio_resultante.evaluar(2), 48)

    def test_resta(self):
        polinomio1 = TDA_Polinomio.Polinomio()
        polinomio2 = TDA_Polinomio.Polinomio()
        polinomio1.agregar(1, 2)
        polinomio1.agregar(2, 1)
        polinomio1.agregar(3, 0)
        polinomio2.agregar(1, 2)
        polinomio2.agregar(2, 1)
        polinomio2.agregar(3, 0)
        polinomio_resultante = polinomio1.resta(polinomio2)
        self.assertEqual(polinomio_resultante.evaluar(1), 0)
        self.assertEqual(polinomio_resultante.evaluar(2), 0)

    def test_multiplicacion(self):
        polinomio1 = TDA_Polinomio.Polinomio()
        polinomio2 = TDA_Polinomio.Polinomio()
        polinomio1.agregar(1, 2)
        polinomio1.agregar(2, 1)
        polinomio1.agregar(3, 0)
        polinomio2.agregar(1, 2)
        polinomio2.agregar(2, 1)
        polinomio2.agregar(3, 0)
        polinomio_resultante = polinomio1.multiplicacion(polinomio2)
        self.assertEqual(polinomio_resultante.evaluar(1), 36)
        self.assertEqual(polinomio_resultante.evaluar(2), 144)

    def test_dividir(self):
        polinomio1 = TDA_Polinomio.Polinomio()
        polinomio2 = TDA_Polinomio.Polinomio()
        polinomio1.agregar(1, 2)
        polinomio1.agregar(2, 1)
        polinomio1.agregar(3, 0)
        polinomio2.agregar(1, 2)
        polinomio2.agregar(2, 1)
        polinomio2.agregar(3, 0)
        polinomio_resultante = polinomio1.dividir(polinomio2)
        self.assertEqual(polinomio_resultante.evaluar(1), 1)
        self.assertEqual(polinomio_resultante.evaluar(2), 1)

    def test_evaluar(self):
        polinomio1 = TDA_Polinomio.Polinomio()
        polinomio1.agregar(1, 2)
        polinomio1.agregar(2, 1)
        polinomio1.agregar(3, 0)
        self.assertEqual(polinomio1.evaluar(1), 6)
        self.assertEqual(polinomio1.evaluar(2), 17)

    def test_derivada(self):
        polinomio1 = TDA_Polinomio.Polinomio()
        polinomio1.agregar(1, 2)
        polinomio1.agregar(2, 1)
        polinomio1.agregar(3, 0)
        polinomio_resultante = polinomio1.derivada()
        self.assertEqual(polinomio_resultante.evaluar(1), 4)
        self.assertEqual(polinomio_resultante.evaluar(2), 6)

    def test_integral(self):
        polinomio1 = TDA_Polinomio.Polinomio()
        polinomio1.agregar(1, 2)
        polinomio1.agregar(2, 1)
        polinomio1.agregar(3, 0)
        polinomio_resultante = polinomio1.integral()
        self.assertEqual(polinomio_resultante.evaluar(1), 1.5)
        self.assertEqual(polinomio_resultante.evaluar(2), 5.5)

if __name__ == '__main__':
    unittest.main()
    


