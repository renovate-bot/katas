from kata.leetcode.common import ListNode, LinkedList


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head and head.next_node:
            slow = head.next_node
            fast = head.next_node.next_node
        else:
            return None

        while fast:
            if fast != slow:

                if fast.next_node:
                    fast = fast.next_node.next_node
                else:
                    return None
            else:
                pass


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.init_list(data=[1])
    Solution().detectCycle(linked_list.head)
