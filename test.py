import unittest
from logic import Logic

class Test(unittest.TestCase):
    def test_normal(self):
        g = Logic()
        g.input = "1+1"
        self.assertEqual(g.Calculate(), 2 )
    def test_(self):
        g = Logic()
        g.input = "1/1"
        self.assertEqual(g.Calculate(), 1 )
    def test_1(self):
        g = Logic()
        g.input = "2/1"
        self.assertEqual(g.Calculate(), 2)
    def test_5(self):
        g = Logic()
        g.input = "2+ 2+2"
        self.assertEqual(g.Calculate(), 6)
    def test_5312(self):
        g = Logic()
        g.input = "2 -5 "
        self.assertEqual(g.Calculate(), -3)

if __name__ == "__main__":
    unittest.main()
