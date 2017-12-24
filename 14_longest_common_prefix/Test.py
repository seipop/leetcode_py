import unittest
from Solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testIsPalindrome(self):
        self.assertEqual(self.solution.longestCommonPrefix(['abcd', 'abce', 'abcf']), 'abc')

if __name__ == '__main__':
    unittest.main()
