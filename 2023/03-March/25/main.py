#!/usr/bin/env python3

import solution

if __name__ == '__main__':
    for i, (n, edges, expected_results) in enumerate((
        (3, [[0, 1], [0, 2], [1, 2]], 0),
        (7, [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]], 14),
    )):
        actual_results = solution.Solution().countPairs(n, edges)
        if actual_results == expected_results:
            print(f'Test Case {i + 1}: Success')
        else:
            print(f'Test Case {i + 1}: Failure '
                  f'(Expected: {expected_results}; Actual: {actual_results})')
