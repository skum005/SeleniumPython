'''

Fixtures:

1. Manual Fixture set up:

 -> Use the decorator @pytest.fixture() on the method that you want to run before/after a test(or to mark as a fixture)
 -> give the method name as argument in the test methods so that the fixture would be executed before/after test

2.  Automation fixture set up:

  -> To mark a method as automatic fixture use the command - @pytest.fixture(autouse=True)
  -> This runs automatically and would be the first one to run

3. To detect the fixtures for a file/module use the command

  pytest --fixtures package_name/file_name

4. Use built in marker @pytest.mark.usefixtures("fixture1", "fixture2") to call the fixtures at test level

5. We can have fixtures at different level, say for module the below command should be used

   @pytest.fixture(scope=module)
'''
import pytest


@pytest.fixture()
def setup_teardown():
    print('Setting up DB')
    yield
    print('Closing DB connections')

@pytest.fixture(autouse=True)
def automatic_fixture():
    print('Automatic Fixture is running')

@pytest.fixture()
def marker_fixture():
    print('Marker fixture')

@pytest.fixture(scope="function", autouse=True)
def module_level_fixture():
    print('Module level fixture is running')

def test_one(setup_teardown):
    print('Testing for test_one is in progress')

def test_two(setup_teardown):
    print('Testing for test_two is in progress')

@pytest.mark.usefixtures("marker_fixture")
def test_three():
    print('Test 3 with automatic and marker fixture running')
