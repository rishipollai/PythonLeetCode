# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head
        cur1 = l1
        cur2= l2
        while cur1 and cur2:
            if(cur1.val < cur2.val):
                cur.next=cur1
                cur=cur.next
                cur1=cur1.next
            else:
                cur.next=cur2
                cur=cur.next
                cur2=cur2.next
        
        if cur1:
            cur.next=cur1
        if cur2:
            cur.next=cur2
        
        return head.next
            
        
