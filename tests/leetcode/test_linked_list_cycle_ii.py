from kata.leetcode.common import LinkedList, get_the_last_node, map_linked_list_to_hash_table
from kata.leetcode.linked_list_cycle_ii import Solution


class TestLinkedListCycleII:

    def test_case_1(self):
        linked_list = LinkedList()
        linked_list.init_list(data=[3, 2, 0, -4])
        last_node = get_the_last_node(linked_list.head)
        linked_list_hash = map_linked_list_to_hash_table(linked_list.head)
        last_node.next_node = linked_list_hash.get(1)
        assert Solution().detectCycle(linked_list.head) == linked_list_hash.get(1)

    def test_case_2(self):
        linked_list = LinkedList()
        linked_list.init_list(data=[1, 2])
        last_node = get_the_last_node(linked_list.head)
        linked_list_hash = map_linked_list_to_hash_table(linked_list.head)
        last_node.next_node = linked_list_hash.get(0)
        assert Solution().detectCycle(linked_list.head) == linked_list_hash.get(0)

    def test_case_3(self):
        linked_list = LinkedList()
        linked_list.init_list(data=[1])
        assert Solution().detectCycle(linked_list.head) is None

    def test_case_4(self):
        linked_list = LinkedList()
        linked_list.init_list(
            data=[-21, 10, 17, 8, 4, 26, 5, 35, 33, -7, -16, 27, -12, 6, 29, -12, 5, 9, 20, 14, 14, 2, 13, -24, 21, 23,
                  -21, 5])
        last_node = get_the_last_node(linked_list.head)
        linked_list_hash = map_linked_list_to_hash_table(linked_list.head)
        last_node.next_node = linked_list_hash.get(24)
        assert Solution().detectCycle(linked_list.head) == linked_list_hash.get(24)
