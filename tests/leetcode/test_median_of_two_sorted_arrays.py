from kata.leetcode.median_of_two_sorted_arrays import Solution


class TestTwoNumbers:
    def test_case_1(self):
        assert Solution().findMedianSortedArrays(
            nums1=[1, 3], nums2=[2]
        ) == 2.0

    def test_case_2(self):
        assert Solution().findMedianSortedArrays(
            nums1=[1, 2], nums2=[3, 4]
        ) == 2.5
