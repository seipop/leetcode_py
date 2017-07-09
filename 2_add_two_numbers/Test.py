import unittest
from Solution import Solution
from ListNode import ListNode

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testListNode(self):
        t = ListNode(0)
        tt = ListNode(0)
        self.assertTrue(t.isEqual(tt))
        self.assertTrue(tt.isEqual(t))

        t = ListNode(1)
        tt = ListNode(1)
        self.assertTrue(t.isEqual(tt))
        self.assertTrue(tt.isEqual(t))

        t = ListNode(0)
        tt = ListNode(1)
        self.assertFalse(t.isEqual(tt))
        self.assertFalse(tt.isEqual(t))

        t = ListNode(0)
        t.next = ListNode(0)
        t.next.next = ListNode(0)
        tt = ListNode(0)
        tt.next = ListNode(0)
        tt.next.next = ListNode(0)
        self.assertTrue(t.isEqual(tt))
        self.assertTrue(tt.isEqual(t))

        t = ListNode(0)
        t.next = ListNode(1)
        t.next.next = ListNode(2)
        tt = ListNode(0)
        tt.next = ListNode(1)
        tt.next.next = ListNode(2)
        self.assertTrue(t.isEqual(tt))
        self.assertTrue(tt.isEqual(t))

        t = ListNode(0)
        t.next = ListNode(1)
        t.next.next = ListNode(2)
        tt = ListNode(1)
        tt.next = ListNode(2)
        tt.next.next = ListNode(0)
        self.assertFalse(t.isEqual(tt))
        self.assertFalse(tt.isEqual(t))

        t = ListNode(0)
        t.next = ListNode(1)
        t.next.next = ListNode(2)
        tt = ListNode(0)
        tt.next = ListNode(1)
        tt.next.next = ListNode(0)
        self.assertFalse(t.isEqual(tt))
        self.assertFalse(tt.isEqual(t))

        t = ListNode(0)
        t.next = ListNode(1)
        t.next.next = ListNode(2)
        tt = ListNode(1)
        tt.next = ListNode(1)
        tt.next.next = ListNode(2)
        self.assertFalse(t.isEqual(tt))
        self.assertFalse(tt.isEqual(t))

        t = ListNode(0)
        t.next = ListNode(0)
        t.next.next = ListNode(0)
        tt = ListNode(0)
        tt.next = ListNode(0)
        self.assertFalse(t.isEqual(tt))
        self.assertFalse(tt.isEqual(t))

        t = ListNode(1)
        t.next = ListNode(2)
        t.next.next = ListNode(3)
        tt = ListNode(1)
        tt.next = ListNode(2)
        self.assertFalse(t.isEqual(tt))
        self.assertFalse(tt.isEqual(t))

    def testMakeListNodesFromNumber(self):
        t = ListNode(0)
        tt = ListNode.makeListNodesFromNumber(0)
        self.assertTrue(t.isEqual(tt))

        t = ListNode(0)
        tt = ListNode.makeListNodesFromNumber(1)
        self.assertFalse(t.isEqual(tt))

        t = ListNode(1)
        t.next = ListNode(0)
        t.next.next = ListNode(1)
        tt = ListNode.makeListNodesFromNumber(101)
        self.assertTrue(t.isEqual(tt))

        t = ListNode(4)
        t.next = ListNode(5)
        t.next.next = ListNode(6)
        tt = ListNode.makeListNodesFromNumber(654)
        self.assertTrue(t.isEqual(tt))

        t = ListNode(1)
        t.next = ListNode(2)
        t.next.next = ListNode(3)
        t.next.next.next = ListNode(4)
        tt = ListNode.makeListNodesFromNumber(4321)
        self.assertTrue(t.isEqual(tt))

        t = ListNode(9)
        t.next = ListNode(9)
        t.next.next = ListNode(9)
        tt = ListNode.makeListNodesFromNumber(999)
        self.assertTrue(t.isEqual(tt))

    def testListNodeToString(self):
        t = ListNode(0)
        self.assertEqual(t.toString(), '0')

        t = ListNode(1)
        self.assertEqual(t.toString(), '1')

        t = ListNode(1)
        t.next = ListNode(2)
        t.next.next = ListNode(3)
        self.assertEqual(t.toString(), '321')

    def testAddTwoNumbers(self):
        l1 = ListNode.makeListNodesFromNumber(243)
        l2 = ListNode.makeListNodesFromNumber(564)
        r1 = ListNode.makeListNodesFromNumber(243 + 564)
        r2 = self.solution.addTwoNumbers(l1, l2)
        self.assertTrue(r1.isEqual(r2))

        l1 = ListNode.makeListNodesFromNumber(5)
        l2 = ListNode.makeListNodesFromNumber(5)
        r1 = ListNode.makeListNodesFromNumber(5 + 5)
        r2 = self.solution.addTwoNumbers(l1, l2)
        self.assertTrue(r1.isEqual(r2))

        l1 = ListNode.makeListNodesFromNumber(189)
        l2 = ListNode.makeListNodesFromNumber(0)
        r1 = ListNode.makeListNodesFromNumber(189 + 0)
        r2 = self.solution.addTwoNumbers(l1, l2)
        self.assertTrue(r1.isEqual(r2))

        l1 = ListNode.makeListNodesFromNumber(588)
        l2 = ListNode.makeListNodesFromNumber(564)
        r1 = ListNode.makeListNodesFromNumber(588 + 564)
        r2 = self.solution.addTwoNumbers(l1, l2)
        self.assertTrue(r1.isEqual(r2))

if __name__ == '__main__':
    unittest.main()
