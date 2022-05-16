from kata.leetcode.reversed_linked_list import Solution, ListNode


class TestReversedLinkedList:

    def test_case_1(self):
        num_1 = ListNode(1)
        num_2 = ListNode(2)
        num_1.next = num_2
        num_3 = ListNode(3)
        num_2.next = num_3
        num_4 = ListNode(4)
        num_3.next = num_4
        num_5 = ListNode(5)
        num_4.next = num_5

        assert Solution().reverseList(num_1) == num_5

    def test_case_2(self):
        num_1 = ListNode(1)
        num_1.next = (num_2 := ListNode(2))
        assert Solution().reverseList(num_1) == num_2

    def test_case_3(self):
        assert Solution().reverseList(None) is None
