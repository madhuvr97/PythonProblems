'''
pytest -m smoke -v -s   ==> Use this command to run the test cases marked as smoke
pytest -k Credit -v -s  ==> Use this command to run the selected test cases meeting a certain criteria
@pytest.mark.skip  ==> used to skip a test case
'''
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_function3():
    msg = "Hi"
    assert "Hello" == msg, "Test case failed."


def test_function4Credit():
    a, b = 2, 4
    assert a + 2 == b, "Addition do not match"
