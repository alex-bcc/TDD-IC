import unittest
from app import valida
from app import multiplo
from app import bee_1143


class TestFatorial(unittest.TestCase):

    def test_valida(self):
        self.assertFalse(valida(-3.5))
        self.assertTrue(valida(3.5))
        self.assertFalse(valida(11.0))
        self.assertTrue(valida(10.0))

    def test_multiplo(self):
        self.assertTrue(multiplo(200))
        self.assertTrue(multiplo(100))

    def test_bee_1143(self):
        self.assertFalse(bee_1143(0), 1)

if __name__ == '__main__':
    unittest.main()
