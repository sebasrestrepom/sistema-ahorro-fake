import unittest
from clases.transaccion import Transaccion, Consignacion, Retiro

class TestTransaccion(unittest.TestCase):
    def test_creacion_transaccion(self):
        transaccion = Transaccion("0001", "Genérica", 100000)
        self.assertEqual(transaccion.id_transaccion, "0001")
        self.assertEqual(transaccion.tipo_transaccion, "Genérica")
        self.assertEqual(transaccion.monto, 100000)

    def test_consignacion(self):
        consignacion = Consignacion("0002", "Consignación", 50000)
        self.assertEqual(consignacion.id_transaccion, "0002")
        self.assertEqual(consignacion.tipo_transaccion, "Consignación")
        self.assertEqual(consignacion.monto, 50000)

    def test_retiro(self):
        retiro = Retiro("0003", "Retiro", 20000)
        self.assertEqual(retiro.id_transaccion, "0003")
        self.assertEqual(retiro.tipo_transaccion, "Retiro")
        self.assertEqual(retiro.monto, 20000)

if __name__ == "__main__":
    unittest.main()