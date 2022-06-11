from kata.leetcode.common import LinkedList, get_the_last_node, map_linked_list_to_hash_table
from kata.leetcode.linked_list_cycle import Solution


class TestReorderLRist:

    def test_case_1(self):
        linked_list = LinkedList()
        linked_list.init_list(data=[3, 2, 0, -4])
        last_node = get_the_last_node(linked_list.head)
        linked_list_hash = map_linked_list_to_hash_table(linked_list.head)
        last_node.next_node = linked_list_hash.get(1)
        assert Solution().hasCycle(linked_list.head)

    def test_case_2(self):
        linked_list = LinkedList()
        linked_list.init_list(data=[1, 2])
        last_node = get_the_last_node(linked_list.head)
        linked_list_hash = map_linked_list_to_hash_table(linked_list.head)
        last_node.next_node = linked_list_hash.get(0)
        assert Solution().hasCycle(linked_list.head)

    def test_case_3(self):
        linked_list = LinkedList()
        linked_list.init_list(data=[1])
        assert Solution().hasCycle(linked_list.head) is False
