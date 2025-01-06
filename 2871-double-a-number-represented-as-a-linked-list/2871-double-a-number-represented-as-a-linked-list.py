# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val==0 or not head:
            return head
        dummy = head
        lst = []
        while dummy:
            lst.append(dummy.val)
            dummy = dummy.next
        ans = 0
        for i in range(len(lst)):
            ans = ans*10 + lst[i]
        ans *= 2
        sol = ListNode(-1)
        tail = sol
        lst = []
        d = ans
        l = 0
        while d:
            l+=1
            d//=10
        for i in range(l):
            lst.append(ans%10)
            ans//=10
        lst = lst[::-1]
        for i in range(l):
            tail.next = ListNode(lst[i])
            tail = tail.next
        return sol.next