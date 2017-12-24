class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type s: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''

        longestPrefix = strs[0]
        for s in strs[1:]:
            l = len(longestPrefix)
            while (s[:l] != longestPrefix) and (l > 0):
                l = l - 1
                longestPrefix = longestPrefix[:l]

        return longestPrefix
