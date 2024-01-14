from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], _: int) -> None:
        i = 0
        for n in nums2:
            while i < m and n > nums1[i]:
                i += 1
            for j in reversed(range(i, m)):
                nums1[j + 1] = nums1[j]
            nums1[i] = n
            i += 1
            m += 1
