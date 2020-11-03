# 1290. Convert Binary Number in a Linked List to Integer
#
# Solution
# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
#
# Return the decimal value of the number in the linked list.
#
# Example 1:
#
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10
# Example 2:
#
# Input: head = [0]
# Output: 0
# Example 3:
#
# Input: head = [1]
# Output: 1
# Example 4:
#
# Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
# Output: 18880
# Example 5:
#
# Input: head = [0,0]
# Output: 0
#
#
# Constraints:
#
# The Linked List is not empty.
# Number of nodes will not exceed 30.
# Each node's value is either 0 or 1.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue_Method1(self, head: ListNode) -> int: #submitted

        decimal = 0
        while head != None:
            binary = head.val
            decimal = 2*decimal + binary
            head = head.next
        return decimal

    def getDecimalValue_Method2(self, head: ListNode) -> int:

        current = head
        binary = ""
        while current != None:
            binary = binary + str(current.val)
            current = current.next

        power, decimal = 0, 0
        binary = int(binary)

        while binary > 0:
            mod = binary % 10
            binary = binary // 10
            decimal = decimal + (mod * pow(2, power))
            power += 1

        return decimal

head = ListNode()
head.val = 1
node1 = ListNode()
node1.val = 0
node2 = ListNode()
node2.val = 0
node3 = ListNode()
node3.val = 1

head.next = node1
node1.next = node2
node2.next = node3
#1001
obj = Solution()
print("Decimal using method 1:", obj.getDecimalValue_Method1(head))
print("Decimal using method 2:", obj.getDecimalValue_Method2(head))
