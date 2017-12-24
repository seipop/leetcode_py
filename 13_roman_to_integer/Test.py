import unittest
from Solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testIsPalindrome(self):
        self.assertEqual(self.solution.romanToInt('I'), 1)
        self.assertEqual(self.solution.romanToInt('II'), 2)
        self.assertEqual(self.solution.romanToInt('III'), 3)
        self.assertEqual(self.solution.romanToInt('IV'), 4)
        self.assertEqual(self.solution.romanToInt('V'), 5)
        self.assertEqual(self.solution.romanToInt('VI'), 6)
        self.assertEqual(self.solution.romanToInt('VII'), 7)
        self.assertEqual(self.solution.romanToInt('VIII'), 8)
        self.assertEqual(self.solution.romanToInt('IX'), 9)
        self.assertEqual(self.solution.romanToInt('X'), 10)
        self.assertEqual(self.solution.romanToInt('XX'), 20)
        self.assertEqual(self.solution.romanToInt('DV'), 505)

if __name__ == '__main__':
    unittest.main()
