class regularAcount: 
    def __init__(self,acNum:int,acHolN:str,rateOInt:float,curBal:float):
        self._acountNumber = acNum
        self._acountHolderName = acHolN
        self._rateOfInterest = rateOInt
        self._currentBalance = curBal
#getters
        @property
        def _acountNumber(self):
            return self.__acountNumber
        @property
        def _acountHolderName(self):
            return self.__acountHolderName
        @property
        def _rateOfInterest(self):
            return self.__rateOfInterest
        @property
        def _currentBalance(self):
            return self.__currentBalance
#setteres
        @_acountNumber.setter
        def _acountNumber(self,args):
            print("setting _acountNumber")
            if (str(args).isnumeric() and isinstance(args,int)):
                self.__acountNumber = args
            else:   raise TypeError ("Error : Invaild Account Number")
        @_acountHolderName.setter
        def _acountHolderName(self,args):
            if (args.isalpha()):
                self.__acountHolderName = args
            else:   raise TypeError ("Error : Invaild Input")
        @_rateOfInterest.setter
        def _rateOfInterest(self,args):
            if isinstance(args,float):
                self.__rateOfInterest = args
            else:   raise TypeError ("Error : Invaild Interest Rate Number")
        @_currentBalance.setter
        def _currentBalance(self,args):
            if isinstance(args,float):
                self.__currentBalance = args
            else:raise TypeError ("Error : Invaild Balance Ammount / Number")
    def deposit(self,depositAmount):
        if (depositAmount > 0):
            self._currentBalance += depositAmount
        else:   raise TypeError("Transaction Declined : Invalid Amount")
        
    def withdraw(self,withdrawAmount):
        if (withdrawAmount <= self._currentBalance): #check if there is enough money
            self._currentBalance -= withdrawAmount
            return withdrawAmount
        else:   raise TypeError("Transaction Declined : Insufficient Funds")

    def getInfo(self):
        output ={
        "acountNumber" : self._acountNumber,
        "acountHolderName" : self._acountHolderName,
        "rateOfInterest" : self._rateOfInterest,
        "currentBalance" : self._currentBalance 
        }   
        return output

class savingAccount(regularAcount): 
    def __init__(self,acNum:int,acHolN:str,rateOInt:float,curBal:float,minBal:float):
        super().__init__(acNum,acHolN,rateOInt,curBal)
        self._minimumBalance = minBal
    def withdraw(self,withdrawAmount):
        #can only withdraw if left with more then minimumBalance amount
        if (self._currentBalance - withdrawAmount) >= self._minimumBalance: 
            self._currentBalance -= withdrawAmount
            return withdrawAmount
        else:  
            raise TypeError("Transaction Declined : Over Limit / Min Value")
    def getInfo(self):
        output ={
        "acountNumber" : self._acountNumber,
        "acountHolderName" : self._acountHolderName,
        "rateOfInterest" : self._rateOfInterest,
        "currentBalance" : self._currentBalance,
        "minimumBalance" :self._minimumBalance}
        return output
    
class checkingAcount(regularAcount): 
    def __init__(self,acNum:int,acHolN:str,rateOInt:float,curBal:float,ovrDraftLim :float):
        super().__init__(acNum,acHolN,rateOInt,curBal)
        self._overdraftAllowed = ovrDraftLim
    def withdraw(self,withdrawAmount):
        #can only withdraw if left with more then overdraft amount
        if (self._currentBalance - withdrawAmount) >= (0 - self._overdraftAllowed): 
            self._currentBalance -= withdrawAmount
            return withdrawAmount
        else:  
            raise TypeError("Transaction Declined : Insufficient Overdraft / Funds")
    def getInfo(self):
        output ={
        "acountNumber" : self._acountNumber,
        "acountHolderName" : self._acountHolderName,
        "rateOfInterest" : self._rateOfInterest,
        "currentBalance" : self._currentBalance,
        "overdraftAllowed" :self._overdraftAllowed
        }
        return output