class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head

        while fast and fast.next:
           slow = slow.next
           fast = fast.next.next
        
        second = slow.next

        prev = slow.next = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first, last = head, prev
        while last:
            nxt1, nxt2 = first.next, last.next
            first.next = last
            last.next = nxt1
            first, last = nxt1, nxt2

