### Test stuff
# val = input("Enter your value: \n")
# print(val)

import sys

acc_type = "test"
valid_acc = "1234567"
valid_acc_list = []
count = 0
tsf_temp = list()

## Check if input is fully numeric
def is_int(n):
   k = [ord(i) for i in n]
   for i in range(len(k)):
       if 47 < k[i] <= 57:
         pass
       else:
         return False
   return True

def is_alpha_num(k):
   n = [ord(j) for j in k]
   for i in range(len(n)):
       #  47 < x < 57,  64 < x < 91, 97 < x < 123
       if 47 < n[i] <= 57 or 64 < n[i] < 91 or 96 < n[i] < 123:
           pass
       else:
           return False
   return True

def print_accounts():
    List_File = open("Account_List.txt", "r+")
    for line in List_File:
        valid_acc_list.append(line)
    #for i in valid_acc_list:
    print (valid_acc_list)

def transfer():
    while True:
        acc_num = input("Enter in 7-digit account number to transfer from: \n")
        if isinstance(acc_num, str) and len(str(acc_num)) == 7 and int(acc_num) == valid_acc:
            while True:
                acc_num2 = input("Enter in 7-digit account number to transfer to: \n")
                if isinstance(acc_num2, str) and len(str(acc_num2)) == 7 and int(acc_num2) == valid_acc:
                    while True:
                        deposit_value = input("Enter a 3 to 8 digit monetary value to transfer: \n")
                        if isinstance(deposit_value, str) and len(str(deposit_value)) >= 3 and len(str(deposit_value)) <= 8:
                            print("Transferred " + deposit_value + " from account " + acc_num + " to account " + acc_num2 + ". \n")
                            tsf_temp.append("XFR",acc_num,deposit_value,acc_num2)
                            print(tsf_temp)
                            break
                        else:
                            print("Enter valid monetary amount to transfer pelase!")
                    break
                else:
                    print("Enter valid account number please!")
            break
        else:
            print("Enter valid account number please!")

def deposit():
    while True:
        acc_num = input("Please enter in 7-digit account number: \n")
        if is_int(acc_num) == True:
            if len(str(acc_num)) == 7:
                if acc_num == valid_acc: #replace the valid_acc with excel
                    while True:
                        amount = input("Enter how much you want to deposit: \n")
                        if is_int(amount) == True:
                            if int(amount) < 99999999 or int(amount) > 0:
                                print("You have successfully deposited: $", amount, "into your bank account")
                                tsf_temp.append("DEP " + acc_num + amount + " 0000000 "+"***")
                                return True
                            else:
                                print("**ERROR** You please enter a range between 0 - 99999999")
                        else:
                            print("**ERROR** This is amount is not numerical")
                else:
                    print("**ERROR** You did not enter a valid account number")
            else:
                print("**ERROR** Your account number was not 7-digits")
        else:
            print("**ERROR** Your account number must be numerical")

## Withdraw Transaction
def withdraw():
    while True:
        acc_num = input("Please enter in 7-digit account number: \n")
        if is_int(acc_num) == True:
            if len(str(acc_num)) == 7:
                if acc_num == str(valid_acc): #replace the valid_acc with excel
                    while True:
                        amount = input("Enter how much you want to withdraw: \n")
                        if is_int(amount) == True:
                            if int(amount) < 99999999 and int(amount) > 0:
                                print("You have successfully withdrawed:$",amount, "into your bank account")
                                return True
                            else:
                                print("**ERROR** You please enter a range between 0 - 99999999")
                        else:
                            print("**ERROR** This is amount is not numerical")
                else:
                    print("**ERROR** You did not enter a valid account number")
            else:
                print("**ERROR** Your account number was not 7-digits")
        else:
            print("**ERROR** Your account number must be numerical")

## Delete Acc
def deleteacct():
   while True:
       acc_num = input("Enter in 7-digit account number: \n")
       # Check if account number is int
       if is_int(acc_num) == True:
           # Check if account number is on valid account list
           if acc_num == valid_acc:
               while True:
                   name = input("Please enter an account name with between 3 - 30 alphanumeric characters. \n")
                   # Check if name entered is alphanumeric
                   if is_alpha_num(name) == True:
                       if len(name) >= 3 and len(name) < 31:
                           print("Account successfully created")
                           return True
                       else:
                           print("Error! Account name must be between 3-30 characters. \n")
                   elif is_alpha_num(name) != True:
                       print("Error! Please enter in alphanumeric characters. \n ")
           else:
                print("Error! Please enter a valid account number. \n")
       elif is_int(acc_num) != True:
           print("Error! Enter in a 7-digit account number.")

## Create Acct
def createacct():
   while True:
       acc_num = input("Enter in 7-digit account number: \n")
       # Check if account number is int
       if is_int(acc_num) == True:
           # Check if account number length 7
           if acc_num != valid_acc:
               if len(acc_num) == 7:
                   while True:
                       name = input("Please enter an account name with between 3 - 30 alphanumeric characters. \n")
                       # Check if name entered is alphanumeric
                       if is_alpha_num(name) == True:
                           if len(name) >= 3 and len(name) < 31:
                               print('Accounts Successfully Created')

                               return True
                           else:
                               print("Error! Account name must be between 3-30 characters. \n")
                       elif is_alpha_num(name) != True:
                           print("Error! Please enter in alphanumeric characters. \n ")
               else:
                    print("Error! Please enter an account number with 7 digits. \n")
           else:
                print("Error! Please enter a new account number. \n")
       elif is_int(acc_num) != True:
           print("Error! Enter in a 7-digit account number. \n")

## Identifies whether or not account type is atm or agent
def get_Acc_Type():
    while True:
        global acc_type
        acc_type = input("Please login as atm or agent:\n")
        if acc_type == "atm" or acc_type == "agent":
            break
        else: #user did not type atm or agent
            print("** ERROR ** User did not input valid account type")

### 327 Main Starts Here ###
print("Welcome to the 327 Front End")
# Looping Sessions
while True:
    login_valid = input('Please enter "login" to login to Quinterac or "exit" to exit program: \n')
    if login_valid == "login":
        get_Acc_Type()
        while True: # Looping Transactions
            print ("What would you like to do?\n - Deposit (deposit)\n - Withdraw (withdraw)\n - Transfer (transfer)")
            if acc_type == "agent":
                print (" - Create Account (createacct)\n - Delete Account (deleteacct)")
            transaction_type = input(" - Logout (logout)\n")
            if (transaction_type == "deposit" or transaction_type == "withdraw" or transaction_type == "transfer" or transaction_type == "createacct" or transaction_type == "deleteacct" or transaction_type == "logout"):
                if transaction_type == "deposit":
                    deposit()
                if transaction_type == "withdraw":
                    withdraw()
                if transaction_type == "transfer":
                    print("Go to transfer function")
                    transfer()
                if transaction_type == "createacct":
                    if acc_type == "agent":
                        createacct()
                    else:
                        print("You're not agent account type!")
                if transaction_type == "deleteacct":
                    if acc_type == "agent":
                        deleteacct()
                    else:
                        print("You're not agent account type!")
                if transaction_type == "logout":
                    break
            else:
                print("Not a valid transaction")
        print("Transaction Complete \n \n")

    elif login_valid == "exit":
        sys.exit()
    elif login_valid == "test":
        print_accounts()

    else: # if user did not enter login
        print("** ERROR ** Login not valid, please enter valid input")


