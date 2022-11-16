import acounts as A , os ,time
clear = lambda: os.system('clear')
centeramount = 50

#setting defaults
allAcounts = {}
wallet = 10000

defaultAc = A.regularAcount(0000,"default",2.2,5000)
allAcounts.update({defaultAc._acountNumber : defaultAc})

checkingAc = A.checkingAcount(1,"defaultChck",2.2,5001,200)
allAcounts.update({checkingAc._acountNumber : checkingAc})

savingAc = A.savingAccount(2,"defaultSave",2.2,5002,2000)
allAcounts.update({savingAc._acountNumber : savingAc})

def showMainMenu():
    while True: 
        clear()
        print("--Main Menu--".center(centeramount))
        print("""   [1] : Open Account
    [2] : Select Account
    [3] : Exit Application
        """)
        #testing
        # print(defaultAc._acountNumber)
        # print(allAcounts)
        
        try: 
            userinp = int(input("> "))
        #TODO open acount
            if userinp == 1:
                pass
            #DONE select account
            elif userinp == 2:
                print("All Acounts".center(centeramount))
                for acount in allAcounts.values():
                    print(f" : {acount._acountHolderName}")
                while True:
                    inpnum = int(input("Enter Account Number "))
                    if inpnum in allAcounts.keys():
                        showAccountMenu(allAcounts[inpnum])
                    else:
                        print("account doesnt exsist")
            #TODO exit Application  
            elif userinp == 3:
                print("EXITING Banking System")
                exit
                break
        except: print("invalid input")
        
def showAccountMenu(selectedAcc):
    global wallet
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
            #TODO check balance
            #TODO deposit
            #TODO withdraw
            #TODO exit account
            time.sleep(2)
        except:
            print("invalid input")
            time.sleep(2)
    showMainMenu()

#init call    
showMainMenu()