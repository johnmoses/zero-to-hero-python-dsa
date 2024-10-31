203 Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Approach 1: Sentinel Node

Intuition

The problem seems to be very easy if one has to delete a node in the middle:

Pick the node-predecessor prev of the node to delete.

Set its next pointer to point to the node next to the one to delete

Algorithm

Initiate sentinel node as ListNode(0) and set it to be the new head: sentinel.next = head.

Initiate two pointers to track the current node and its predecessor: curr and prev.

While curr is not a null pointer:

Compare the value of the current node with the value to delete.

In the values are equal, delete the current node: prev.next = curr.next.

Otherwise, set predecessor to be equal to the current node.

Move to the next node: curr = curr.next.

Return sentinel.next.

11/23/2021 10:28