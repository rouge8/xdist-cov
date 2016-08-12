import pytest

from dir1.mod1 import add


@pytest.mark.parametrize('numbers, result', [
    ([1, 2, 3, 4], 10),
])
def test_add(numbers, result):
    assert add(*numbers) == result
