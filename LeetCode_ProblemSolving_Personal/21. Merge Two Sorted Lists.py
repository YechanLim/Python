# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        solution = ListNode()
        lastNode = solution
        

        while(l1 != None or l2 != None):
            newNode = ListNode()

            if(l1 == None):
                newNode.val = l2.val
                l2 = l2.next    
            elif(l2 == None):
                newNode.val = l1.val
                l1 = l1.next
            else:
                if(l1.val <= l2.val):
                    newNode.val = l1.val
                    l1 = l1.next
                else:
                    newNode.val = l2.val
                    l2 = l2.next

            lastNode.next = newNode
            lastNode = newNode

        return solution.next
