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
            print l
            total = max(total, len(l))
        return total

if __name__ == '__main__':
    solution = Solution()
    r = solution.lengthOfLongestSubstring("abcabcbb")
    print r == 3
    print r
    r = solution.lengthOfLongestSubstring("bbbbb")
    print r == 1
    print r
    r = solution.lengthOfLongestSubstring("pwwkew")
    print r == 3
    print r
    r = solution.lengthOfLongestSubstring("aab")
    print r == 2
    print r
    r = solution.lengthOfLongestSubstring("dvdf")
    print r == 3
    print r
