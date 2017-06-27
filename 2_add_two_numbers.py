# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.var = x
        self.next = None

def printf(x):
        print("%d -> " % x.var),
        if x.next:
            printf(x.next)
        else:
            print("")

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


if __name__ == '__main__':
    solution = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    r = solution.addTwoNumbers(l1, l2)
    printf(r)
    l1 = ListNode(5)
    r = solution.addTwoNumbers(l1, l1)
    printf(r)
    l1 = ListNode(1)
    l1.next = ListNode(8)
    l1.next.next = ListNode(9)
    l2 = ListNode(0)
    r = solution.addTwoNumbers(l1, l2)
    printf(r)
