import unittest

from merge_intervals.solution import Solution


class SolutionTest(unittest.TestCase):
    sln = Solution()

    def test_merge(self):
        assert self.sln.merge([[1, 3]]) == [[1, 3]]
        assert self.sln.merge([[1, 3], [2, 5]]) == [[1, 5]]
        assert self.sln.merge([[1, 3], [2, 5], [5, 8]]) == [[1, 8]]
        assert self.sln.merge([[1, 4], [0, 4]]) == [[0, 4]]
        assert self.sln.merge([[2,3],[4,5],[6,7],[8,9],[1,10]]) == [[1, 10]]
