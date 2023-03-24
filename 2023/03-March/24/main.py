#!/usr/bin/env python3

import solution

if __name__ == '__main__':
    for i, (n, connections, expected_results) in enumerate((
        (6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]], 3),
        (5, [[1, 0], [1, 2], [3, 2], [3, 4]], 2),
        (3, [[1, 0], [2, 0]], 0),
    )):
        actual_results = solution.Solution().minReorder(n, connections)
        if actual_results == expected_results:
            print(f'Test Case {i + 1}: Success')
        else:
            print(f'Test Case {i + 1}: Failure '
                  f'(Expected: {expected_results}; Actual: {actual_results})')
