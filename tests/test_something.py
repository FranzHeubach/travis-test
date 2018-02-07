import unittest

class ExampleTestClass(unittest.TestCase):
    
    def setUp(self):
        self.var = 123
        
    def test_var(self):
        self.assertEqual(self.var, 123)
        
if __name__ == '__main__':
    unittest.main()
