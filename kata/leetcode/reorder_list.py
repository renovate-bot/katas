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
        # 1. divide it into two linked list
        p = head
        while length_of_left_list - 1 > 0:
            p = p.next_node
            length_of_left_list -= 1

        head_of_right_list = p.next_node
        p.next_node = None

        # 2. revert second linked list
        head_of_right_list = self.reverseList(head_of_right_list)

        # 3. insert each ele
        p = head
        q = head_of_right_list
        while q:
            temp = p.next_node
            if q:
                next_ele = q.next_node
            else:
                next_ele = None
            q.next_node = temp
            p.next_node = q

            p = temp
            q = next_ele

        return p

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
