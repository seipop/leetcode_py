import unittest
from Solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testIsPalindrome(self):
        self.assertEqual(self.solution.isPalindrome(123), False)
        self.assertEqual(self.solution.isPalindrome(313), True)
        self.assertEqual(self.solution.isPalindrome(444433313334444), True)
        self.assertEqual(self.solution.isPalindrome(-444433313334444), False)

if __name__ == '__main__':
    unittest.main()
