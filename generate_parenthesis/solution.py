from typing import List


class Solution:
    def generate_parenthesis(self, n: int) -> List[str]:
        strs = self.expand_permutations({"()": 1}, 1, n)
        result = [s for s, i in strs.items() if i == n]
        result = sorted(result)
        return result

    def expand_permutations(self, strs: dict[str, int], depth: int, n: int) -> dict[str, int]:
        should_expand = False

        strs_k = list(strs)
        strs_to_expand = [s for s, i in strs.items() if i == depth]
        for s1 in strs_to_expand:
            i = strs[s1]
            if i >= n:
                continue
            should_expand = True

            strs["(" + s1 + ")"] = i + 1
            for s2 in strs_k:
                j = strs[s2]
                cnt = i + j
                if i + strs[s2] <= n:
                    self.add_if_missing(s1+s2, cnt, strs)
                    self.add_if_missing(s2+s1, cnt, strs)

        if should_expand:
            return self.expand_permutations(strs, depth+1, n)
        return strs

    def add_if_missing(self, v: str, depth: int, strs: dict[str, int]):
        if v not in strs:
            strs[v] = depth
