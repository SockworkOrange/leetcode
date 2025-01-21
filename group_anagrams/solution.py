from typing import List, Dict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res: Dict[str, List[str]] = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in res:
                res[sorted_s] = []
            res[sorted_s].append(s)
        return [strs for _, strs in res.items()]