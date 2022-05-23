from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def init_list(self, data):
        self.head = ListNode(data[0])

        head = self.head
        p = self.head

        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return head

    def print_list(self):
        p = self.head
        while p:
            print(p.val)
            p = p.next


def find_larger(head):
    max_value = 0
    standard = head.val
    p = head
    while p:
        if p.val > standard and p.val > max_value:
            max_value = p.val
            return max_value
        p = p.next
    return max_value


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        h = head
        result = []
        while h:
            max_value = find_larger(h)
            result.append(max_value)
            h = h.next
        return result


if __name__ == "__main__":
    pass
