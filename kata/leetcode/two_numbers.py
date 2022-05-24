from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        result = []

        for pos_l, value_l in enumerate(nums):
            for pos_r, value_r in enumerate(nums):
                if value_l + value_r == target and pos_l != pos_r:
                    result.append(pos_l)
                    result.append(pos_r)
                    return result


if __name__ == "__main__":
    Solution().twoSum(nums=[2, 7, 11, 15], target=9)
