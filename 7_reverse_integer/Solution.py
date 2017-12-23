class Solution(object):
    def reverse(self, x):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        max = 2**31 - 1

        if abs(x) > max:
            return 0

        if x < 0:
            res = int(str(x)[:0:-1]) * -1
        else:
            res = int(str(x)[::-1])

        if abs(res) > max:
            return 0

        return res
