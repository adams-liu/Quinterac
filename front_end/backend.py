

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


def transfer(acc1, amount, acc2):
    if real_Dict[acc2]["balance"] < amount:
        print("FATAL ERROR: transfer insufficient funds")
        return 0
    else:
        real_Dict[acc1]["balance"] += amount
    return 0


def create_acc(acc, acc_name):
    real_Dict[acc] = {'balance': 500000, 'name': acc_name}
    return 0


def delete_acc(acc, acc_name):
    if real_Dict[acc]['name'] != acc_name:
        print("FATAL ERROR: account name does not match")
    else:
        del real_Dict[acc]
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

    if ts_type == 'DEP':
        deposit(acc1,amount)
    if ts_type == "WDR":
        withdraw(acc1,amount)
    if ts_type == 'XFR':
        transfer(acc1, amount, acc2)
    if ts_type == 'NEW':
        create_acc(acc1, acc_name)
    if ts_type == 'DEL':
        delete_acc(acc1, acc_name)
    if ts_type == 'EOS':
        end_sesh()

