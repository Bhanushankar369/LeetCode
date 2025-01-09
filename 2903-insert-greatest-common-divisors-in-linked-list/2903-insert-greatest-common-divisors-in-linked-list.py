# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        second = head.next

        while second:
            new_Node = ListNode(gcd(first.val, second.val))
            first.next = new_Node
            new_Node.next = second

            first = second
            second = second.next
        return head