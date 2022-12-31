from collections import defaultdict

import tests


# Time O(n)
# Space O(n)
def top_k_frequent(nums, k):
    count = defaultdict(int)
    freq = [[] for _ in range((len(nums) + 1))]
    for n in nums:
        count[n] += 1
    for n, c in count.items():
        freq[c].append(n)
    result = []
    for i in range(len(nums), 0, -1):
        for n in freq[i]:
            result.append(n)
            if len(result) == k:
                return result
    return []


tests.test(top_k_frequent)
