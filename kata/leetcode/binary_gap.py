class Solution:

    def binary_gap(self, num):
        binary_of_num = to_binary(num).split("1")
        binary_of_num.pop()
        binary_of_num.pop(0)
        max_dis = 0
        for item in binary_of_num:
            if '0' in item:
                if (dis := len(item) + 1) > max_dis:
                    max_dis = dis
        return max_dis


def to_binary(n):
    return bin(n).replace('0b', '')


if __name__ == "__main__":
    Solution().binary_gap(22)
