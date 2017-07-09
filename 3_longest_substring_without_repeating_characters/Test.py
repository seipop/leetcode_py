import unittest
from Solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testLengthOfLongestSubstring(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(self.solution.lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(self.solution.lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(self.solution.lengthOfLongestSubstring("aab"), 2)
        self.assertEqual(self.solution.lengthOfLongestSubstring("dvdf"), 3)

if __name__ == '__main__':
    unittest.main()
