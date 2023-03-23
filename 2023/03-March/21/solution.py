from typing import Sequence

class Solution:
    def zeroFilledSubarray(self, nums: Sequence[int]) -> int:
        result = 0
        i = 0
        while i < len(nums):
            # Find a subarray of 0's. If the current element is not 0, our
            # equation will simply work out to 0.
            count = 0
            while i < len(nums) and nums[i] == 0:
                count += 1
                i += 1
            i += 1
            result += (count * (count + 1)) // 2
        return result