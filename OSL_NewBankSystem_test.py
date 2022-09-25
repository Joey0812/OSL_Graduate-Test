
class Person(object):
    def __init__(self):
        self.UserName = ''
        self.Currency = ''
        self.Balance = 0
class Bank(object):
    dict1 = {}
    list1 = []

    #account creation
    def creation(self):
        per1 = Person()
        per1.UserName = input("Please enter your name：")
        per1.Currency = input("Please enter your currency(only HKD,USD,SGD)：")
        if not any([w in per1.Currency and w for w in ["HKD","USD","SGD"]]):
            print("Currency is invalid")
            print("*******Back to previous level*******")
            return -1
        else:
            c = per1.UserName
            Bank.dict1[c] = per1
            print("Account open successfully")
            return -1

    #deposit
    def deposit(self):         
            a = input("Please enter your username:")
            if a not in Bank.dict1.keys():
                print("Username does not exist")
                print("*******Back to previous level*******")
                return -1
            else:
                c = int(input("Please enter the amount of your deposit:"))
                if c <= 0:
                    print("The deposit amount must be positive")
                else:
                     Bank.dict1[a].Balance += c
                     print("Deposit successfully your current balance is:", Bank.dict1[a].Balance,Bank.dict1[a].Currency)
                     print("*******Back to previous level*******")
                     return -1
           
            
    #withdrawal
    def withdrawal(self):    
            a = input("Please enter your username:")
            if a not in Bank.dict1.keys():
                print("Username does not exist")
                print("*******Back to previous level*******")
                return -1
            else:
                c = int(input("Please enter the amount of your withdrawal:"))
                if c > Bank.dict1[a].Balance:
                    print("Insufficient balance,please re-enter the withdrawal amount")
                elif c <= 0:
                    print("The withdrawal amount must be positive")
                else:
                    Bank.dict1[a].Balance -= c
                    print("Withdrawal successful your current balance is:", Bank.dict1[a].Balance,Bank.dict1[a].Currency)
                    print("*******Back to previous level*******")
                    return -1
        
    #transfer
    def transfer(self):
        a = input("Please enter your username:")
        if a not in Bank.dict1.keys():
            print("Username does not exist")
            print("*******Back to previous level*******")
            return -1
        else:
            c = input("Please enter the username you want to transfer:")
            if c not in Bank.dict1.keys():
                print("Username does not exist")
                print("*******Back to previous level*******")
                return -1
            if a == c:
                print("Cannot transfer money to yourself")
                print("*******Back to previous level*******")
                return -1
            if Bank.dict1[a].Currency != Bank.dict1[c].Currency:
                print("Transfer can not happen between two accounts with two different currencies")
            else:
                d = int(input("Please enter the transfer amount:"))
                if d > Bank.dict1[a].Balance:
                    print("Insufficient balance,please re-enter the transfer amount")
                elif d <= 0:
                    print("The transfer amount must be positive")
                else:
                    Bank.dict1[a].Balance -= d
                    Bank.dict1[c].Balance += d
                    print("Transfer successfully your current balance is:", Bank.dict1[a].Balance,Bank.dict1[a].Currency)
                    print("*******Back to previous level*******")
                    return -1
    
    #List bank account balance
    def listBalance(self):
        a = input("Please enter your username:")
        if a not in Bank.dict1.keys():
            print("Username does not exist")
            print("*******Back to previous level*******")
            return -1
        else:
            print("Your balance is :",Bank.dict1[a].Balance,Bank.dict1[a].Currency)
            print("*******Back to previous level*******")
            return -1
    
    #display transaction statement
    def displayState(self):
        print("*******Back to previous level*******")
        return -1
    
        
    #main
    def bankSystem(self):
        print("WELCOME!")
        while 1:
            print("***************************************")
            print("*\t1、Account creation\n*\t2、Money deposit\n*\t3、Money withdrawal\n*\t4、Money transfer"
                  "\n*\t5、List bank account balance\n*\t6、Display transaction statement")
            print("***************************************")
            a = input("Please enter the number of operations:")
            if a == "1":
                self.creation()
            elif a == "2":
                self.deposit()
            elif a == "3":
                self.withdrawal()
            elif a == "4":
                self.transfer()
            elif a == "5":
                self.listBalance()
            elif a == "6":
                self.displayState()
            else:
                print("Incorrectly entered,please re-enter")
            
a = Bank()
a.bankSystem()


        
                 