import unittest

from restore_ip_addresses.solution import Solution


class SolutionTest(unittest.TestCase):
    sln = Solution()

    def test_restore_ip_addresses(self):
        assert self.sln.restore_ip_addresses("333") == []
        assert self.sln.restore_ip_addresses("25525511135") == ["255.255.11.135","255.255.111.35"]