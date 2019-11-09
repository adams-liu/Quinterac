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


    #print("real dictionary is,", real_Dict)


# transaction functions
def deposit():
    print("in deposit function")
    return 0


def withdraw():
    print("in withdraw function")
    return 0


def transfer():
    print("in transfer function")
    return 0


def create_acc(acc, acc_name):
    print("create function")
    real_Dict[acc] = {'balance': 500000, 'name': acc_name}
    return 0


def delete_acc(acc, acc_name):
    print("delete function")
    if real_Dict[acc]['name'] != acc_name:
        print("FATAL ERROR")
    else:
        del real_Dict[acc]
    return 0


def end_sesh():
    print("end of system")
    return 0


# Transaction checks start here
TSF_in = open("TSF.txt", "r+")
TSF_lines = TSF_in.read().splitlines()
for row in TSF_lines:
    ts_type, acc1, amount, acc2, acc_name = row.split()
    amount = int(amount)
    #print("my prints are", ts_type, acc1, amount, acc2, acc_num)
    if ts_type == 'DEP':
        deposit()
    if ts_type == "WDR":
        withdraw()
    if ts_type == 'XFR':
        transfer()
    if ts_type == 'NEW':
        create_acc(acc1, acc_name)
        print(real_Dict)
    if ts_type == 'DEL':
        delete_acc(acc1, acc_name)
        print(real_Dict)
    if ts_type == 'EOS':
        end_sesh()



