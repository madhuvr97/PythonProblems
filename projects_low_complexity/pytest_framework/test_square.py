import pytest
from square import square


@pytest.mark.usefixtures("setup")
class TestSquare:
    def test_square_positive(self, setup):
        assert square(2) == 4

    def test_square_negative(self, setup):
        assert square(-3) == 9
