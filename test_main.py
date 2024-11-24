import unittest
from main import Trithemius_encrypt, Trithemius_decrypt, validate_key

class TestTrithemiusCipher(unittest.TestCase):
    def setUp(self):
        self.ukrainian_alphabet = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
        self.english_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def test_validate_key_2d_vector(self):
        key = "3,4"
        result = validate_key(key, "2D-вектор")
        self.assertEqual(result, [3, 4])

    def test_validate_key_3d_vector(self):
        key = "1,2,3"
        result = validate_key(key, "3D-вектор")
        self.assertEqual(result, [1, 2, 3])

    def test_validate_key_keyword(self):
        key = "PASSWORD"
        result = validate_key(key, "Гасло")
        self.assertEqual(result, "PASSWORD")

    def test_invalid_2d_vector(self):
        key = "3,4,5"
        with self.assertRaises(ValueError):
            validate_key(key, "2D-вектор")

    def test_invalid_3d_vector(self):
        key = "3,4"
        with self.assertRaises(ValueError):
            validate_key(key, "3D-вектор")

    def test_invalid_keyword(self):
        key = ""
        with self.assertRaises(ValueError):
            validate_key(key, "Гасло")

if __name__ == "__main__":
    unittest.main()
