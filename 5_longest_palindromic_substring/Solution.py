import re

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        searched = []
        palindrome = ''

        if len(s) == 1 or self.isPalindrome(s):
            return s

        for i in range(0, len(s)):
            if s[i] in searched:
                continue
            a1 = s[i]
            searched += a1
            p1 = format(r'%s' % a1)
            chars = list(re.finditer(p1, s))
            chars = map(lambda x: x.start(), chars)

            if len(chars) == 1:
                palindrome = a1 if len(a1) > len(palindrome) else palindrome
                continue

            hasPalindrome = False
            for l in range(len(chars), 0, -1):
                for i in range(0, len(chars) - l):
                    substr = s[chars[i]: chars[i + l] + 1]
                    if len(substr) <= len(palindrome):
                        continue
                    elif self.isPalindrome(substr):
                        palindrome = substr
                        hasPalindrome = True
                if hasPalindrome:
                    break

        return palindrome

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: boolean
        """
        isPalindrome = True
        if not s:
            pass
        elif s[0] == s[-1]:
            isPalindrome = isPalindrome and self.isPalindrome(s[1:-1])
        else:
            isPalindrome = False
        return isPalindrome
