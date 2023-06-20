
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
        Return the list in ascending order
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

    # 160. Intersection of Two Linked Lists

    def getIntersectionNode(headA: ListNode, headB: ListNode):
        """
        Given the heads of two singly linked-lists headA and headB, 
        return the node at which the two lists intersect. 
        If the two linked lists have no intersection at all, return null.
        """
        lenA = 0
        lenB = 0
        nodeA, nodeB = headA, headB
        # get length of both lists
        while nodeA:
            lenA+=1
            nodeA = nodeA.next
        while nodeB:
            lenB += 1
            nodeB = nodeB.next
        # get the difference of the lists
        diff = abs(lenA-lenB)

        #start the lists at the same time
        if lenA > lenB:
            while diff > 0:
                headA = headA.next
                diff-=1
        else:
            while diff > 0:
                headB = headB.next
                diff-=1
        #walk through linked lists in parallel to find where they are equal
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
    
    # 206. Reverse Linked List

    def reverseListIterative(self, head):
        """ 
        Given the head of a singly linked list, reverse the list, and return the reversed list.
        This is the iterative solution
        """
        newList = None
        curr = head
        while curr:
            nextNode = curr.next
            curr.next = newList
            newList = curr
            curr = nextNode
        return newList
    
    def reverseListRecursive(self, head):
        """ 
        Given the head of a singly linked list, reverse the list, and return the reversed list.
        This is the recursive solution
        """
        if head == None:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseListRecursive(head.next)
            head.next.next = head
        head.next = None
        return newHead











