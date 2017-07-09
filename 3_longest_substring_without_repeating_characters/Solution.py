# Definition for singly-linked list.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = []
        total = 0
        for i in s:
            if i in l:
                n = l.index(i)
                l = l[(n+1): ]
            l.append(i)
            total = max(total, len(l))
        return total
