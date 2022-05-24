from typing import List


class Solution:

    # violence O(n^2)
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #
    #     result = []
    #
    #     for pos_l, value_l in enumerate(nums):
    #         for pos_r, value_r in enumerate(nums):
    #             if value_l + value_r == target and pos_l != pos_r:
    #                 result.append(pos_l)
    #                 result.append(pos_r)
    #                 return result

    # O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []

        for pos, value in enumerate(nums):
            p = list.copy(nums)
            p.remove(value)
            if target - value in p:
                result.append(pos)
        return result


if __name__ == "__main__":
    Solution().twoSum(nums=[2, 7, 11, 15], target=9)
