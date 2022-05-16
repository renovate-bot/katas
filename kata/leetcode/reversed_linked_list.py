class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def get_data(self):
        return self.val

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.val = new_data

    def set_next(self, new_next):
        self.next = new_next


class Solution:

    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        current = head
        pre = None
        while current:
            head = current
            tmp = current.next
            current.next = pre
            pre = current
            current = tmp
        return head


if __name__ == "__main__":

    pass
