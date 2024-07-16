# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy_head = ListNode()
        temp = dummy_head
                
        while l1 or l2 or carry:
            first = 0
            seccound = 0
            sum = carry
            # print(l1.val)
            # print(l2.val)
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            temp.next = ListNode(sum%10)
            temp = temp.next
            carry = sum//10
        return  dummy_head.next