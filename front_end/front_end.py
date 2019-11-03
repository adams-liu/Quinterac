import sys
import os

## Initialize global variable for account type.
acc_type = ""
## Initialize empty lists for temporary transaction summary file.
tsf_temp = []


## Writes all contents of the temporary transaction summary file onto the actual transaction summary file saved as "TSF.txt"
def temp_to_TSF(list):
    ## Takes the transaction summary file: "TSF.txt" from the command line under variable name: outfile

    outfile = open(sys.argv[2], 'w')
    for i in list:
        ## Add all contents of the list onto the actual transaction summary file
        outfile.writelines(i)
    outfile.close()

## Check if input is fully numeric
def is_int(input):
   ## Convert user input into ASCII values

   k = [ord(i) for i in input]
   for i in range(len(k)):
       ## Check if each character of user input is within range of ASCII Characters for integers
       if 47 < k[i] <= 57:
         pass
       else:
         return False
   return True

## Check if input is alphanumeric
def is_alpha_num(input):
   ## Convert user input into ASCII values
   n = [ord(j) for j in input]
   for i in range(len(n)):
       ## Check if input is within ASCII range of 47 < x < 57 or 64 < x < 91 or 97 < x < 123, for numbers, upper and lower case letters
       if 47 < n[i] <= 57 or 64 < n[i] < 91 or 96 < n[i] < 123:
           pass
       else:
           return False
   return True

## Reads the valid account list file saved as "Account_List.txt" and tries to match each entry against the user input
def check_valid_acc(acc_num):

    ## Takes the valid account list file from the system command line
    infile = open(sys.argv[1], "r+")

    lines = infile.read().splitlines()
    ## Loops through each entry of valid account list file
    for i in lines:
        ## Return True if there is a match with user input
        if acc_num == i:
            return True

    return False

## Transfer transaction
def transfer():
    while True:
        ## Ask for user input
        acc_num = input("Enter in 7-digit account number to transfer from: \n")
        if is_int(acc_num) == True:
            ## If the first digit of the account does not start with zero, proceed to next line
            if acc_num[0] != '0':
                ## If the length of user input are 7 digits, proceed to next line
                if len(str(acc_num)) == 7:
                    ## If the user input matches an account number from the valid account list file, then proceed
                    if check_valid_acc(acc_num) == True:
                        while True:
                            acc_num2 = input("Enter in 7-digit account number to transfer to: \n")
                            ## Check if second user input is of type string, 7 characters, and also a valid account number
                            if is_int(acc_num2) == True:
                                ## If the first digit of the account does not start with zero, proceed to next line
                                if acc_num2[0] != '0':
                                    ## If the length of user input are 7 digits, proceed to next line
                                    if len(str(acc_num2)) == 7:
                                        ## If the user input matches an account number from the valid account list file, then proceed
                                        if check_valid_acc(acc_num2) == True:
                                            while True:
                                                amount = input("Enter in a monetary amount between 3 and 8 digits: \n")
                                                ## Check if the user input are numbers
                                                if is_int(amount) == True:
                                                    ## Check if the user input is below 9 digits
                                                    if int(amount) <= 99999999 and int(amount) > 99:
                                                        print("You have successfully transferred: $" + amount + " from account " + acc_num + " to account " + acc_num2)
                                                        ## Appending transaction code into the temporary transaction summary file
                                                        tsf_temp.append("XFR " + acc_num + " " + amount + " " + acc_num2 + " " + '*** \n')
                                                        return True
                                                    elif int(amount) <= 99:
                                                        print("** ERROR **  Please enter an amount greater than 2 digits")
                                                    else:
                                                        print("** ERROR ** Please enter an amount below 9 digits")
                                                else:
                                                    print("** ERROR **  This is amount is not numerical")
                                        else:
                                            print("** ERROR **  You did not enter a valid account number")
                                    else:
                                        print("** ERROR **  Your account number was not 7-digits")
                                else:
                                    print("** ERROR **  Your account number can not start with 0")
                            else:
                                print("** ERROR **  Your account number must be numerical")
                    else:
                        print("** ERROR **  You did not enter a valid account number")
                else:
                    print("** ERROR **  Your account number was not 7-digits")
            else:
                print("** ERROR **  Your account number can not start with 0")
        else:
            print("** ERROR **  Your account number must be numerical")


## Deposit Transaction
def deposit():
    while True:
        ## Ask for user input
        acc_num = input("Please enter in 7-digit account number: \n")
        ## If the user input are numbers, then proceed to next line
        if is_int(acc_num) == True:
            ## If the first digit of the account does not start with zero, proceed to next line
            if acc_num[0] != '0':
                ## If the length of user input are 7 digits, proceed to next line
                if len(str(acc_num)) == 7:
                    ## If the user input matches an account number from the valid account list file, then proceed
                    if check_valid_acc(acc_num) == True:
                        while True:
                            amount = input("Enter in a monetary amount between 3 and 8 digits: \n")
                            ## Check if the user input are numbers
                            if is_int(amount) == True:
                                ## Check if the user input is below 9 digits
                                if int(amount) <= 99999999 and int(amount) > 99:
                                    print("You have successfully deposited: $", amount, "into your bank account")
                                    ## Appending transaction code into the temporary transaction summary file
                                    tsf_temp.append("DEP " + acc_num + " " + amount + " 0000000 "+"*** \n")
                                    return True
                                elif int(amount) <= 99:
                                    print("** ERROR **  Please enter an amount greater than 2 digits")
                                else:
                                    print("** ERROR **  Please enter an amount below 9 digits")
                            else:
                                print("** ERROR **  This is amount is not numerical")
                    else:
                        print("** ERROR **  You did not enter a valid account number")
                else:
                    print("** ERROR **  Your account number was not 7-digits")
            else:
                print("** ERROR **  Your account number can not start with 0")
        else:
            print("** ERROR **  Your account number must be numerical")


## Withdraw Transaction
def withdraw():
    while True:
        ## Ask for user input
        acc_num = input("Please enter in 7-digit account number: \n")
        ## If the user input are numbers, then proceed to next line
        if is_int(acc_num) == True:
            ## If the first digit of the account does not start with zero, proceed to next line
            if acc_num[0] != '0':
                ## If the length of user input are 7 digits, proceed to next line
                if len(str(acc_num)) == 7:
                    ## If the user input matches an account number from the valid account list file, then proceed
                    if check_valid_acc(acc_num) == True:
                        while True:
                            amount = input("Enter in a monetary amount between 3 and 8 digits: \n")
                            ## Check if the user input are numbers
                            if is_int(amount) == True:
                                ## Check if the user input is below 9 digits
                                if int(amount) <= 99999999 and int(amount) > 99:
                                    print("You have successfully withdrew: $",amount, "into your bank account")
                                    ## Appending transaction code into the temporary transaction summary file
                                    tsf_temp.append("WDR " + acc_num + " " + amount + " 0000000 "+"*** \n")
                                    return True
                                elif int(amount) <= 99:
                                    print("** ERROR **  Please enter an amount greater than 2 digits")
                                else:
                                    print("** ERROR **  Please enter an amount below 9 digits")
                            else:
                                print("** ERROR **  This is amount is not numerical")
                    else:
                        print("** ERROR **  You did not enter a valid account number")
                else:
                    print("** ERROR **  Your account number was not 7-digits")
            else:
                print("** ERROR **  Your account number can not start with 0")
        else:
            print("** ERROR **  Your account number must be numerical")

## Delete Account Transaction
def deleteacct():
   while True:
       ## Ask for user input
       acc_num = input("Enter in 7-digit account number: \n")
       # Check if user input are numbers
       if is_int(acc_num) == True:
           # Check if account number is on valid account list
           if check_valid_acc(acc_num) == True:
               while True:
                   name = input("Please enter an account name with between 3 - 30 alphanumeric characters. \n")
                   # Check if name entered is alphanumeric
                   if is_alpha_num(name) == True:
                       if len(name) >= 3 and len(name) < 31:
                           print("Account Successfully Deleted")
                           ## Appending transaction code into the temporary transaction summary file
                           tsf_temp.append("DEL " + acc_num + " 000" + " 0000000 " + name + ' \n')
                           return True
                       else:
                           print("** ERROR **  Account name must be between 3-30 characters.")
                   elif is_alpha_num(name) != True:
                       print("** ERROR **  Please enter in alphanumeric characters.")
           else:
                print("** ERROR **  Please enter a valid account number.")
       else:
           print("** ERROR **  Enter in a 7-digit account number.")


## Create Account Transaction
def createacct():
   while True:
       ## Ask for user input
       acc_num = input("Enter in 7-digit account number: \n")
       # Check if user input are numbers
       if is_int(acc_num) == True:
           # Check if account number entered is new
           if check_valid_acc(acc_num) == False:
               # Check if the account number entered is 7-digits
               if len(acc_num) == 7:
                   while True:
                       name = input("Please enter an account name with between 3 - 30 alphanumeric characters. \n")
                       # Check if name entered is alphanumeric
                       if is_alpha_num(name) == True:
                           if len(name) >= 3 and len(name) < 31:
                               print('Account Successfully Created')
                               ## Appending transaction code into the temporary transaction summary file
                               tsf_temp.append("NEW " + acc_num + " 000" + " 0000000 " + name + ' \n')
                               return True
                           else:
                               print("** ERROR **  Account name must be between 3-30 characters.")
                       elif is_alpha_num(name) != True:
                           print("** ERROR **  Please enter in alphanumeric characters.")
               else:
                    print("** ERROR **  Please enter an account number with 7 digits.")
           else:
                print("** ERROR **  Please enter a new account number.")
       else:
           print("** ERROR **  Enter in a 7-digit account number.")

## Identifies whether or not account type is atm or agent
def get_Acc_Type():

    while True:

        # User enters in user type
        acc_type = input("Please login as atm or agent:\n")
        ## Check if user input is valid
        if acc_type == "atm" or acc_type == "agent":
            return acc_type
        else: #user did not type atm or agent
            print("** ERROR **  User did not input valid account type")

def main():
    ### 327 Main Starts Here ###
    print("Welcome to the 327 Front End")

    # Looping Sessions
    while True:
        try:
            login_valid = input('Please enter "login" to login to Quinterac or "exit" to exit program:\n')
            if login_valid == "login":
                ## Request the user's account type: either atm or agent
                acc_type = get_Acc_Type()
                while True: # Looping Transactions
                    print ("What would you like to do?: - Deposit (deposit) | Withdraw (withdraw) | Transfer (transfer)", end ="")
                    ## If user is of type agent, then create account and delete account transactions are also shown as options
                    if acc_type == "agent":
                        print (" | Create Account (createacct) | Delete Account (deleteacct)", end ="")
                    ## Request user input, saved in the variable "transaction_type"
                    transaction_type = input(" | Logout (logout)\n")
                    ## Check if the user input matches any of the valid transactions
                    if transaction_type == "deposit" or transaction_type == "withdraw" or transaction_type == "transfer" or transaction_type == "createacct" or transaction_type == "deleteacct" or transaction_type == "logout":
                        if transaction_type == "deposit":

                            deposit()
                        if transaction_type == "withdraw":
                            withdraw()
                        if transaction_type == "transfer":
                            transfer()
                        if transaction_type == "createacct":
                            ## If the user type is agent, then proceed to transaction
                            if acc_type == "agent":
                                createacct()
                            else: ## ERROR  when atm user tries to create account
                                print("** ERROR **  You're not agent account type!")
                        if transaction_type == "deleteacct":
                            ## If the user type is agent, then proceed to transaction
                            if acc_type == "agent":
                                deleteacct()
                            else: ## ERROR  when atm user tries to delete account
                                print("** ERROR **  You're not agent account type!")
                        if transaction_type == "logout":
                            print("Transaction Complete!")
                            ## Logout add EOS transaction to the end of the temporary transaction summary file
                            tsf_temp.append("EOS " + '0000000 ' + "000 " + "0000000 " + "***\n")
                            ## add contents of the temporary transaction summary to the actual transaction summary file
                            temp_to_TSF(tsf_temp)
                            print("Transaction Complete!")
                            break
                    else: ## User did not enter a valid transaction
                        print("** ERROR **  Not a valid transaction, please try again!")
            ## Exit program when the user enters in exit
            elif login_valid == "exit":

                sys.exit()

            else: # if user did not enter login
                print("** ERROR **  Login not valid, please enter valid input")
        except:
            break
main()

