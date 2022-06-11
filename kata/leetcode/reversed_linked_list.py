class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next_node

    def get_data(self):
        return self.val

    def get_next_node(self):
        return self.next_node

    def set_data(self, new_data):
        self.val = new_data

    def set_next_node(self, new):
        self.next_node = new


class Solution:

    def reverseList(self, head):
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

    pass
