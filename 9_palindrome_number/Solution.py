class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        sx = str(x)
        l = len(sx)
        if (l % 2):
            a1 = l / 2
            a2 = l / 2
        else:
            a1 = l / 2
            a2 = l / 2 - 1
        for c in range(a1, l):
            if sx[a1] != sx[a2]:
                return False
            a1 += 1
            a2 -= 1
        return True
