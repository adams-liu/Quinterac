

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


print("real dictionary is,", real_Dict)
print("testing" , real_Dict["1234567"])


# transaction functions
def deposit(acc1,amount):
    real_Dict[acc1]["balance"] = real_Dict[acc1]["balance"] + amount
    print("Final Amount" , real_Dict[acc1]["balance"])
    return 0


def withdraw(acc1,amount):
    if(real_Dict[acc1]["balance"] >= amount):
        real_Dict[acc1]["balance"] = real_Dict[acc1]["balance"] - amount
        print("Final Amount" , real_Dict[acc1]["balance"])
    else:
        print("FATAL ERROR: Withdraw insufficient funds")
    return 0


def transfer():
    print("in transfer function")
    return 0


def create_acc():
    print("go to create function")
    return 0


def delete_acc():
    print("go to delete function")
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
    print("my prints are", ts_type, acc1, amount, acc2, acc_name)
    if ts_type == 'DEP':
        deposit(acc1,amount)
    if ts_type == "WDR":
        withdraw(acc1,amount)
    if ts_type == 'XFR':
        transfer()
    if ts_type == 'NEW':
        create_acc()
    if ts_type == 'DEL':
        delete_acc()
    if ts_type == 'EOS':
        end_sesh()

