from typing import MutableSequence


class Solution:
    def canPlaceFlowers(self, flowerbed: MutableSequence[int], n: int) -> bool:
        for i, plot in enumerate(flowerbed):
            # We have planted enough.
            if n <= 0:
                break
            # The current plot is already occupied.
            if plot == 1:
                continue
            # The previous plot is occupied.
            if i > 0 and flowerbed[i - 1] == 1:
                continue
            # The next plot is occupied.
            if i < len(flowerbed) - 1 and flowerbed[i + 1] == 1:
                continue
            flowerbed[i] = 1
            n -= 1
        return n <= 0
