from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        linked_list_hash = {}
        p = head
        index = 0
        while p:
            if p in linked_list_hash.values():
                return True
            else:
                linked_list_hash.update({index: p})
                p = p.next
                index += 1

        return False
