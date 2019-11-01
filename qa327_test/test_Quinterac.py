import tempfile
from importlib import reload
import os
import io
import sys

#import front_end.front_end as front_end
import front_end.front_end as front_end

path = os.path.dirname(os.path.abspath(__file__))


def test_R6T1(capsys):

    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'atm',
            'logout'

        ],
        intput_valid_accounts=[
            '123456'
        ],
        expected_tail_of_terminal_output=[

           'Transaction Complete!'
        ],
        expected_output_transactions=[
            'EOS 0000000 000 0000000 ***'
        ])
def test_R1T1(capsys):

    helper(
        capsys=capsys,
        terminal_input=[
            'logout'
        ],
        intput_valid_accounts=[
            '123456'
        ],
        expected_tail_of_terminal_output=[

           "** ERROR ** Login not valid, please enter valid input"
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
            '123456'
        ],
        expected_tail_of_terminal_output=[

            "** ERROR ** Login not valid, please enter valid input"
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
            '123456'
        ],
        expected_tail_of_terminal_output=[

            "** ERROR ** Login not valid, please enter valid input"
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
            '123456'
        ],
        expected_tail_of_terminal_output=[

            "** ERROR ** Login not valid, please enter valid input"
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
            '123456'
        ],
        expected_tail_of_terminal_output=[

            "** ERROR ** Login not valid, please enter valid input"
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
            '123456'
        ],
        expected_tail_of_terminal_output=[

            "** ERROR ** Login not valid, please enter valid input"
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
            '123456'
        ],
        expected_tail_of_terminal_output=[

            "** ERROR ** Login not valid, please enter valid input"
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
            '123456'
        ],
        expected_tail_of_terminal_output=[

            "** Error ** Not a valid transaction, please try again!"
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
            '123456'
        ],
        expected_tail_of_terminal_output=[

            "** Error ** Not a valid transaction, please try again!"
        ],
        expected_output_transactions=[

        ])

#### R3 Test cases ####
def test_r3(capsys):

    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'logout'

        ],
        intput_valid_accounts=[
            '123456'
        ],
        expected_tail_of_terminal_output=[

           'Transaction Complete!'
        ],
        expected_output_transactions=[
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

    # capture terminal output / errors
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
        assert expected_tail_of_terminal_output[index] == out_lines[index-1]

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
