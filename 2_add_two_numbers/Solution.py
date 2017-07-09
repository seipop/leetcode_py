from ListNode import ListNode

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def addTwoNode(n1, n2, num):
            """
            :type n1: ListNode
            :type n2: ListNode
            :type num: Int
            :rtype: ListNode
            """
            if (not n1 and not n2):
                return None
            n1 = n1 if n1 else ListNode(0)
            n2 = n2 if n2 else ListNode(0)

            t = n1.var + n2.var + num
            n = t / 10
            r = ListNode(t % 10)
            if (n1.next or n2.next):
                r.next = addTwoNode(n1.next, n2.next, n)
            else:
                r.next = None if n == 0 else ListNode(1)
            return r

        return addTwoNode(l1, l2, 0)
