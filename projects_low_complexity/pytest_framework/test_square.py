'''
In Pytest, fixtures are functions that provide a fixed baseline for setup, preparation, and cleanup tasks required for
testing. They allow for the establishment of a consistent and reusable state for testing scenarios by providing data,
objects, or resources necessary for test execution. Fixtures help in reducing code duplication, improving test
readability, and enhancing test reliability by ensuring that the necessary preconditions are met before running tests.
By encapsulating setup and teardown logic, fixtures promote modular and maintainable test code, enabling efficient
testing practices in software development.
'''

import pytest
from square import square

# Define a fixture to set up the test environment
@pytest.fixture
def setup():
    print("\nSetting up test environment")
    # Perform any setup tasks here if needed
    yield
    print("\nTearing down test environment")
    # Perform any cleanup tasks here if needed

# Write test cases using the fixture
def test_square_positive(setup):
    assert square(2) == 4


def test_square_negative(setup):
    assert square(-3) == 9
