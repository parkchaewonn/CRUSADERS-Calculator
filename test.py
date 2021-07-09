import unittest
from test_logic import LogicTest as Logic

class Test(unittest.TestCase):

    def test_0(self):
        g = Logic()
        g.input = "1 + 1"
        self.assertEqual(g.Calculate(), 2 )

    def test_1(self):
        g = Logic()
        g.input = "1 / 1"
        self.assertEqual(g.Calculate(), 1 )

    def test_2(self):
        g = Logic()
        g.input = "2 / 1"
        self.assertEqual(g.Calculate(), 2)

    def test_3(self):
        g = Logic()
        g.input = "2 + 2 + 2"
        self.assertEqual(g.Calculate(), 6)

    def test_4(self):
        g = Logic()
        g.input = "2 - 5 "
        self.assertEqual(g.Calculate(), -3)

    def test_5(self):
        g = Logic()
        g.input = "1 + 1 + 1"
        self.assertEqual(g.Calculate(), 3)

    def test_6(self):
        g = Logic()
        g.input = "5"
        self.assertEqual(g.Calculate(), 5)

    def test_7(self):
        g = Logic()
        g.input = "5 * 5"
        self.assertEqual(g.Calculate(), 25)

    def test_8(self):
        g = Logic()
        g.input = "6 - 3"
        self.assertEqual(g.Calculate(), 3)

    def test_9(self):
        g = Logic()
        g.input = "5 - 5 - 5"
        self.assertEqual(g.Calculate(), -5)

    def test_10(self):
        g = Logic()
        g.input = "5 / 0"
        self.assertEqual(g.Calculate(), "Zero Division Error")

    def test_11(self):
        g = Logic()
        g.input = "+ - 5765 * 74 - / 84"
        self.assertEqual(g.Calculate(), "Syntax Error")

    def test_12(self):
        g = Logic()
        g.input = "49 + 1 * 5"
        self.assertEqual(g.Calculate(), 54)

    def test_13(self):
        g = Logic()
        g.input = "5"
        self.assertEqual(g.Calculate(), 5)

    def test_14(self):
        g = Logic()
        g.input = "40 - 94 + 61"
        self.assertEqual(g.Calculate(), 7)
        
    def test_15(self):
        g = Logic()
        g.input = "50 + 5 / 5"
        self.assertEqual(g.Calculate(), 51.0)

if __name__ == "__main__":
    unittest.main()
