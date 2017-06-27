# Definition for singly-linked list.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

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
