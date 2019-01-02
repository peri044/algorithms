# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def get_single_digits(self, number):
        # str_digits = str(number).split("")
        # digits = [int(digit) for digit in digits]
        digits=[]
        while True:
            rem=number%10
            num = int(number/10)
            digits.append(rem)
            number=num
            if num==0: break
        return digits
    
    def get_digits(self, llist):
        
        digits = [str(llist.val)]
        next = llist.next
        while next is not None:
            digits.append(str(next.val))
            next = next.next
        return int((''.join(digits[::-1])))
               
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rev_l1 = self.get_digits(l1)
        rev_l2 = self.get_digits(l2)
        l3_val = rev_l1 + rev_l2
        print (l3_val)
        digits= self.get_single_digits(l3_val)
        ans=[]
        for val in digits:
            ans.append(ListNode(val))
        for i in range(len(digits)):
            if i!=len(digits)-1:
                ans[i].next = ans[i+1]
            else:
                ans[i].next = None
        return ans[0]
        
        
        
        