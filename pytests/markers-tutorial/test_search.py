import pytest

'''
MARKERS

Group tests using markers 

--> To list all inbuilt markers available use the command: pytest --markers

-->  Adding custom markers
    -To add a custom marker to your test method @pytest.mark.custom_marker_name. 
    - After adding a marker the tests can be executed using the command: pytest -m "marker_name" -v -rA. E.g. pytest -m "smoke" -v -rA
    -The above command displays a warning saying that the marker is not registered. 
        -- we can either disable the warnings by adding the command like arg --disable-warnings
        -- We can register the marker to avoid these warnings which can be done by adding in pytest.ini file(refer the same for syntax)

-->  We can add multiple markers to a single test method. Refer the test_search1() test method
--> To run tests marked with multiple markers(the below command searches for tests that satisfies both smoke and regression)
      - pytest -m "marker1 and marker2". e.g. pytest -m "smoke and regression"
      
--> Similarly there are other ways to run tests 
     - pytest -m "smoke and not regression"
     - pytest -m "not regression"      
     - pytest -m "not regression" markers-tutorial/test_search.py     
     - pytest -m "smoke or regression"
     
--> Markers can be defined at file level. For declaring single using the below command at the top of the file
    - pytestmark = pytest.mark.all 
    - for defining multiple 
    pytestmark = [pytest.mark.all, pytest.mark.suite1]
'''

pytestmark = [pytest.mark.all, pytest.mark.suite1]

@pytest.mark.regression
@pytest.mark.smoke
def test_search1():
    print('Search test 1 running')
    assert 2+2 == 4, 'Search test 1 failed'


@pytest.mark.smoke
def test_search2():
    print('Search test 2 running')
    assert 2+2 == 5, 'Search test 2 failed'


def test_e2e():
    print('Search test e2e')
    assert 2+2 == 5, 'Search test e2e failed'
