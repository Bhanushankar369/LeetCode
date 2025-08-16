# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        dummy = head

        while dummy:
            lst.append(dummy.val)
            dummy = dummy.next

        val = -101
        res = []

        for i in range(len(lst)):
            if val != lst[i]:
                res.append(lst[i])
                val = lst[i]

        ans = ListNode(-1)
        node = ans

        for i in range(len(res)):
            node.next = ListNode(res[i])
            node = node.next

        return ans.next
