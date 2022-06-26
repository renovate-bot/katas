from typing import List


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def init_list(self, data):
        self.head = ListNode(data[0])

        head = self.head
        p = self.head

        for i in data[1:]:
            node = ListNode(i)
            p.next_node = node
            p = p.next_node
        return head

    def print_list(self, head):
        p = head
        while p:
            print(p.val)
            p = p.next_node

    def push_in_list(self):
        result = []
        p = self.head
        while p:
            result.append(p.val)
            p = p.next_node
        return result


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self, vals: List):
        self.root = self.generate_tree(vals)

    @staticmethod
    def generate_tree(vals):
        if not len(vals):
            return None

        root = None
        queue = []

        fill_left = True

        for val in vals:
            node = TreeNode(val) if val else None

            if len(queue) == 0:
                root = node
                queue.append(node)
            elif fill_left:
                queue[0].left = node
                fill_left = False
                if node:
                    queue.append(node)
            else:
                queue[0].right = node
                if node:
                    queue.append(node)
                queue.pop(0)
                fill_left = True
        return root


def get_the_last_node(head):
    p = head
    while p.next_node:
        p = p.next_node
    return p


def map_linked_list_to_hash_table(head):
    p = head
    index = 0
    result = {}
    while p:
        result.update({index: p})
        p = p.next_node
        index += 1

    return result
