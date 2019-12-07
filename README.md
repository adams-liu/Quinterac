# Quinterac Project

The product that is designed is an Queen's Old-Fashioned Interactive Banking System ("Quinterac"). Quinterac consists of two parts:

    - the Front end, a banking transaction acceptor for simple ATM-stel baking transactions
    - the Back Office, an overnight batch processor to maintain and update a master accounts file.
# Directory Folders
```
│   .gitignore
│   LICENSE
│   README.md
│   requirements.txt
│   tree.txt
│   
├───.github
│   └───workflows
│           pythonapp.yml
│           
├───.pytest_cache
│   │   .gitignore
│   │   CACHEDIR.TAG
│   │   README.md
│   │   
│   └───v
│       └───cache
│               lastfailed
│               nodeids
│               stepwise
│               
├───qa327_app
│   │   Account_List.txt
│   │   backend.py
│   │   driver.py
│   │   front_end.py
│   │   new_MAF.txt
│   │   TSF.txt
│   │   __init__.py
│   │   __main__.py
│   │   
│   └───__pycache__
│           app.cpython-37.pyc
│           backend.cpython-37.pyc
│           front_end.cpython-37.pyc
│           __init__.cpython-37.pyc
│           
├───qa327_reports
│       Quinterac - Vowels Inc - Assn1.pdf
│       Quinterac - Vowels Inc - Assn2.pdf
│       Quinterac - Vowels Inc - Assn3.pdf
│       Quinterac - Vowels Inc - Assn4.pdf
│       Quinterac - Vowels Inc - Assn5.pdf
│       Quinterac - Vowels Inc - Assn6.pdf
│       
├───qa327_test
│   │   Account_List.txt
│   │   assn1_ requirements.xlsx
│   │   assn3_error_spreadsheet.xlsx
│   │   assn5_whitebox_tests.xlsx
│   │   test_backend.py
│   │   test_frontend.py
│   │   test_new_MAF.txt
│   │   test_new_TSF.txt
│   │   __init__.py
│   │   
│   ├───.pytest_cache
│   │   │   .gitignore
│   │   │   CACHEDIR.TAG
│   │   │   README.md
│   │   │   
│   │   └───v
│   │       └───cache
│   │               lastfailed
│   │               nodeids
│   │               stepwise
│   │               
│   └───__pycache__
│           test_backend.cpython-37-pytest-5.2.2.pyc
│           test_frontend.cpython-37-pytest-5.2.2.pyc
│           test_main_approach2.cpython-37-pytest-5.2.2.pyc
│           test_main_approach3.cpython-37-pytest-5.2.2.pyc
│           test_Quinterac.cpython-37-pytest-5.2.0.pyc
│           test_Quinterac.cpython-37-pytest-5.2.2.pyc
│           __init__.cpython-37.pyc
│           
└───__pycache__
        front_end.cpython-37.pyc
        test_Quinterac.cpython-37-pytest-5.2.0.pyc
```        

# How to run the Quinterac app
This is just to run the Quinterac app on it's own
1. Open your bash command-line
2. Go to the folder where the Quinterac app is located
```bash
$cd ./Quinterac/qa327_app
```
3. In the command-line to run Quinterac type the following:
```bash
$py front_end.py Account_List.txt TSF.txt
```
# How to run black box testing

For black-box testing, the pytest tool was used to run assertion statements. To run the tests, please do the following:
 1. Open your bash command-line
 2. Go to the folder where the Quinterac app is located
 ```bash
 $cd ./Quinterac/qa327_app
 ```
 3. Open "front_end.py" with your local text editor
 4. Comment out line 2 " from backend import * " if you are only running blackbox testing
 5. Go back to parent folder
 ```bash
 $cd ..
 $cd ./qa327_test
 ```
 6. In the command-line to run pytest type the following:
 ```bash
 $pytest test_front_end.py
 ```
 7. Make sure to go back to the front_end.py and uncomment line 2 after black-box testing is completed.

# How to run white box testing

For whitebox testing a the back office of the Quinterac app was cloned. To run the test, please do the following:
1. Open your bash command line
2. Go to the folder where the back office test code is
```bash
$cd ./Quinterac/qa327_test
```
3. Open "test_backend.py" with PyCharm
4. Press the green execute button to run
