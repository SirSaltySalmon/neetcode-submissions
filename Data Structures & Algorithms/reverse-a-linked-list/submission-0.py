# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curNode = head
        prevNode = None

        while not curNode is None:
            temp = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = temp
        
        return prevNode if not prevNode is None else curNode