# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        cur_node = None
        while not list1 is None or not list2 is None:
            next_node = None
            #get the smaller out of the two or the next available
            if list2 is None or (not list1 is None and list1.val < list2.val):
                next_node = list1
                list1 = list1.next
            else:
                next_node = list2
                list2 = list2.next
            
            if head is None:
                head = next_node
                cur_node = head
            else:
                cur_node.next = next_node
                cur_node = cur_node.next
        
        return head
            
