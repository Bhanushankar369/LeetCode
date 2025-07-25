# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(-1)
        dummy = res
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = ListNode(list1.val)
                dummy = dummy.next
                list1 = list1.next
            elif list1.val > list2.val:
                dummy.next = ListNode(list2.val)
                dummy = dummy.next
                list2 = list2.next
            else:
                dummy.next = ListNode(list1.val)
                dummy = dummy.next
                list1 = list1.next

        if list1:
            dummy.next = list1

        if list2:
            dummy.next = list2

        return res.next