import unittest
from Solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testIsPalindrome(self):
        self.assertTrue(self.solution.isPalindrome("bab"))
        self.assertTrue(self.solution.isPalindrome("baab"))
        self.assertTrue(self.solution.isPalindrome("bb"))
        self.assertTrue(self.solution.isPalindrome("a"))
        self.assertTrue(self.solution.isPalindrome("ababa"))

        self.assertFalse(self.solution.isPalindrome("baba"))
        self.assertFalse(self.solution.isPalindrome("bbaba"))
        self.assertFalse(self.solution.isPalindrome("aab"))
        self.assertFalse(self.solution.isPalindrome("ba"))
        self.assertFalse(self.solution.isPalindrome("ababaa"))

    def testMakeRange(self):
        self.assertEqual(self.solution.makeRange([0, 1]), [[0, 1]])
        self.assertEqual(self.solution.makeRange([1, 0]), [[0, 1]])
        self.assertEqual(self.solution.makeRange([0]), [[0, 0]])
        self.assertEqual(self.solution.makeRange([1, 1]), [[1, 1]])
        self.assertEqual(self.solution.makeRange([0, 1, 2]), [[0, 1], [0, 2], [1, 2]])
        self.assertEqual(self.solution.makeRange([1, 0, 2]), [[0, 1], [0, 2], [1, 2]])
        self.assertEqual(self.solution.makeRange([1, 2, 3, 4]), [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])
        self.assertEqual(self.solution.makeRange([4, 2, 3, 1]), [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])
        self.assertEqual(self.solution.makeRange([4, 3, 3, 4]), [[3, 4]])
        self.assertEqual(self.solution.makeRange([12, 16]), [[12, 16]])

    def testLongestPalindrome(self):
        self.assertEqual(self.solution.longestPalindrome("babad"), "aba")
        self.assertEqual(self.solution.longestPalindrome("cbbd"), "bb")
        self.assertEqual(self.solution.longestPalindrome("sacbbdbbcaj"), "acbbdbbca")
        self.assertEqual(self.solution.longestPalindrome("aaaaa"), "aaaaa")
        self.assertEqual(self.solution.longestPalindrome("a"), "a")
        self.assertEqual(self.solution.longestPalindrome("jrjnbctoqgzimtoklkxcknwmhiztomaofwwzjnhrijwkgmwwuazcowskjhitejnvtblqyepxispasrgvgzqlvrmvhxusiqqzzibcyhpnruhrgbzsmlsuacwptmzxuewnjzmwxbdzqyvsjzxiecsnkdibudtvthzlizralpaowsbakzconeuwwpsqynaxqmgngzpovauxsqgypinywwtmekzhhlzaeatbzryreuttgwfqmmpeywtvpssznkwhzuqewuqtfuflttjcxrhwexvtxjihunpywerkktbvlsyomkxuwrqqmbmzjbfytdddnkasmdyukawrzrnhdmaefzltddipcrhuchvdcoegamlfifzistnplqabtazunlelslicrkuuhosoyduhootlwsbtxautewkvnvlbtixkmxhngidxecehslqjpcdrtlqswmyghmwlttjecvbueswsixoxmymcepbmuwtzanmvujmalyghzkvtoxynyusbpzpolaplsgrunpfgdbbtvtkahqmmlbxzcfznvhxsiytlsxmmtqiudyjlnbkzvtbqdsknsrknsykqzucevgmmcoanilsyyklpbxqosoquolvytefhvozwtwcrmbnyijbammlzrgalrymyfpysbqpjwzirsfknnyseiujadovngogvptphuyzkrwgjqwdhtvgxnmxuheofplizpxijfytfabx"), "qosoq")
        self.assertEqual(self.solution.longestPalindrome("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"), "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa")

if __name__ == '__main__':
    unittest.main()
