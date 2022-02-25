# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        result_head = ListNode(0)
        result = result_head
        while list1 or list2:
            if list2 == None:
                result.next = ListNode(list1.val)
                result = result.next
                list1 = list1.next
            elif list1 == None:
                result.next = ListNode(list2.val)
                result = result.next
                list2 = list2.next
            elif list1.val < list2.val:
                result.next = ListNode(list1.val)
                result = result.next
                list1 = list1.next
            else:
                result.next = ListNode(list2.val)
                result = result.next
                list2 = list2.next
        
        return result_head.next
                
        