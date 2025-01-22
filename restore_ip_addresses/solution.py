class Solution:
    def restore_ip_addresses(self, s: str) -> list[str]:
        if len(s) < 4:
            return []
        result = self.expand_ip_range([], s)
        return result

    def expand_ip_range(self, ip_range_octets: list[int], remaining_s: str) -> list[str]:
        all_ip_octets_exist = len(ip_range_octets) == 4
        no_remaining_digits = remaining_s == ""

        if all_ip_octets_exist and no_remaining_digits:
            return [".".join([str(o) for o in ip_range_octets])]

        # 1. valid ip range, but still more digits to process => no ip permutations to add
        # 2. not a valid ip range, and no digits left to make it valid => no ip permutations to add
        if all_ip_octets_exist or no_remaining_digits:
            return []

        result = []

        octet_1 = int(remaining_s[:1])
        if 0 <= octet_1 <= 255:
            result += self.expand_ip_range(ip_range_octets + [octet_1], remaining_s[1:])
        if octet_1 == 0:
            return result

        octet_2 = int(remaining_s[:2])
        if 0 <= octet_2 <= 255:
            result += self.expand_ip_range(ip_range_octets + [octet_2], remaining_s[2:])

        octet_3 = int(remaining_s[:3])
        if 0 <= octet_3 <= 255:
            result += self.expand_ip_range(ip_range_octets + [octet_3], remaining_s[3:])

        return sorted(set(result))