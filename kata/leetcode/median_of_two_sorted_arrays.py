from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        sorted_merged_list = sorted(nums1)
        print(sorted_merged_list)
        length = len(sorted_merged_list)
        if length % 2 == 1:
            result = sorted_merged_list[int(length / 2)]
        else:
            result = (sorted_merged_list[left := int(length / 2) - 1] + sorted_merged_list[left + 1]) / 2

        return result


if __name__ == "__main__":
    a = Solution().findMedianSortedArrays(
        nums1=[1, 2, 3],
        nums2=[5, 4]
    )

    print(a)
