# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        ans = list1
        a_tail = list1
        b_tail = list1
        while a_tail and a>1:
            a_tail = a_tail.next
            a-=1
        while b_tail and b>-1:
            b_tail = b_tail.next
            b-=1

        a_tail.next = list2

        list2_tail = list2
        while list2_tail.next:
            list2_tail = list2_tail.next
        list2_tail.next = b_tail
        return ans 