import pytest
def setup_module(module):  #Perform ONCE in the Beginning !!!
    print('PrintONCE IN THE BEGINING!!!')

def teardown_module(module):
    print('Perform Once in the END!!!')  #Perform Once in the End!!!
@pytest.fixture()
def setup():
    print('run before EACH method/test!')
    yield
    print('run AFTER each test')



def test_SignInByEmail(setup):
    print('sinin by EMAIL')

def test_signInByFB(setup):
    print('signin by facebook')


