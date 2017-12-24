ROMAN = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0

        while len(s):
            ss = s[-1]
            num = ROMAN[ss]
            total += num
            if len(s) > 1 and ROMAN[s[-2]] < num:
                total -= ROMAN[s[-2]]
                s = s[:-2]
            else:
                s = s[:-1]

        return total
