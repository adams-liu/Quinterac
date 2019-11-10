### TEST CODE ###

# Account_List = [1234567,7654321,1357246,6427531]
# Account_Balance = {}
# Account_Name = {"BobRoss123", }
#
# Accounts_Dict = {1234567: {'balance': 5000, 'name': 'bobross'},
#                  7654321: {'balance': 5000, 'name': 'johndoe'}}
#
# #Method sorts code
#
# Accounts_Dict[7777777] = {'balance': 7, 'name': 'seven'}

# Set all accounts to default balance of 5000
# for i in range(len(Account_List)):
#     Account_Balance[Account_List[i]] = 5000
# print(Account_Balance)

# print("Your account balance is:", Account_Balance)
# print("Your account dictionary is:", Accounts_Dict)

### Program starts here ###
# opens master account file
MAF_in = open("new_MAF.txt", "r+")
MAF_lines = MAF_in.read().splitlines()
# print("my infile is", MAF_lines)

# creates and organizes dictionary for MAF
real_Dict = {}
for row in MAF_lines:
    acc_num, balance, name = row.split()
    real_Dict[acc_num] = {'balance': int(balance), 'name': name}

# print("real dictionary is,", real_Dict)


# transaction functions
def deposit():
    print("in deposit function")
    return 0


def withdraw():
    print("in withdraw function")
    return 0


def transfer(acc1, amount, acc2):
    if real_Dict[acc2]["balance"] < amount:
        print("FATAL ERROR: transfer insufficient funds")
        return 0
    else:
        real_Dict[acc1]["balance"] += amount
    return 0


def create_acc():
    print("go to create function")
    return 0


def delete_acc():
    print("go to delete function")
    return 0


def end_sesh():
    print("end of system")
    new_MAF = []
    print("Sorted dict")
    for i in sorted(real_Dict.keys()):
        new_MAF.append(i + " " + str(real_Dict[i]["balance"]) + " " + real_Dict[i]["name"] + "\n")
        print(i, real_Dict[i])

    outfile = open("newNEW_MAF.txt", 'w')
    for i in new_MAF:
        ## Add all contents of the list onto the actual transaction summary file
        outfile.writelines(i)
    outfile.close()
    return 0


# Transaction checks start here
TSF_in = open("TSF.txt", "r+")
TSF_lines = TSF_in.read().splitlines()
for row in TSF_lines:
    ts_type, acc1, amount, acc2, acc_name = row.split()
    amount = int(amount)
    print("my prints are", ts_type, acc1, amount, acc2, acc_num)
    if ts_type == 'DEP':
        deposit()
    if ts_type == "WDR":
        withdraw()
    if ts_type == 'XFR':
        transfer(acc1, amount, acc2)
    if ts_type == 'NEW':
        create_acc()
    if ts_type == 'DEL':
        delete_acc()
    if ts_type == 'EOS':
        end_sesh()


def dog():
    print("YOUR GAY")
    # Your grammar is wrong ya clown