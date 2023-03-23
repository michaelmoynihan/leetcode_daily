#!/usr/bin/env python3

import solution

if __name__ == '__main__':
    for i, (n, roads, expected_results) in enumerate((
        (4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]], 5),
        (4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]], 2),
    )):
        actual_results = solution.Solution().minScore(n, roads)
        if actual_results == expected_results:
            print(f'Test Case {i + 1}: Success')
        else:
            print(f'Test Case {i + 1}: Failure '
                  f'(Expected: {expected_results}; Actual: {actual_results})')
