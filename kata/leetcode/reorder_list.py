import math

from kata.leetcode.common import LinkedList


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next_node


def length_of_linked_list(node):
    count = 0
    while node:
        count += 1
        node = node.next_node
    return count


class Solution:
    def reorderList(self, head: ListNode) -> None:
        length_of_left_list = math.ceil(length_of_linked_list(head) / 2)
        p = head
        while length_of_left_list - 1 > 0:
            p = p.next_node
            length_of_left_list -= 1

        head_of_right_list, p.next_node = self.reverseList(p.next_node), None

        left, right = head, head_of_right_list
        while right:
            next_ele = right.next_node if right else None
            temp = left.next_node
            right.next_node, left.next_node = temp, right
            left, right = temp, next_ele

        return left

    @staticmethod
    def reverseList(head):
        if head is None or head.next_node is None:
            return head
        current = head
        pre = None
        while current:
            head = current
            tmp = current.next_node
            current.next_node = pre
            pre = current
            current = tmp
        return head


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.init_list(data=[1, 2, 3, 4])

    Solution().reorderList(linked_list.head)
