#!/usr/bin/env python3

import solution

if __name__ == '__main__':
    for i, (flowerbed, n, expected_results) in enumerate((
        ([1, 0, 0, 0, 1], 1, True),
        ([1, 0, 0, 0, 1], 2, False),
    )):
        actual_results = solution.Solution().canPlaceFlowers(flowerbed, n)
        if actual_results == expected_results:
            print(f'Test Case {i + 1}: Success')
        else:
            print(f'Test Case {i + 1}: Failure '
                  f'(Expected: {expected_results}; Actual: {actual_results})')
