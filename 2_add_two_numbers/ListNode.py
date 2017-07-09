# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.var = x
        self.next = None

    @staticmethod
    def makeListNodesFromNumber(num):
        """
        :type num: Int
        :rtype: ListNode
        """
        if num < 0:
            return None
        length = len(format("%d" % num)) - 1
        tnode = node = None
        while(length >= 0):
            n = num % 10
            num = num // 10
            length -= 1
            if not tnode:
                node = ListNode(n)
                tnode = node
            else:
                tnode.next = ListNode(n)
                tnode = tnode.next
        return node

    def isEqual(self, node):
        """
        :type node: ListNode
        :rtype: Bool
        """
        equal = True
        if self.var != node.var:
            equal = False
        if self.next and node.next:
            equal = equal and self.next.isEqual(node.next)
        elif self.next or node.next:
            equal = False
        return equal

    def toString(self):
        """
        :rtype: String
        """
        s = format("%d" % self.var)
        if self.next:
            s = self.next.toString() + s
        return s
