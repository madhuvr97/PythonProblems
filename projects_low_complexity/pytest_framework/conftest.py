'''
In Pytest, fixtures are functions that provide a fixed baseline for setup, preparation, and cleanup tasks required for
testing. They allow for the establishment of a consistent and reusable state for testing scenarios by providing data,
objects, or resources necessary for test execution.

In Pytest, conftest.py serves as a means of providing fixtures for an entire directory. Fixtures defined in a
conftest.py file can be utilized by any test within that package without the need for explicit imports, as pytest
automatically discovers them. This allows for the sharing of fixtures across multiple test files within the same
directory structure.
'''

# Define a fixture to set up the test environment
import pytest

@pytest.fixture
def setup():
    print("\nSetting up test environment")
    # Perform any setup tasks here if needed
    yield
    print("\nTearing down test environment")
    # Perform any cleanup tasks here if needed