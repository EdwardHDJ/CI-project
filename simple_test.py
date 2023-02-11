import unittest
import simple_code

class TestSimpleCode(unittest.TestCase):
    def test_simple_code(self):
            self.assertEqual(simple_code.simple_function(),1)
            
if __name__ == '__main__':
    unittest.main()
