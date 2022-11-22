import unittest
import xor_encoding

class TestEncoding(unittest.TestCase):

    def test_get_key(self):
        self.assertEqual(xor_encoding.get_key(), ';>+>=>,:/>,,(0-;')

    def test_str_xor(self):
        self.assertEqual(xor_encoding.encode_xor('ipconfig', ';>+>=>,:/>,,(0-;'), 'RNHQSXE]')

if __name__ == '__main__':
    unittest.main()
