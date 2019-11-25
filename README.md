# Quinterac Project

The product that is designed is an Queen's Old-Fashioned Interactive Banking System ("Quinterac"). Quinterac consists of two parts:

    - the Front end, a banking transaction acceptor for simple ATM-stel baking transactions
    - the Back Office, an overnight batch processor to maintain and update a master accounts file.

# How to Run Black Box Testing

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
 $py front_end.py Account_List.txt TSF.txt
 ```
 7. Make sure to go back to the front_end.py and uncomment line 2 after black-box testing is completed.
