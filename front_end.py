### Test stuff
# val = input("Enter your value: \n")
# print(val)

acc_type = "test"
valid_acc = '1234567'

# def deposit():
#     while True:
#         acc_num = input("Enter in 7-digit account number: \n")
#         #if isinstance(acc_num, int) and len(str(acc_num)) == 7 and acc_num == valid_acc:
#         if isinstance(acc_num, str) == True:
#
#             print("Yayy")
#             # if acc_num == valid_acc:
#             #     deposit_value = input("Enter in how much you want to deposit: \n")
#                 # if deposit_value  == isinstance(deposit_value,int) and deposit_value == (size(deposit_value)> 3) and deposit_value == (size(deposit_value)> 8)
#             #
#         else:
#             print("Enter valid account number please!")


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
                            print("Account Successfully Deleted")
                            return True
                        else:
                            print("Error! Account name must be between 3-30 characters. \n")
                    elif is_alpha_num(name) != True:
                        print("Error! Please enter in alphanumeric characters. \n ")
            else:
                 print("Error! Please enter a valid account number. \n")
        elif is_int(acc_num) != True:
            print("Error! Enter in a 7-digit account number.")


def createacct():
    while True:
        acc_num = input("Enter in 7-digit account number: \n")
        # Check if account number is int
        if is_int(acc_num) == True:
            # Check if account number length 7
            if acc_num == valid_acc:
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
                 print("Error! Please enter a valid account number. \n")
        elif is_int(acc_num) != True:
            print("Error! Enter in a 7-digit account number. \n")


def is_valid_acc(acc):
    for i in range(len(valid_acc)):
        if acc == valid_acc(i):
            return True

def is_int(acc):
    n = [ord(j) for j in acc]
    for i in range(len(n)):
        #  47 < x < 57
        if 47 < n[i] <= 57:
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


def get_Acc_Type():
    while True:
        global acc_type
        acc_type = input("Please login as atm or agent:\n")
        if acc_type == "atm" or acc_type == "agent":
            # if (acc_type == "atm" || "agent")
            # if (acc_type == "atm"):
            #     acc_type = "atm"
            #     print("logged in as atm")
            # else: #agent
            #     acc_type = "agent"
            #     print("logged in as agent")
            print("my account type is", acc_type)
            break

        else: #user did not type atm or agent
            print("** ERROR ** User did not input valid account type")




### 327 Main Starts Here ###
print("Welcome to the 327 Front End")
# Looping Sessions
while True:
    login_valid = input('Please enter "login" to login to Quinterac: \n')
    if login_valid == "login":
        # continue
        print("Login successful")
        get_Acc_Type()
        # Looping Transactions
        while True:
            print ("What would you like to do?\n - Deposit (deposit)\n - Withdraw (withdraw)\n - Transfer (transfer)")
            if acc_type == "agent":
                print (" - Create Account (createacct)\n - Delete Account (deleteacct)")
            transaction_type = input(" - Logout (logout)\n")
            if (transaction_type == "deposit" or transaction_type == "withdraw" or transaction_type == "transfer" or transaction_type == "createacct" or transaction_type == "deleteacct" or transaction_type == "logout"):
                 #   print ("It worked")
                if transaction_type == "deposit":
                    print("Go to deposit function")
                    deposit()

                if transaction_type == "withdraw":
                    print("Go to withdraw function")
                if transaction_type == "transfer":
                    print("Go to transfer function")
                if transaction_type == "createacct":
                    if acc_type == "agent":
                        #print("Go to create account function")
                        createacct()
                    else:
                        print("You're not agent account type!")
                if transaction_type == "deleteacct":
                    if acc_type == "agent":
                        deleteacct()
                        #print("Go to delete account function")
                    else:
                        print("You're not agent account type!")
                if transaction_type == "logout":
                    print("Go to logout function")
                    break
            else:
                print("Not a valid transaction")


        print("Transaction Complete \n \n")
    else: # if user did not enter login
        print("** ERROR ** Login not valid, please enter valid input")


# user = input("Please login as agent or atm")
# if (user == "agent" or "atm")