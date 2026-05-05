# Solution

'''''
Approach


Handle edge case: If the list is empty, return it.
Find the length and tail:
Traverse the list to count nodes.
Keep a pointer (dummy) to the last node.
Normalize k:
position = k % length
If position == 0, no rotation is needed.
Find new tail:
The new tail is at index length - position - 1.
Rearrange pointers:
Let new_head = current.next
Break the list: current.next = None
Connect old tail to old head: dummy.next = head
'''


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        length = 1
        dummy = head

        while dummy.next:
            dummy = dummy.next
            length += 1
        
        position = k % length
        if position == 0:
            return head
        
        current = head

        for _ in range(length - position - 1):
            current = current.next
        
        new_head = current.next
        current.next = None
        dummy.next = head

        return new_head