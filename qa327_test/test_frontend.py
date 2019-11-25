import tempfile
from importlib import reload
import os
import io
import sys

#import front_end.front_end as front_end
import qa327_app.front_end as front_end
path = os.path.dirname(os.path.abspath(__file__))


#### R6 Test Cases ####
def test_R6T1(capsys):

    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'logout'
        ],
        intput_valid_accounts=[
            
        ],
        expected_tail_of_terminal_output=[

           'Transaction Complete!',
            'Please enter "login" to login to Quinterac or "exit" to exit program:'

        ],
        expected_output_transactions=[
            'EOS 0000000 000 0000000 ***'
        ])
def test_R6T2(capsys):

    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'logout'
        ],
        intput_valid_accounts=[
            
        ],
        expected_tail_of_terminal_output=[

           'Transaction Complete!',
            'Please enter "login" to login to Quinterac or "exit" to exit program:'

        ],
        expected_output_transactions=[
            'EOS 0000000 000 0000000 ***'
        ])

#### R1 Test Cases ####
def test_R1T1(capsys):

    helper(
        capsys=capsys,
        terminal_input=[
            'logout'
        ],
        intput_valid_accounts=[
            
        ],
        expected_tail_of_terminal_output=[

           "** ERROR **  Login not valid, please enter valid input",
           'Please enter "login" to login to Quinterac or "exit" to exit program:'
        ],
        expected_output_transactions=[

        ])
def test_R1T2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'createacct'
        ],
        intput_valid_accounts=[
            
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  Login not valid, please enter valid input",
            'Please enter "login" to login to Quinterac or "exit" to exit program:'
        ],
        expected_output_transactions=[

        ])
def test_R1T3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'deleteacct'
        ],
        intput_valid_accounts=[
            
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  Login not valid, please enter valid input",
            'Please enter "login" to login to Quinterac or "exit" to exit program:'
        ],
        expected_output_transactions=[

        ])
def test_R1T4(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'deposit'
        ],
        intput_valid_accounts=[
            
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  Login not valid, please enter valid input",
            'Please enter "login" to login to Quinterac or "exit" to exit program:'
        ],
        expected_output_transactions=[

        ])
def test_R1T5(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'withdraw'
        ],
        intput_valid_accounts=[
            
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  Login not valid, please enter valid input",
            'Please enter "login" to login to Quinterac or "exit" to exit program:'
        ],
        expected_output_transactions=[

        ])
def test_R1T6(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'transfer'
        ],
        intput_valid_accounts=[
            
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  Login not valid, please enter valid input",
            'Please enter "login" to login to Quinterac or "exit" to exit program:'
        ],
        expected_output_transactions=[

        ])
def test_R1T7(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'asdfasdfjasdfj'
        ],
        intput_valid_accounts=[
            
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  Login not valid, please enter valid input",
            'Please enter "login" to login to Quinterac or "exit" to exit program:'
        ],
        expected_output_transactions=[

        ])

#### R2 Test cases ####
def test_R2T1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'login'
        ],
        intput_valid_accounts=[
            
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  Not a valid transaction, please try again!",
            "What would you like to do?: - Deposit (deposit) | Withdraw (withdraw) | Transfer (transfer) | Logout (logout)"
        ],
        expected_output_transactions=[

        ])
def test_R2T2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'asdfasdfasd'
        ],
        intput_valid_accounts=[
            
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  Not a valid transaction, please try again!",
            "What would you like to do?: - Deposit (deposit) | Withdraw (withdraw) | Transfer (transfer) | Logout (logout)"
        ],
        expected_output_transactions=[

        ])

#### R3 Test cases ####
def test_R3T1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm'
        ],
        intput_valid_accounts=[
            
        ],
        expected_tail_of_terminal_output=[
            "What would you like to do?: - Deposit (deposit) | Withdraw (withdraw) | Transfer (transfer) | Logout (logout)"
        ],
        expected_output_transactions=[

        ])
def test_R3T2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent'
        ],
        intput_valid_accounts=[
            
        ],
        expected_tail_of_terminal_output=[
            "What would you like to do?: - Deposit (deposit) | Withdraw (withdraw) | Transfer (transfer) | Create Account (createacct) | Delete Account (deleteacct) | Logout (logout)"
        ],
        expected_output_transactions=[

        ])

#### R4 Test cases ####
def test_R4T1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'deposit'
        ],
        intput_valid_accounts=[
            
        ],
        expected_tail_of_terminal_output=[
            "Please enter in 7-digit account number: "
        ],
        expected_output_transactions=[

        ])
def test_R4T2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'withdraw'
        ],
        intput_valid_accounts=[
            
        ],
        expected_tail_of_terminal_output=[
            "Please enter in 7-digit account number: "
        ],
        expected_output_transactions=[

        ])
def test_R4T3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'transfer'
        ],
        intput_valid_accounts=[
            
        ],
        expected_tail_of_terminal_output=[
            "Enter in 7-digit account number to transfer from: "
        ],
        expected_output_transactions=[

        ])
def test_R4T4(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'createacct'
        ],
        intput_valid_accounts=[
            
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  You're not agent account type!",
            "What would you like to do?: - Deposit (deposit) | Withdraw (withdraw) | Transfer (transfer) | Logout (logout)"

        ],
        expected_output_transactions=[

        ])
def test_R4T5(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'deleteacct'
        ],
        intput_valid_accounts=[
            
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  You're not agent account type!",
            "What would you like to do?: - Deposit (deposit) | Withdraw (withdraw) | Transfer (transfer) | Logout (logout)"
        ],
        expected_output_transactions=[

        ])

#### R5 Test cases ####
def test_R5T1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct'
        ],
        intput_valid_accounts=[
            
        ],
        expected_tail_of_terminal_output=[
            "Enter in 7-digit account number: "

        ],
        expected_output_transactions=[

        ])
def test_R5T2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'deleteacct'
        ],
        intput_valid_accounts=[
            
        ],
        expected_tail_of_terminal_output=[
            "Enter in 7-digit account number: "

        ],
        expected_output_transactions=[

        ])
def test_R5T3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'deposit'
        ],
        intput_valid_accounts=[
            
        ],
        expected_tail_of_terminal_output=[
            "Please enter in 7-digit account number: "
        ],
        expected_output_transactions=[

        ])
def test_R5T4(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'withdraw'
        ],
        intput_valid_accounts=[
            
        ],
        expected_tail_of_terminal_output=[
            "Please enter in 7-digit account number: "
        ],
        expected_output_transactions=[

        ])
def test_R5T5(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'transfer'
        ],
        intput_valid_accounts=[
            
        ],
        expected_tail_of_terminal_output=[
            "Enter in 7-digit account number to transfer from: "
        ],
        expected_output_transactions=[

        ])

#### R7 Test cases ####
def test_R7T1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'deposit',
            'qu3en$'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            '** ERROR **  Your account number must be numerical',
            'Please enter in 7-digit account number: '
        ],
        expected_output_transactions=[

        ])
def test_R7T2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'deposit',
            '0100327'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  Your account number can not start with 0",
            'Please enter in 7-digit account number: '
        ],
        expected_output_transactions=[

        ])
def test_R7T3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'deposit',
            '100327'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  Your account number was not 7-digits",
            'Please enter in 7-digit account number: '
        ],
        expected_output_transactions=[

        ])
def test_R7T4(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'deposit',
            '1000427'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  You did not enter a valid account number",
            'Please enter in 7-digit account number: '
        ],
        expected_output_transactions=[

        ])
def test_R7T5(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'deposit',
            '1000327'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'

        ],
        expected_tail_of_terminal_output=[
            "Enter in a monetary amount between 3 and 8 digits: "
        ],
        expected_output_transactions=[

        ])

#### R8 Test cases ####
def test_R8T1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'deposit',
            '1000327',
            'que3n$'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  This is amount is not numerical",
            "Enter in a monetary amount between 3 and 8 digits: "
        ],
        expected_output_transactions=[

        ])
def test_R8T2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'deposit',
            '1000327',
            '98'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  Please enter an amount greater than 2 digits",
            "Enter in a monetary amount between 3 and 8 digits: "
        ],
        expected_output_transactions=[

        ])
def test_R8T3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'deposit',
            '1000327',
            '987654321'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  Please enter an amount below 9 digits",
            "Enter in a monetary amount between 3 and 8 digits: "
        ],
        expected_output_transactions=[

        ])
def test_R8T4(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'deposit',
            '1000327',
            '101'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "You have successfully deposited: $ 101 into your bank account",
            "What would you like to do?: - Deposit (deposit) | Withdraw (withdraw) | Transfer (transfer) | Logout (logout)"
        ],
        expected_output_transactions=[

        ])

#### R9 Test cases ####
def test_R9T1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'deposit',
            '1000327',
            '101',
            'logout'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            'Transaction Complete!',
            'Please enter "login" to login to Quinterac or "exit" to exit program:'
        ],
        expected_output_transactions=[
            'DEP 1000327 101 0000000 *** ',
            'EOS 0000000 000 0000000 ***'
        ])

#### R10 Test cases ####
def test_R10T1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'withdraw',
            'qu3en$'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            '** ERROR **  Your account number must be numerical',
            'Please enter in 7-digit account number: '
        ],
        expected_output_transactions=[

        ])
def test_R10T2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'withdraw',
            '0100327'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  Your account number can not start with 0",
            'Please enter in 7-digit account number: '
        ],
        expected_output_transactions=[

        ])
def test_R10T3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'withdraw',
            '100327'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  Your account number was not 7-digits",
            'Please enter in 7-digit account number: '
        ],
        expected_output_transactions=[

        ])
def test_R10T4(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'withdraw',
            '1000427'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  You did not enter a valid account number",
            'Please enter in 7-digit account number: '
        ],
        expected_output_transactions=[

        ])
def test_R10T5(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'withdraw',
            '1000327'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'

        ],
        expected_tail_of_terminal_output=[
            "Enter in a monetary amount between 3 and 8 digits: "
        ],
        expected_output_transactions=[

        ])

#### R11 Test cases ####
def test_R11T1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'withdraw',
            '1000327',
            'que3n$'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  This is amount is not numerical",
            "Enter in a monetary amount between 3 and 8 digits: "
        ],
        expected_output_transactions=[

        ])
def test_R11T2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'withdraw',
            '1000327',
            '98'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  Please enter an amount greater than 2 digits",
            "Enter in a monetary amount between 3 and 8 digits: "
        ],
        expected_output_transactions=[

        ])
def test_R11T3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'withdraw',
            '1000327',
            '987654321'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  Please enter an amount below 9 digits",
            "Enter in a monetary amount between 3 and 8 digits: "
        ],
        expected_output_transactions=[

        ])
def test_R11T4(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'withdraw',
            '1000327',
            '101'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "You have successfully withdrew: $ 101 into your bank account",
            "What would you like to do?: - Deposit (deposit) | Withdraw (withdraw) | Transfer (transfer) | Logout (logout)"
        ],
        expected_output_transactions=[

        ])

#### R12 Test cases ####
def test_R12T1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'withdraw',
            '1000327',
            '101',
            'logout'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            'Transaction Complete!',
            'Please enter "login" to login to Quinterac or "exit" to exit program:'
        ],
        expected_output_transactions=[
            'WDR 1000327 101 0000000 *** ',
            'EOS 0000000 000 0000000 ***'
        ])

#### R13 Test cases ####
def test_R13T1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'transfer',
            'qu3en$'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            '** ERROR **  Your account number must be numerical',
            'Enter in 7-digit account number to transfer from: '
        ],
        expected_output_transactions=[

        ])
def test_R13T2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'transfer',
            '0100327'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  Your account number can not start with 0",
            'Enter in 7-digit account number to transfer from: '
        ],
        expected_output_transactions=[

        ])
def test_R13T3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'transfer',
            '100327'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  Your account number was not 7-digits",
            'Enter in 7-digit account number to transfer from: '
        ],
        expected_output_transactions=[

        ])
def test_R13T4(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'transfer',
            '1000427'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  You did not enter a valid account number",
            'Enter in 7-digit account number to transfer from: '
        ],
        expected_output_transactions=[

        ])
def test_R13T5(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'transfer',
            '1000327'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            'Enter in 7-digit account number to transfer to: '
        ],
        expected_output_transactions=[

        ])
#### R14 Test cases ####
def test_R14T1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'transfer',
            '1000327',
            'qu3en$'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            '** ERROR **  Your account number must be numerical',
            'Enter in 7-digit account number to transfer to: '
        ],
        expected_output_transactions=[

        ])
def test_R14T2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'transfer',
            '1000327',
            '0100327'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  Your account number can not start with 0",
            'Enter in 7-digit account number to transfer to: '
        ],
        expected_output_transactions=[

        ])
def test_R14T3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'transfer',
            '1000327',
            '100327'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  Your account number was not 7-digits",
            'Enter in 7-digit account number to transfer to: '
        ],
        expected_output_transactions=[

        ])
def test_R14T4(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'transfer',
            '1000327',
            '1000427'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  You did not enter a valid account number",
            'Enter in 7-digit account number to transfer to: '
        ],
        expected_output_transactions=[

        ])
def test_R14T5(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'transfer',
            '1000327',
            '1000328'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            'Enter in a monetary amount between 3 and 8 digits: '
        ],
        expected_output_transactions=[

        ])
#### R15 Test cases ####
def test_R15T1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'transfer',
            '1000327',
            '1000328',
            'que3n$'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  This is amount is not numerical",
            "Enter in a monetary amount between 3 and 8 digits: "
        ],
        expected_output_transactions=[

        ])
def test_R15T2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'transfer',
            '1000327',
            '1000328',
            '98'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "** ERROR **  Please enter an amount greater than 2 digits",
            "Enter in a monetary amount between 3 and 8 digits: "
        ],
        expected_output_transactions=[

        ])
def test_R15T3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'transfer',
            '1000327',
            '1000328',
            '987654321'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "** ERROR ** Please enter an amount below 9 digits",
            "Enter in a monetary amount between 3 and 8 digits: "
        ],
        expected_output_transactions=[

        ])
def test_R15T4(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'transfer',
            '1000327',
            '1000328',
            '101'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            'You have successfully transferred: $101 from account 1000327 to account 1000328',
            'What would you like to do?: - Deposit (deposit) | Withdraw (withdraw) | Transfer (transfer) | Logout (logout)'
        ],
        expected_output_transactions=[

        ])
#### R16 Test cases ####
def test_R16T1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'transfer',
            '1000327',
            '1000328',
            '101',
            'logout'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            'Transaction Complete!',
            'Please enter "login" to login to Quinterac or "exit" to exit program:'
        ],
        expected_output_transactions=[
            'XFR 1000327 101 1000328 *** ',
            'EOS 0000000 000 0000000 ***'
        ])

#### R17 Test cases ####
def test_R17T1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            'que3n$'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "**ERROR** Enter in a 7-digit account number",
            "Enter in 7-digit account number: "
        ],
        expected_output_transactions=[

        ])

def test_R17T2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '0100329'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "**ERROR** Your account number can not start with 0",
            "Enter in 7-digit account number: "
        ],
        expected_output_transactions=[

        ])


def test_R17T3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '100329'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "**ERROR** Please enter an account number with 7 digits",
            "Enter in 7-digit account number: "
        ],
        expected_output_transactions=[

        ])


def test_R17T4(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '1000327'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "**ERROR** Please enter a new account number",
            "Enter in 7-digit account number: "
        ],
        expected_output_transactions=[

        ])


def test_R17T5(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '1000329'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "Please enter an account name with between 3 - 30 alphanumeric characters "
        ],
        expected_output_transactions=[

        ])

#### R18 Test cases ####
def test_R18T1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '1000329',
            'my'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "**ERROR** Account name must be between 3-30 characters",
            "Please enter an account name with between 3 - 30 alphanumeric characters "
        ],
        expected_output_transactions=[

        ])


def test_R18T2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '1000329',
            'Acc123'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "Account Successfully Created",
            "What would you like to do?: - Deposit (deposit) | Withdraw (withdraw) | Transfer (transfer) | Create Account (createacct) | Delete Account (deleteacct) | Logout (logout)"
        ],
        expected_output_transactions=[

        ])


def test_R18T3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '1000329',
            'myAccountNameIsWayTooLong123456789'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "**ERROR** Account name must be between 3-30 characters",
            "Please enter an account name with between 3 - 30 alphanumeric characters "
        ],
        expected_output_transactions=[

        ])


def test_R18T4(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '1000329',
            'qu3en$'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            "**ERROR** Please enter in alphanumeric characters",
            "Please enter an account name with between 3 - 30 alphanumeric characters "
        ],
        expected_output_transactions=[

        ])

#### R19 Test cases ####
def test_R19T1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '1000329',
            'Acc123',
            'logout'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328'
        ],
        expected_tail_of_terminal_output=[
            'Please enter "login" to login to Quinterac or "exit" to exit program:'
        ],
        expected_output_transactions=[
            'NEW 1000329 000 0000000 Acc123 ',
            'EOS 0000000 000 0000000 ***'
        ])

#### R20 Test cases ####
def test_R20T1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'deleteacct',
            'qu3en$'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328',
            '1000329'
        ],
        expected_tail_of_terminal_output=[
            "**ERROR** Enter in a 7-digit account number",
            "Enter in 7-digit account number: "
        ],
        expected_output_transactions=[

        ])

def test_R20T2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'deleteacct',
            '0100329'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328',
            '1000329'
        ],
        expected_tail_of_terminal_output=[
            "**ERROR** Your account number can not start with 0",
            "Enter in 7-digit account number: "
        ],
        expected_output_transactions=[

        ])

def test_R20T3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'deleteacct',
            '100329'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328',
            '1000329'
        ],
        expected_tail_of_terminal_output=[
            "**ERROR** Your account number must only have 7 digits",
            "Enter in 7-digit account number: "
        ],
        expected_output_transactions=[

        ])

def test_R20T4(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'deleteacct',
            '1000123'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328',
            '1000329'
        ],
        expected_tail_of_terminal_output=[
            "**ERROR** Please enter a valid account number",
            "Enter in 7-digit account number: "
        ],
        expected_output_transactions=[

        ])

def test_R20T5(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'deleteacct',
            '1000329'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328',
            '1000329'
        ],
        expected_tail_of_terminal_output=[
            "Please enter an account name with between 3 - 30 alphanumeric characters"
        ],
        expected_output_transactions=[

        ])

#### R21 Test cases ####
def test_R21T1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'deleteacct',
            '1000329',
            'my'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328',
            '1000329'
        ],
        expected_tail_of_terminal_output=[
            "**ERROR** Account name must be between 3-30 characters",
            "Please enter an account name with between 3 - 30 alphanumeric characters"
        ],
        expected_output_transactions=[

        ])

def test_R21T2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'deleteacct',
            '1000329',
            'Acc123'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328',
            '1000329'
        ],
        expected_tail_of_terminal_output=[
            "Account Successfully Deleted",
            "What would you like to do?: - Deposit (deposit) | Withdraw (withdraw) | Transfer (transfer) | Create Account (createacct) | Delete Account (deleteacct) | Logout (logout)"
        ],
        expected_output_transactions=[

        ])

def test_R21T3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'deleteacct',
            '1000329',
            'myAccountNameIsWayTooLong123456789'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328',
            '1000329'
        ],
        expected_tail_of_terminal_output=[
            "**ERROR** Account name must be between 3-30 characters",
            "Please enter an account name with between 3 - 30 alphanumeric characters"
        ],
        expected_output_transactions=[

        ])

def test_R21T4(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'deleteacct',
            '1000329',
            'qu3en$'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328',
            '1000329'
        ],
        expected_tail_of_terminal_output=[
            "**ERROR** Please enter in alphanumeric characters",
            "Please enter an account name with between 3 - 30 alphanumeric characters"
        ],
        expected_output_transactions=[

        ])

#### R22 Test cases ####
def test_R22T1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'deleteacct',
            '1000329',
            'Acc123',
            'logout'
        ],
        intput_valid_accounts=[
            '1000327',
            '1000328',
            '1000329'
        ],
        expected_tail_of_terminal_output=[
            "Transaction Complete!",
            'Please enter "login" to login to Quinterac or "exit" to exit program:'
        ],
        expected_output_transactions=[
            'DEL 1000329 000 0000000 Acc123 ',
            'EOS 0000000 000 0000000 ***'
        ])

def helper(
        capsys,
        terminal_input,
        expected_tail_of_terminal_output,
        intput_valid_accounts,
        expected_output_transactions
):
    """Helper function for testing

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
        terminal_input -- list of string for terminal input
        expected_tail_of_terminal_output list of expected string at the tail of terminal
        intput_valid_accounts -- list of valid accounts in the valid_account_list_file
        expected_output_transactions -- list of expected output transactions
    """

    # cleanup package
    reload(front_end)

    # create a temporary file in the system to store output transactions
    temp_fd, temp_file = tempfile.mkstemp()
    transaction_summary_file = temp_file

    # create a temporary file in the system to store the valid accounts:
    temp_fd2, temp_file2 = tempfile.mkstemp()
    valid_account_list_file = temp_file2
    with open(valid_account_list_file, 'w') as wf:
        wf.write('\n'.join(intput_valid_accounts))

    # prepare program parameters
    sys.argv = [
        'front_end.py',
        valid_account_list_file,
        transaction_summary_file]

    # set terminal input
    sys.stdin = io.StringIO(
        '\n'.join(terminal_input))

    # run the program
    front_end.main()

    # capture terminal output / ERROR s
    # assuming that in this case we don't use stderr
    out, err = capsys.readouterr()

    # split terminal output in lines
    out_lines = out.splitlines()

    # print out the testing information for debugging
    # the following print content will only display if a
    # test case failed:
    print('std.in:', terminal_input)
    print('valid accounts:', intput_valid_accounts)
    print('terminal output:', out_lines)
    print('terminal output (expected tail):', expected_tail_of_terminal_output)

    # compare terminal outputs at the end.`
    for i in range(1, len(expected_tail_of_terminal_output)+1):
        index = i * -1
        assert expected_tail_of_terminal_output[index] == out_lines[index]

    # compare transactions:
    with open(transaction_summary_file, 'r') as of:
        content = of.read().splitlines()

        # print out the testing information for debugging
        # the following print content will only display if a
        # test case failed:
        print('output transactions:', content)
        print('output transactions (expected):', expected_output_transactions)

        for ind in range(len(content)):
            assert content[ind] == expected_output_transactions[ind]

    # clean up
    os.close(temp_fd)
    os.remove(temp_file)
