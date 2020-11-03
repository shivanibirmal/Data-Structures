# Sort a linked list using insertion sort.
#
#
# A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
# With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
#
#
# Algorithm of Insertion Sort:
#
# Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
# It repeats until no input elements remain.
#
# Example 1:
#
# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:
#
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        current = head
        while current:
            curr_next = current.next
            prev, nxt = dummy, dummy.next
            while nxt:
                if nxt.val > current.val: break
                prev = nxt
                nxt = nxt.next

            current.next = nxt
            prev.next = current
            current = curr_next

        return dummy.next

head = ListNode()
head.val = 5
node1 = ListNode()
node1.val = 4
node2 = ListNode()
node2.val = 3
node3 = ListNode()
node3.val = 2

head.next = node1
node1.next = node2
node2.next = node3

obj = Solution()
print("Given list")
curr = head
while curr != None:
    print(curr.val, end = " ")
    curr = curr.next

result = obj.insertionSortList(head)

print("\nSorted list")
while result != None:
    print(result.val, end = " ")
    result = result.next
