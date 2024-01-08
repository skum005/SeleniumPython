'''

1. For installing Pytest use the command: pip install Pytest
2. For Uninstalling Pytest: pip uninstall Pytest
3. To list the packages installed: pip list
4. To verify the version of Pytest: Pytest --version

pip stands for Package Installer for Python

Another way to install a package in Pycharm. Go to File(or Pycharm) -> Settings -> Select your python project -> Select
Python Interpreter -> Click + icon to add new package

'''

'''
Running Python tests

To run all tests: pytest
To run tests that are in a .py file: pytest <file_name>.py 
another way: python -m pytest
another way(provides additional info like print statements under captured sdout section, short test summary etc): pytest -v -rA 

'''

'''
naming conventions 

Pytest file names should have a prefix: test_ or a suffix _test
Similarly the test methods should also have the prefix of test and we must not include a hyphen(-)
And test methods cannot have same names 


'''


'''

running all tests, tests from one or more packages and sub-set of tests from a file

1. Running all tests -> execute the command "pytest -v -rA" from the terminal when you are in the root directory. This collects all the 
pytests present different packages and runs all tests in those packages
 
2. Running tests from a package for ex. regression

Navigate to the directory or package regression first and then run "pytest -v -rA" command. This command collects the tests 
from the package "regression" and only executes those tests 

OR execute the command that includes the package name(BETTER WAY OF DOING IT as it doesnt require switching directory)

pytest <package-name> -v -rA
e.g. pytest regression -v -rA

3. Running tests from more than one package

pytest <package-name1> <package-name2> -v -rA
e.g. pytest regression smoke -v -rA

4. Running sub-set of tests 

(a) Consider two tests having the string 'login' in their names and you can execute them using the command below

pytest -k <matching_string_case_insensitive> -v -rA
e.g. pytest -k login -v -rA

or it can be enclosed in double quotes: pytest -k "login" -v -rA 
 
(b) Consider two tests having the string 'login' in their names and you dont want to execute them, you can do that using the command below

pytest -k "not login" -v -rA

5. Run tests present in a file under a package

pytest <package-name>/<file-name> -v -rA

pytest regression/test_assertions.py -v -rA

6. Running one test function from a file 

pytest <package-name>/<file-name>::<function_name> -v -rA
e.g. pytest regression/test_assertions.py::test_login_invalid -v -rA

'''
