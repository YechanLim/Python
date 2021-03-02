class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        solution = ListNode()
        addtionRound = 0

        while(l1 != None or l2 != None):
            val1 = 0
            val2 = 0

            if(l1 != None):
                val1 = l1.val
                l1 = l1.next

            if(l2 != None):
                val2 = l2.val
                l2 = l2.next

            if(val1 + val2 + addtionRound >= 10):
                solution.val = val1 + val2 + addtionRound - 10
                addtionRound = 1
            else:
                solution.val = val1 + val2 + addtionRound
                addtionRound = 0

            solution.next = next

        return solution


        