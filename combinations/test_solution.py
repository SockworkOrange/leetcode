import unittest

from combinations.solution import Solution


class SolutionTest(unittest.TestCase):
    sln = Solution()

    def test_combinations(self):
        assert self.sln.combine(1,1) == [[1]]
        assert self.sln.combine(4,2) == [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]