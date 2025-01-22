import itertools


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        nums = list(range(1, n + 1))
        res = [list(c) for c in itertools.combinations(nums, k)]
        return sorted(res)