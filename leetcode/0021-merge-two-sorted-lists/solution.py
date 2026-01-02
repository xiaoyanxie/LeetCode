# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy = ListNode(0)  
        # curr = dummy
        # while list1 and list2:
        #     if list1.val <= list2.val:
        #         curr.next = list1
        #         list1 = list1.next
        #         curr = curr.next
        #     else:
        #         curr.next = list2
        #         list2 = list2.next
        #         curr = curr.next
        # if list1:
        #     curr.next = list1
        # else:
        #     curr.next = list2
        # return dummy.next
        if not list1:
            return list2
        if not list2:
            return list1
            
        while list1 and list2:
            if list1.val <= list2.val:
                list1.next = self.mergeTwoLists(list1.next, list2)
                return list1
            else:
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2
                

# iterate over two linked list and merge them in non dereasing order. runtime complexity O(m + n), takes O(1) extra space



