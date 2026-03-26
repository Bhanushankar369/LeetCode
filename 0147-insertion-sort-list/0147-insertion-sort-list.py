# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        dummy = head
        while dummy:
            lst.append(dummy.val)
            dummy = dummy.next
        lst.sort()
        dummy = head
        for i in lst:
            dummy.val = i
            dummy = dummy.next
        return head
