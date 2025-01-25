import unittest

from spiral_matrix_ii.solution import Solution


class SolutionTest(unittest.TestCase):
    sln = Solution()

    def test_generate_matrix(self):
        assert self.sln.generate_matrix(1) == [[1]] # idx 0.0
        assert self.sln.generate_matrix(2) == [
            [1, 2],
            [4, 3]
        ]
        assert self.sln.generate_matrix(3) == [
            [1,2,3],
            [8,9,4],
            [7,6,5]
        ]