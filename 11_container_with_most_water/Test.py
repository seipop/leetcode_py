import unittest
from Solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testIsPalindrome(self):
        self.assertEqual(self.solution.maxArea([1,2,3]), 2)

if __name__ == '__main__':
    unittest.main()
