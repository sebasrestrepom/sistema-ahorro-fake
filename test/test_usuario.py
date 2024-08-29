import unittest
from clases.usuario import Usuario
from clases.cuenta import Cuenta

class TestUsuario(unittest.TestCase):
    def test_creacion_usuario(self):
        usuario = Usuario("123456789", "Juan Perez", 30)
        self.assertEqual(usuario._identificacion, "123456789")
        self.assertEqual(usuario._nombres, "Juan Perez")
        self.assertEqual(usuario._edad, 30)
        self.assertEqual(len(usuario.cuentas), 0)

    def test_asociar_cuenta(self):
        usuario = Usuario("123456789", "Juan Perez", 30)
        cuenta = Cuenta("001", "Ahorros", "2024-08-27")
        usuario.asociar_cuenta(cuenta)
        self.assertEqual(len(usuario.cuentas), 1)
        self.assertEqual(usuario.cuentas[0].id_cuenta, "001")

if __name__ == "__main__":
    unittest.main()