import math


class Solution:
    def unique_paths(self, m: int, n: int) -> int:
        possible_moves = m+n-2 # m-1 moves down + n-1 moves right
        possible_ways = m-1
        return math.comb(possible_moves, possible_ways)