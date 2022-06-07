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

    def print_list(self, head):
        p = head
        while p:
            print(p.val)
            p = p.next

    def push_in_list(self):
        result = []
        p = self.head
        while p:
            result.append(p.val)
            p = p.next
        return result


def get_the_last_node(head):
    p = head
    while p.next:
        p = p.next
    return p


def map_linked_list_to_hash_table(head):
    p = head
    index = 0
    result = {}
    while p:
        result.update({index: p})
        p = p.next
        index += 1

    return result
