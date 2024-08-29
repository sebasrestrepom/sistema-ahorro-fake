import unittest
from clases.persona import Persona

class TestPersona(unittest.TestCase):
    def test_creacion_persona(self):
        persona = Persona("123456789", "Juan Perez", 30)
        self.assertEqual(persona._identificacion, "123456789")
        self.assertEqual(persona._nombres, "Juan Perez")
        self.assertEqual(persona._edad, 30)

if __name__ == "__main__":
    unittest.main()