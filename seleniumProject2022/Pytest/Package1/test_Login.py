import pytest
@pytest.fixture()
def setup():
    print('Opening URL for login')
    yield
    print('closing the APP- will be run after each method!')
def test_LoginByEmail(setup):
    print('login by email')

def test_LoginByFacebook(setup):
    print('login by facebook')