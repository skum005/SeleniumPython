'''

Parameterizing Tests:

-> Parameterization can be achived using the decorator @pytest.mark.parametrize

'''
import math

import pytest

# the below test runs with 3 data sets
@pytest.mark.parametrize("num1, num2, sum", [(1,2,3), (2,4,6), (4,5,9)])
def test_param_with_sigle_decor(num1, num2, sum):
    assert num1 + num2 == sum, 'Sum is invalid'

# the below tests validates the exponential with 9 combinations e.g. 1 pow 1, 1 pow 5, 1 pow 2, 4 pow 1, 4 pow 5 .... 6 pow 2
@pytest.mark.parametrize('base', [1, 4, 6])
@pytest.mark.parametrize('expo', [1, 5, 2])
def test_param_with_multiple_decor(base, expo):
    assert base ** expo == math.pow(base, expo), 'Difference is invalid'

