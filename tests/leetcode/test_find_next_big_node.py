from kata.leetcode.find_next_big_node import Solution
from kata.leetcode.linked_list import LinkedList


class TestReversedLinkedList:

    def test_case_1(self):
        linked_list = LinkedList()
        linked_list.init_list(data=[2, 1, 5])

        assert Solution().nextLargerNodes(linked_list.head) == [5, 5, 0]

    def test_case_2(self):
        linked_list = LinkedList()
        linked_list.init_list(data=[2, 7, 4, 3, 5])
        assert Solution().nextLargerNodes(linked_list.head) == [7, 0, 5, 5, 0]

    def test_case_3(self):
        linked_list = LinkedList()
        linked_list.init_list(data=[1, 7, 5, 1, 9, 2, 5, 1])
        assert Solution().nextLargerNodes(linked_list.head) == [7, 9, 9, 9, 0, 5, 0, 0]
