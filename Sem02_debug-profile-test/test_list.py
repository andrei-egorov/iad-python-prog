
# find the mismatched elements in list `l1` which are not in list `l2`

def solution(l1: list, l2: list) -> list:
    return [
        e
        for e in l1
        if e not in [e for e in l2]
    ]

import pytest

a = [1,2,3]
b = [3,4,None,None]
TEST_CASES = [[a,b]]

class TestCase:
    @pytest.mark.parametrize("test_case", TEST_CASES)
    def test_events(self, test_case):
        assert solution(test_case[0], test_case[1]) == [1,2]
