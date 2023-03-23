#!/usr/bin/env python3

import solution

if __name__ == '__main__':
    for i, (n, connections, expected_results) in enumerate((
        (4, [[0, 1], [0, 2], [1, 2]], 1),
        (6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]], 2),
        (6, [[0, 1], [0, 2], [0, 3], [1, 2]], -1),
    )):
        actual_results = solution.Solution().makeConnected(n, connections)
        if actual_results == expected_results:
            print(f'Test Case {i + 1}: Success')
        else:
            print(f'Test Case {i + 1}: Failure '
                  f'(Expected: {expected_results}; Actual: {actual_results})')
