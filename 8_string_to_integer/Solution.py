INT_MAX = 2147483647
INT_MIN = -2147483648

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        res = "0"
        try:
            if str[0] == '+' or str[0] == '-':
                res = str[0] + res
                str = str[1:]
        except:
                return 0

        for i in str:
            try:
                a = int(i)
                res += i
            except:
                break

        ires = int(res)
        if ires > 0:
            res = INT_MAX if ires > INT_MAX else ires
        else:
            res = INT_MIN if ires < INT_MIN else ires
        return int(res)
