### Test stuff
# val = input("Enter your value: \n")
# print(val)

import sys

acc_type = "test"
valid_acc = 1234567

def deposit():
    while True:
        acc_num = input("Enter in 7-digit account number: \n")
        #if isinstance(acc_num, int) and len(str(acc_num)) == 7 and acc_num == valid_acc:
        if isinstance(acc_num, str) == True:

            print("Yayy")
            # if acc_num == valid_acc:
            #     deposit_value = input("Enter in how much you want to deposit: \n")
                # if deposit_value  == isinstance(deposit_value,int) and deposit_value == (size(deposit_value)> 3) and deposit_value == (size(deposit_value)> 8)
            #
        else:
            print("Enter valid account number please!")



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
    login_valid = input('Please enter "login" to login to Quinterac or "exit" to exit program: \n')
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
                        print("Go to create account function")
                    else:
                        print("You're not agent account type!")
                if transaction_type == "deleteacct":
                    if acc_type == "agent":
                        print("Go to delete account function")
                    else:
                        print("You're not agent account type!")
                if transaction_type == "logout":
                    print("Go to logout function")
                    break
            else:
                print("Not a valid transaction")



        print("Transaction Complete \n \n")
    if login_valid == "exit":
        sys.exit()
    else: # if user did not enter login
        print("** ERROR ** Login not valid, please enter valid input")


# user = input("Please login as agent or atm")
# if (user == "agent" or "atm")