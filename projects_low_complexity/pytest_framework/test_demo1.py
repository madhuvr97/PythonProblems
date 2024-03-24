'''
Pytest file naming conventions:
    Test files start with "test_".
    Test modules should be named "test_<module_name>.py".
    Test classes start with "Test".
    Test functions within modules or classes start with "test_".
'''
import pytest


@pytest.mark.smoke
def test_function1():
    print("Hello madhu!")


def test_function2Credit():
    print("Good morning...")
