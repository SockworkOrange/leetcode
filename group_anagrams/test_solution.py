import unittest

from group_anagrams.solution import Solution


class SolutionTest(unittest.TestCase):
    sln = Solution()

    def test_groupAnagrams(self):
        assert self.sln.groupAnagrams(["a"]) == [["a"]]
        assert self.sln.groupAnagrams(["abc", "bac"]) == [["abc", "bac"]]
        assert self.sln.groupAnagrams(["abc", "rad", "bac", "dar"]) == [["abc", "bac"], ["rad", "dar"]]
