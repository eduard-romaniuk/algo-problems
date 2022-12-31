from collections import defaultdict

import tests


# Time O(m*n)
# Space O(m)
# Where m - len(strs) and n - average(len(current_str))
def group_anagrams(strs):
    anagrams = defaultdict(list)
    ord_a = ord('a')
    for current_str in strs:
        count = [0] * 26
        for char in current_str:
            count[ord(char) - ord_a] += 1
        anagrams[tuple(count)].append(current_str)
    return list(anagrams.values())


tests.test(group_anagrams)
