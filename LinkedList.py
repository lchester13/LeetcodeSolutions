
"""Leetcode ListNode class for problems"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LeetCodeSolutions:

    #21. Merge Two Sorted Lists

    def mergeTwoLists(self, list1, list2):
        """ 
        Merge the two lists in a one sorted list. 
        The list should be made by splicing together the nodes of the first two lists
        """
        head = ListNode()
        current = head
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.nexts
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1: 
            current.next = list1
        else: 
            current.next = list2
        return head.next
    
    #141. Linked List Cycle

    def hasCycle(self, head) -> bool:
        """
        Given head, the head of a linked list, determine if the linked list has a cycle in it.
        This solution uses Floyd's Cycle Finding Algorithm that utilizies a slow pointer and a fast pointer
        """
        slowPointer, fastPointer = head, head
        while (slowPointer and fastPointer and fastPointer.next):
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
            if slowPointer == fastPointer:
                return True
        return False








