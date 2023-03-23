#!/usr/bin/env python3

import solution

if __name__ == '__main__':
    for i, (nums, expected_results) in enumerate((
        ([1, 3, 0, 0, 2, 0, 0, 4], 6),
        ([0, 0, 0, 2, 0, 0], 9),
        ([2, 10, 2019], 0),
    )):
        actual_results = solution.Solution().zeroFilledSubarray(nums)
        if actual_results == expected_results:
            print(f'Test Case {i + 1}: Success')
        else:
            print(f'Test Case {i + 1}: Failure '
                  f'(Expected: {expected_results}; Actual: {actual_results})')
