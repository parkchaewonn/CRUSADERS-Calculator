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


if __name__ == "__main__":
    unittest.main()
