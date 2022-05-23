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


def find_larger(lst):
    max_value = 0
    standard = lst[0]
    for i in lst[1:]:
        if i > standard and i > max_value:
            return i
    return max_value


class Solution:
    def __init__(self):
        self.head = None

    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        self.head = head
        result = []
        val_in_list = self.push_in_list()
        while len(val_in_list):
            result.append(find_larger(val_in_list))
            val_in_list.pop(0)

        return result

    def push_in_list(self):
        result = []
        p = self.head
        while p:
            result.append(p.val)
            p = p.next
        return result


if __name__ == "__main__":
    pass
