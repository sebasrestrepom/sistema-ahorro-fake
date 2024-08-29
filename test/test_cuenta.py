import unittest
from clases.cuenta import Cuenta
from clases.transaccion import Consignacion, Retiro

class TestCuenta(unittest.TestCase):
    def test_creacion_cuenta(self):
        cuenta = Cuenta("001", "Ahorros", "2024-08-27")
        self.assertEqual(cuenta.id_cuenta, "001")
        self.assertEqual(cuenta._tipo_cuenta, "Ahorros")
        self.assertEqual(cuenta._fecha_apertura, "2024-08-27")
        self.assertEqual(len(cuenta.transacciones), 0)

    def test_realizar_transaccion(self):
        cuenta = Cuenta("001", "Ahorros", "2024-08-27")
        transaccion = Consignacion("0001", "Consignación", 100000)
        cuenta.realizar_transaccion(transaccion)
        self.assertEqual(len(cuenta.transacciones), 1)
        self.assertEqual(cuenta.transacciones[0].id_transaccion, "0001")

if __name__ == "__main__":
    unittest.main()