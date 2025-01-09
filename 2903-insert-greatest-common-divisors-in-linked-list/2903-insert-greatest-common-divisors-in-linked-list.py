# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        dummy = head
        while dummy:
            lst.append(dummy.val)
            dummy = dummy.next
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a
        gcd_lst = []
        for i in range(len(lst)-1):
            gcd_lst.append(gcd(lst[i], lst[i+1]))
        k=0
        print(gcd_lst)
        l=1
        while k<len(gcd_lst):
            lst.insert(l, gcd_lst[k])
            k+=1
            l+=2
            print(i)
        ans = ListNode(-1)
        tail = ans
        for i in lst:
            tail.next = ListNode(i)
            tail = tail.next
        return ans.next