import unittest
from Solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testMyAtoi(self):
        self.assertEqual(self.solution.myAtoi(''), 0)
        self.assertEqual(self.solution.myAtoi('0'), 0)
        self.assertEqual(self.solution.myAtoi('123'), 123)
        self.assertEqual(self.solution.myAtoi('1230'), 1230)
        self.assertEqual(self.solution.myAtoi('0123'), 123)
        self.assertEqual(self.solution.myAtoi('0a1b2c'), 0)
        self.assertEqual(self.solution.myAtoi('1a2b3c'), 1)
        self.assertEqual(self.solution.myAtoi('01a2b3c'), 1)
        self.assertEqual(self.solution.myAtoi('101a2b3c'), 101)
        self.assertEqual(self.solution.myAtoi('a10b2c'), 0)
        self.assertEqual(self.solution.myAtoi('abc123'), 0)
        self.assertEqual(self.solution.myAtoi('123@123'), 123)
        self.assertEqual(self.solution.myAtoi('+1'), 1)
        self.assertEqual(self.solution.myAtoi('++1'), 0)
        self.assertEqual(self.solution.myAtoi('-123'), -123)
        self.assertEqual(self.solution.myAtoi('    010'), 10)
        self.assertEqual(self.solution.myAtoi('2147483648'), 2147483647)
        self.assertEqual(self.solution.myAtoi('-2147483648'), -2147483648)

if __name__ == '__main__':
    unittest.main()
