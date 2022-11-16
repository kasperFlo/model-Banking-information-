import acounts as A , os
clear = lambda: os.system('cls')
centeramount = 20

#setting defaults
allAcounts = {}
wallet = 0
defaultAc = A.regularAcount(0000,"default",2.2,5000)
allAcounts.update({defaultAc._acountNumber : defaultAc})

def showMainMenu():
    while True: 
        print("""
        [1] : Open Account
        [2] : Select Account
        [3] : Exit Application
        """)
        userinp = int(input("> "))
        #TODO open acount
        if userinp == 1:
            pass

        #TODO select account
        elif userinp == 2:
            print("All Acounts".center(centeramount))
            for acount in enumerate(allAcounts.values()):
                print(f"[{acount[0]+1}] : {acount[1]._acountHolderName}")
            while True:
                inpnum = input("Enter Account Number ")
                if inpnum in allAcounts.keys():
                    selectedAcc = allAcounts[inpnum]
                    showAccountMenu(selectedAcc)
                else:
                    print("account doesnt exsist")
        #TODO exit Application  
        elif userinp == 3:
            print("EXITING")
            exit
        
        
        pass
        
def showAccountMenu(selectedAcc):
    pass
    #TODO check balance
    #TODO deposit
    #TODO withdraw
    #TODO exit account

showMainMenu()