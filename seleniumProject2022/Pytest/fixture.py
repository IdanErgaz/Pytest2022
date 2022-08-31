import pytest

#when use the fixture this method will be run before EACH method
@pytest.fixture()
def setup():
    print('once before each method')

def test_method1(setup):
    print('test method 1')

def test_method2(setup):
    print('this is test method2')