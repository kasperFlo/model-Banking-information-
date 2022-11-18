import acounts as A , os ,time ,json 
from pprint import pprint
clear = lambda: os.system('clear')
centeramount = 50

#setting defaults
wallet = 10000
localBankDB = []


defaultAc = A.regularAcount(0000,"default",2.2,5000)
checkingAc = A.checkingAcount("0001","defaultChck",2.2,5001,200)
savingAc = A.savingAccount("0002","defaultSave",2.2,5002,2000)

def showMainMenu():  
    import acounts as A 
    while True: 
        # clear()
        print("""       --Main Menu--
    [1] : Open Account
    [2] : Select Account
    [3] : Exit Application
        """)
        try: 
            userinp = int(input("> "))
        #DONE open acount
            if userinp == 1:
                try:
                    # print("""       --Account Opening--""")
                    # accountType = input("what type of acount would you like to open (\n   [regular]\n   [checking]\n   [saving)\n   >")
                    # acountHolderName = input("What Name Would you like this account to be under\n   >")
                    # rateOfInterest = input("What is this accounts rate of interest\n    >")
                    # currentBalance = input("How much would you like to initially deposit into this account\n    >")
                    # acountNumber = input("what is this accounts number\n    >")
                    
                    accountType = "regular"
                    acountHolderName = "dickhead"
                    rateOfInterest = "dickhead" #69
                    currentBalance = 21
                    acountNumber = 6868
                    
                    if(accountType.lower() == "regular"):
                        acountHolderName = A.regularAcount(acountNumber,acountHolderName,rateOfInterest,currentBalance)
                    elif(accountType.lower() =="checking"):
                        overdraftAllowed = input("What is the over draft of this account\n    >")
                        acountHolderName = A.checkingAcount(acountNumber,acountHolderName,rateOfInterest,currentBalance,overdraftAllowed)
                    elif(accountType.lower =="saving"):
                        minimumBalance = input("What is this accounts Minimum Balance\n   ")
                        acountHolderName = A.savingAccount(acountNumber,acountHolderName,rateOfInterest,currentBalance,overdraftAllowed,minimumBalance)
                    updateDatabase(acountHolderName)
                except Exception as e: print(e, end="")

        #DONE select account
            elif userinp == 2:
                allAcNum = [i['acountNumber'] for i in Gdata]
                print("  All Acounts")

                pprint(Gdata)
                # pprint(localBankDB)

                while True:
                    inpnum = int(input("Enter Account Number "))
                    if inpnum in allAcNum:
                        showAccountMenu(allAcNum.index(inpnum))
                    else:
                        print("account doesnt exsist")
        #DONE Application  
            elif userinp == 3:
                print("EXITING Banking System")
                exit
        except: print("invalid input") 
        time.sleep(2)
        
def showAccountMenu(inputAcc):
    global wallet
    selectedAcc = localBankDB[inputAcc]
    while True:
        try:
            clear()
            userinp = int(input("""        [1] : Check Balance 
        [2] : Deposit
        [3] : Withdraw
        [4] : Exit Account
                > """))
            if (userinp == 1):
                print(f"Your Current Balance: {selectedAcc._currentBalance}$")
                print(f"Your Current Wallet Balance: {wallet}$")
            elif(userinp == 2):
                depositAmount = float(input("How much would you like to deposit > "))
                try: 
                    selectedAcc.deposit(depositAmount)
                    wallet -= depositAmount
                    print("Depositing Money ...ok")
                except Exception as e: print(e)

            elif(userinp == 3):
                attemptedWithdraw = float(input("How much would you like to withdraw > "))
                try:
                    withdrawAmount = selectedAcc.withdraw(attemptedWithdraw)
                    wallet += withdrawAmount
                    print("Withdraw Money ...ok")
                except Exception as e: print(e)

            elif(userinp == 4):
                print("Exiting Acount")
                break
            time.sleep(2)
        except:
            print("invalid input")
            time.sleep(2)
    showMainMenu()


#database functions VVV
with open ('accountDataBase.json', 'w') as A:
    json.dump([],A)
#resets database ^^^

def updateLocalData():
    with open ('accountDataBase.json', 'r') as A:
        global Gdata
        Gdata = (json.load(A))
def updateDatabase(*args:list):
    updateLocalData()
    try:
        allAcNum = [i['acountNumber'] for i in Gdata]
        for i in args:
            if i in localBankDB or i._acountNumber in allAcNum:
                raise TypeError ("One or More Inputed Accounts already exist")
            with open ('accountDataBase.json', 'w') as A:
                newData = Gdata
                newData.append(i.getInfo())
                json.dump(newData,A ,indent=4)
        for obj in args:
            localBankDB.append(obj)
        # updateLocalData()
    except Exception as e: print(e) ; time.sleep(2)
updateDatabase(defaultAc,checkingAc,savingAc)


#init call    
showMainMenu()
