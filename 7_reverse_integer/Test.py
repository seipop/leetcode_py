import unittest
from Solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testReverseInteger(self):
        self.assertEqual(self.solution.reverse(123), 321)
        self.assertEqual(self.solution.reverse(-123), -321)
        self.assertEqual(self.solution.reverse(120), 21)
        self.assertEqual(self.solution.reverse(1200), 21)
        self.assertEqual(self.solution.reverse(0), 0)
        self.assertEqual(self.solution.reverse(00), 0)
        self.assertEqual(self.solution.reverse(1534236469), 0)
        self.assertEqual(self.solution.reverse(-2147483412), -2143847412)
        self.assertEqual(self.solution.reverse(1463847412), 2147483641)

if __name__ == '__main__':
    unittest.main()
