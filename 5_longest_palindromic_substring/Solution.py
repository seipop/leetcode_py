import re

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        searched = []
        palindromes = []

        for i in range(0, len(s)):
            if s[i] in searched:
                continue
            a1 = s[i]
            searched += a1
            p1 = format(r'%s' % a1)
            chars = list(re.finditer(p1, s))
            chars = map(lambda x: x.start(), chars)
            l = self.makeRange(chars)
            l = map(lambda x: [x[0], x[1] + 1], l)
            for p in l:
                if self.isPalindrome(s[p[0]: p[1]]) and s[p[0]: p[1]]:
                    palindromes.append(s[p[0]: p[1]])

        palindromes = list(set(palindromes))

        ml = max(len(pa) for pa in palindromes)
        longestPalindrome = list(lpa for lpa in palindromes if len(lpa) == ml)[0]

        return longestPalindrome

    def makeRange(self, l):
        """
        :type l: list
        :rtype: list
        """
        col = []
        l = list(set(l))
        l.sort()
        if not l:
            return []
        if len(l) == 1:
            return [[l[0], l[0]]]
        for i in range(0, len(l) - 1):
           for j in range(i + 1, len(l)):
               col.append([l[i], l[j]])
        return col


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
