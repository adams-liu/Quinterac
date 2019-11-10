# opens master account file
MAF_in = open("new_MAF.txt", "r+")
MAF_lines = MAF_in.read().splitlines()

# creates and organizes dictionary for MAF
real_Dict = {}
for row in MAF_lines:
    acc_num, balance, name = row.split()
    real_Dict[acc_num] = {'balance': int(balance), 'name': name}


# transaction deposit
def deposit(acc1,amount):
    real_Dict[acc1]["balance"] = real_Dict[acc1]["balance"] + amount
    return 0

# transaction withdraw
def withdraw(acc1,amount):
    if(real_Dict[acc1]["balance"] >= amount):
        real_Dict[acc1]["balance"] = real_Dict[acc1]["balance"] - amount
    else:
        print("FATAL ERROR: withdraw insufficient funds")
    return 0

# transaction transfer
def transfer(acc1, amount, acc2):
    if real_Dict[acc2]["balance"] < amount:
        print("FATAL ERROR: transfer insufficient funds")
        return 0
    else:
        real_Dict[acc1]["balance"] += amount
        real_Dict[acc2]["balance"] -= amount
    return 0

# transaction create account
def create_acc(acc, acc_name):
    real_Dict[acc] = {'balance': 500000, 'name': acc_name}
    return 0

# transaction delete account
def delete_acc(acc, acc_name):
    if (real_Dict[acc]['name'] != acc_name) and (real_Dict[acc]['balance'] != 0):
        print("FATAL ERROR: account name does not match and account balance is not zero")
    elif real_Dict[acc]['name'] != acc_name:
        print("FATAL ERROR: account name does not match")
    elif real_Dict[acc]['balance'] != 0:
        print("FATAL ERROR: account balance is not zero")
    else:
        del real_Dict[acc]
    return 0

# transaction end of session
def end_sesh():
    # store MAF lines
    new_MAF = []
    # creates new account list with new MAF
    acc_list_out = open("Account_List.txt", 'w')
    # sorts dictionary keys
    for i in sorted(real_Dict.keys()):
        # creates line for MAF
        new_MAF.append(i + " " + str(real_Dict[i]["balance"]) + " " + real_Dict[i]["name"] + "\n")
        # writes the (ordered) account number
        acc_list_out.write(i)
        acc_list_out.write("\n")
    # closes new account list
    acc_list_out.close()

    # creates new MAF file
    MAF_out = open("new_MAF.txt", 'w')
    for i in new_MAF:
        ## Add all contents of MAF list to MAF file
        MAF_out.writelines(i)
    # closes new MAF file
    MAF_out.close()
    return 0


# Transaction checks start here
TSF_in = open("TSF.txt", "r+")
TSF_lines = TSF_in.read().splitlines()

# Goes through each transaction line by line
for row in TSF_lines:
    ts_type, acc1, amount, acc2, acc_name = row.split()
    amount = int(amount)
    # Branches off to transaction function type depending on first attribute
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

