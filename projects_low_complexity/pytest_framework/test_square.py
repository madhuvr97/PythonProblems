from square import square

# Write test cases using the fixture in conftest.py
def test_square_positive(setup):
    assert square(2) == 4


def test_square_negative(setup):
    assert square(-3) == 9
