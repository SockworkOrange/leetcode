import unittest

from unique_paths.solution import Solution


class SolutionTest(unittest.TestCase):
    sln = Solution()

    def test_unique_paths(self):
        assert self.sln.unique_paths(1, 1) == 1
        assert self.sln.unique_paths(1, 2) == 1
        assert self.sln.unique_paths(2, 2) == 2
        assert self.sln.unique_paths(3, 2) == 3
        assert self.sln.unique_paths(3, 3) == 6
        assert self.sln.unique_paths(3, 7) == 28