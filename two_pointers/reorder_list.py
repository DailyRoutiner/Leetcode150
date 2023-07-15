class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head

        # Step 1: Find the middle of the linked list
        while fast and fast.next:
           slow = slow.next         # middle
           fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None
        # Step 2: Reverse the second half of the linked list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # Step 3: Merge the first and reversed second half of the linked list
        first, last = head, prev
        while last:
            nxt1, nxt2 = first.next, last.next
            first.next = last
            last.next = nxt1
            first, last = nxt1, nxt2

