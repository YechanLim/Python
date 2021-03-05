class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        solution = ListNode()
        lastNode = solution
        addtionRound = 0

        while(l1 != None or l2 != None):
            val1 = 0
            val2 = 0
            newNode = ListNode()

            if(l1 != None):
                val1 = l1.val
                l1 = l1.next

            if(l2 != None):
                val2 = l2.val
                l2 = l2.next

            //이것보단 % / 로 하는게 더 깔끔할 거 같다.!
            if(val1 + val2 + addtionRound >= 10):
                newNode.val = val1 + val2 + addtionRound - 10
                addtionRound = 1
            else:
                newNode.val = val1 + val2 + addtionRound
                addtionRound = 0

            lastNode.next = newNode
            lastNode = newNode

        if(addtionRound == 1):
            newNode = ListNode(1,None)
            lastNode.next = newNode
            
        solution = solution.next
        return solution


        