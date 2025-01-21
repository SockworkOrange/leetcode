from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        i = 0
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        curr_interval: List[int] = intervals[i]
        next_interval: List[int] = intervals[i+1]

        while next_interval is not None:
            [curr_left, curr_right] = curr_interval
            [next_left, next_right] = next_interval

            if curr_right >= next_left:
                intervals[i] = [min(curr_left, next_left), max(curr_right, next_right)]
                del intervals[i+1]
            else:
                i += 1

            curr_interval = intervals[i]
            next_interval = intervals[i+1] if i+1 < len(intervals) else None
        return intervals