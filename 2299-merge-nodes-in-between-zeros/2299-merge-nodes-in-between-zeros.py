# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        dummy = head
        while dummy:
            lst.append(dummy.val)
            dummy = dummy.next
        sums = []
        current_sum = 0
        inside_segment = False

        for num in lst:
            if num == 0:
                if inside_segment:
                    sums.append(current_sum)
                    current_sum = 0
                inside_segment = True
            else:
                if inside_segment:
                    current_sum += num
        dummy = ListNode(-1)
        tail = dummy
        for i in sums:
            tail.next = ListNode(i)
            tail = tail.next
        return dummy.next