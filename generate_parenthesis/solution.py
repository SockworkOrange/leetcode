from typing import List


class Solution:
    def generate_parenthesis(self, n: int) -> List[str]:
        strs = self.expand_permutations({"()": 1}, 1, n)
        result = sorted([s for s, i in strs.items() if i == n])
        return result

    def expand_permutations(self, strs: dict[str, int], depth: int, n: int) -> dict[str, int]:
        should_expand = False
        strs_k = list(strs)
        strs_to_expand = [s for s, i in strs.items() if i == depth]
        for s in strs_to_expand:
            i = strs[s]
            if i >= n:
                continue
            should_expand = True
            strs = strs | {
                s + s2: i + strs[s2]
                for s2 in strs_k
                if i + strs[s2] <= n
            }
            strs = strs | {
                s2 + s: i + strs[s2]
                for s2 in strs_k
                if i + strs[s2] <= n
            }
            strs["(" + s + ")"] = i + 1
        if should_expand:
            return self.expand_permutations(strs, depth+1, n)
        return strs
