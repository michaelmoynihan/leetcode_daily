#!/usr/bin/env python3

import solution

if __name__ == '__main__':
    for i, (actions, params, expected_results) in enumerate((
        (
            ['WordDictionary', 'addWord', 'addWord', 'addWord',
                'search', 'search', 'search', 'search'],
            [[], ['bad'], ['dad'], ['mad'], ['pad'], ['bad'], ['.ad'], ['b..']],
            [None, None, None, None, False, True, True, True],
        ),
    )):
        word_dictionary = None
        actual_results = []
        for j, (action, param, expected_result) in enumerate(zip(actions, params, expected_results)):
            if action == 'WordDictionary':
                word_dictionary = solution.WordDictionary(*param)
                actual_results.append(None)
            elif action == 'addWord':
                actual_results.append(word_dictionary.addWord(*param))
            elif action == 'search':
                actual_results.append(word_dictionary.search(*param))
            else:
                actual_results.append(None)
        if actual_results == expected_results:
            print(f'Test Case {i + 1}: Success')
        else:
            print(f'Test Case {i + 1}: Failure '
                  f'(Expected: {expected_results}; Actual: {actual_results})')
