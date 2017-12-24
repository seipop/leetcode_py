R5 = ['V', 'L', 'D', '']
R10 = ['I', 'X', 'C', 'M']

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        count = 0

        while num > 0:
            c = num % 10
            c1 = c % 5
            c2 = c / 5
            r10 = R10[count]
            r5 = R5[count]

            if c1 > 3:
                if c2 > 0:
                    res = r10 + R10[count + 1] + res
                else:
                    res = r10 + r5 + res
            else:
                if c1 == 0 and c != 0:
                    res = r5 + res
                else:
                    res = r5 * c2 + r10 * c1 + res
            count += 1
            num = num / 10
        return res
