import unittest
from Solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testTwoSum(self):
        self.assertEqual(self.solution.twoSum([1, 2, 3], 3), [0, 1])
        self.assertEqual(self.solution.twoSum([1, 2, 3], 4), [0, 2])
        self.assertEqual(self.solution.twoSum([1, 2, 3], 5), [1, 2])

if __name__ == '__main__':
    unittest.main()
