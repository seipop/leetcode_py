class Solution(object):
    def __init__(self):
        self.maxLen = 0
        self.startPosition = 0

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(0, len(s)):
            self.findPalindrome(s, i, i)
            self.findPalindrome(s, i, i + 1)

        palindrome = s[self.startPosition: self.startPosition + self.maxLen]

        self.startPosition = 0
        self.maxLen = 0

        return palindrome


    def findPalindrome(self, s, left, right):
        """
        :type s: str
        :type center: int
        :type lift: int
        :type right: int
        :rtype: boolean
        """
        flag = False
        while left >= 0 and right < len(s) and (s[left] == s[right]):
            left -= 1
            right += 1
            flag = True

        if flag:
            left += 1
            right -= 1
        else:
            right -= 1

        if self.maxLen <= (right - left + 1):
            self.maxLen = right - left + 1
            self.startPosition = left

        return [left, right]
