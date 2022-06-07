from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# def find_larger(lst):
#     max_value = 0
#     standard = lst[0]
#     for i in lst[1:]:
#         if i > standard and i > max_value:
#             return i
#     return max_value


class Solution:
    def __init__(self):
        self.head = None

    # 单调栈
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        self.head = head
        val_in_list = self.push_in_list()
        result = [0] * len(val_in_list)

        monotonous_stack = []

        for index, ele in enumerate(val_in_list):
            while monotonous_stack and val_in_list[monotonous_stack[-1]] < ele:
                x = monotonous_stack.pop()
                result[x] = index
            monotonous_stack.append(index)

        return [val_in_list[i] if i else 0 for i in result]

    # def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
    #     self.head = head
    #     result = []
    #     val_in_list = self.push_in_list()
    #     while len(val_in_list):
    #         result.append(find_larger(val_in_list))
    #         val_in_list.pop(0)
    #
    #     return result

    def push_in_list(self):
        result = []
        p = self.head
        while p:
            result.append(p.val)
            p = p.next
        return result


if __name__ == "__main__":
    pass
