from kata.leetcode.linked_list import LinkedList
from kata.leetcode.reorder_list import Solution


class TestReorderList:

    def test_case_1(self):
        linked_list = LinkedList()
        linked_list.init_list(data=[1, 2, 3, 4])

        Solution().reorderList(linked_list.head)
        assert linked_list.push_in_list() == [1, 4, 2, 3]

    def test_case_2(self):
        linked_list = LinkedList()
        linked_list.init_list(data=[1, 2, 3, 4, 5])

        Solution().reorderList(linked_list.head)
        assert linked_list.push_in_list() == [1, 5, 2, 4, 3]
