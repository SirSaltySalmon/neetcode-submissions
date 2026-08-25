# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(0)
        cur_node = head
        # Use a heap to efficiently get the smallest element from k lists
        import heapq
        heap = []
        for i, node in enumerate(lists): 
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        while heap:
            data = heapq.heappop(heap)
            next_node = data[2]
            if next_node.next:
                node_to_reappend = next_node.next
                heapq.heappush(heap, (node_to_reappend.val, data[1], node_to_reappend))
            
            cur_node.next = next_node
            cur_node = cur_node.next
        
        return head.next