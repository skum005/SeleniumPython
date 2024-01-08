'''

Python assertions

'''


def add(num1, num2):
    return num1 + num2


# hard assert example

def test_assertions_demo():
    assert add(2, 5) == 8, 'Addition 2,5 failed'
    assert add(2, 2) == 5, 'Addition of 2 & 2 failed'


def test_login_invalid():
    print('this test name has substring matching another test called login in the package regression')
    assert add(3, 3) == 6, 'addition of 3 & 3 faileds'
