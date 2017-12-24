import unittest
from Solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testIsPalindrome(self):
        self.assertEqual(self.solution.intToRoman(1), 'I')
        self.assertEqual(self.solution.intToRoman(2), 'II')
        self.assertEqual(self.solution.intToRoman(3), 'III')
        self.assertEqual(self.solution.intToRoman(4), 'IV')
        self.assertEqual(self.solution.intToRoman(5), 'V')
        self.assertEqual(self.solution.intToRoman(6), 'VI')
        self.assertEqual(self.solution.intToRoman(7), 'VII')
        self.assertEqual(self.solution.intToRoman(8), 'VIII')
        self.assertEqual(self.solution.intToRoman(9), 'IX')
        self.assertEqual(self.solution.intToRoman(10), 'X')
        self.assertEqual(self.solution.intToRoman(11), 'XI')
        self.assertEqual(self.solution.intToRoman(20), 'XX')
        self.assertEqual(self.solution.intToRoman(45), 'XLV')
        self.assertEqual(self.solution.intToRoman(50), 'L')
        self.assertEqual(self.solution.intToRoman(101), 'CI')
        self.assertEqual(self.solution.intToRoman(505), 'DV')
        self.assertEqual(self.solution.intToRoman(1000), 'M')

if __name__ == '__main__':
    unittest.main()
