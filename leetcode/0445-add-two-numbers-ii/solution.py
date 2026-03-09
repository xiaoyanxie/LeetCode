# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def toStack(node):
            """
            7->2->4->3
                     ^
            
            stack: [7, 2, 4, 3]
            """
            stack = []
            while node:
                stack.append(node.val)
                node = node.next
            return stack
        
        def addNumbers(stack1, stack2) -> ListNode:
            """
            [7, 2, 4, 3]
               [5, 6, 4]
             ^

            carry = 0
            curr,      nxt
            node(7) -> node(8) -> node(0) -> node(7) -> None
            """
            carry = 0
            curr, nxt = None, None
            while stack1 or stack2:
                digit = 0
                if stack1 and stack2:
                    digit = stack1.pop() + stack2.pop() + carry
                elif stack1:
                    digit = stack1.pop() + carry
                else:
                    digit = stack2.pop() + carry
                
                if digit >= 10:
                    carry = 1
                    digit -= 10
                else:
                    carry = 0
                
                nxt = curr
                curr = ListNode(digit, nxt)
            
            if carry == 1:
                nxt = curr
                curr = ListNode(1, nxt)

            return curr
        
        stack1 = toStack(l1)
        stack2 = toStack(l2)
        return addNumbers(stack1, stack2)
