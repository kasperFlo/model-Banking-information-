
class regularAcount:  
    instances = []

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
            self.__acountNumber = args
        @_acountHolderName.setter
        def _acountHolderName(self,args):
            self.__acountHolderName = args
        @_rateOfInterest.setter
        def _rateOfInterest(self,args):
            self.__rateOfInterest = args
        @_currentBalance.setter
        def _currentBalance(self,args):
            self.__currentBalance = args
    def deposit(self):
        pass
    def withdraw(self):
        pass
    def __str__(self) -> str:
        return f"{self._acountNumber} {self._acountHolderName} {self._rateOfInterest} {self._currentBalance}"


class savingAccount(regularAcount): 
    def __init__(self,acNum:int,acHolN:str,rateOInt:float,curBal:float,minBal:float):
        super.__init__(acNum,acHolN,rateOInt,curBal)
        self._minimumBalance = minBal
    def caWithdraw(self,withdrawAmount):
        #can only withdraw if left with more then minimumBalance amount
        if (self._currentBalance - withdrawAmount) < self._minimumBalance: 
            self._currentBalance -= withdrawAmount
            return withdrawAmount
        else:  
            return None

class checkingAcount(regularAcount): 
    def __init__(self,acNum:int,acHolN:str,rateOInt:float,curBal:float,ovrDraftLim :float):
        super.__init__(acNum,acHolN,rateOInt,curBal)
        self._overdraftAllowed = ovrDraftLim
    def saWithdraw(self,withdrawAmount):
        #can only withdraw if left with more then minimumBalance minus overdraft amount
        if (self._currentBalance - withdrawAmount) < self._minimumBalance - self._overdraftAllowed: 
            self._currentBalance -= withdrawAmount
            return withdrawAmount
        else:  
            return None
    

