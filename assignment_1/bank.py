from datetime import datetime, date

class BankAccount:

    def __init__(self,account_number,account_holder):

        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self,amount):
       
        try:
            if amount <= 0  :
                raise ValueError
            else:
                self.balance += amount
                
                
                print("Amount ",amount,"/- Rs. is credited to Acoount no: ",self.account_number)
                
        except ValueError:
            print("Enter amount that is greater  than Zero!")
        line()
        
    def withdraw(self,amount):
      
        print("Initiating Withdrawal ",amount,"Rs...")
        try:
            if amount > self.balance:
                raise ValueError
            else:
                self.balance -= amount
                print("Amount ",amount,"/- Rs is Debited from account: ",self.account_number)
        except ValueError:
            print("No sufficient balance!")
        line()
        
    def get_balance(self):
        
        print(f"Account Balance for {self.account_holder} is {self.balance}/- Rs.")
        line()


    def __str__(self):
        return f"Account[{self.account_number}] - Holder: {self.account_holder}, Balance: {self.balance:.2f}"


def line():
    print("-" * 40)



class SavingsAccount(BankAccount):

    def __init__(self, account_number, account_holder,interest_rate):
        super().__init__(account_number, account_holder)
        self.intrest_rate = interest_rate
    
    def apply_interest(self):
        interest_amount = self.balance *(self.intrest_rate/100)
        self.balance += interest_amount
        print("Interest amount ",interest_amount," is added")
        line()

class CurrentAccount(BankAccount):

    def __init__(self, account_number, account_holder,overdraft_limit):
        super().__init__(account_number, account_holder)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        
        try:
            if (self.overdraft_limit + self.balance) >= amount :
                super().withdraw(amount)
            else:
                raise ValueError
        except ValueError:
            print("No sufficient balance!")
        
        line()



class FixedDepositAccount(BankAccount):
    def __init__(self, account_number, account_holder,amount,lock_in_period):
        super().__init__(account_number, account_holder)
        self.lock_in_period = datetime.strptime(lock_in_period, "%d-%m-%Y").date()
        self.balance = amount
    
    def withdraw(self, amount):
        if self.lock_in_period <= date.today():
            return super().withdraw(amount)
        else:
            print(f"Transaction failed: Your fixed deposit matures on {self.lock_in_period}. Please try after that date.")




class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}   # dictionary: account_number → account object

    def add_account(self, account):
        if account.account_number in self.accounts:
            print(f"Account {account.account_number} already exists in {self.name}.")
        else:
            self.accounts[account.account_number] = account
            print(f"Account {account.account_number} added successfully to {self.name}.")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def transfer_funds(self, from_acc_num, to_acc_num, amount):
        from_acc = self.get_account(from_acc_num)
        to_acc = self.get_account(to_acc_num)

        if from_acc is None:
            print(f"Source account {from_acc_num} not found in {self.name}.")
            return
        if to_acc is None:
            print(f"Destination account {to_acc_num} not found in {self.name}.")
            return

        print(f"\nInitiating transfer of {amount}/- Rs from {from_acc_num} to {to_acc_num}...")

 
        before_balance = from_acc.balance
        from_acc.withdraw(amount)

       
        if from_acc.balance < before_balance:
            to_acc.deposit(amount)
            print("Transfer successful")
        else:
            print("Transfer failed")





# ob = BankAccount(1,"Aswin")
# line()
# ob.deposit(100.0)
# ob.deposit(-10)
# ob.get_balance()
# ob.withdraw(55)
# ob.withdraw(70)
# ob.get_balance()
# print(ob)
# line()
# line()
# sb2=SavingsAccount(2,"unni",8.0)
# sb2.deposit(1000)
# sb2.apply_interest()
# sb2.get_balance()
# cb3 = CurrentAccount(3,"aryan",500.0)
# cb3.deposit(1000)
# cb3.withdraw(500)
# cb3.get_balance()
# cb3.withdraw(600)
# cb3.get_balance()
# cb3.withdraw(500)
# fd4 = FixedDepositAccount(4,"Ni",5000,"20-10-2024")
# fd4.withdraw(500)

if __name__ == "__main__":
    line()
    print(" BANK SYSTEM")
    line()

   
    my_bank = Bank("SBI")

   
    acc1 = BankAccount(101, "Aswin")                    
    acc2 = SavingsAccount(102, "Unni", 5.0)            
    acc3 = CurrentAccount(103, "Aryan", 500.0)          
    acc4 = FixedDepositAccount(104, "Nila", 5000, "20-10-2026")  

    my_bank.add_account(acc1)
    my_bank.add_account(acc2)
    my_bank.add_account(acc3)
    my_bank.add_account(acc4)

    line()
    print("Deposits")
    acc1.deposit(1000)
    acc2.deposit(2000)
    acc3.deposit(500)
    acc4.deposit(1000)  

    line()
    print("Withdrawals")
    acc1.withdraw(200)
    acc2.withdraw(300)
    acc3.withdraw(800)  
    acc3.withdraw(1000)
    acc4.withdraw(500) 

    line()
    print("Interest on Savings")
    acc2.apply_interest()
    acc2.get_balance()

    line()
    print("Transfer Funds")
    my_bank.transfer_funds(101, 102, 400)  
    my_bank.transfer_funds(103, 101, 200)  

    line()
    print("Final Balances")
    acc1.get_balance()
    acc2.get_balance()
    acc3.get_balance()
    acc4.get_balance()

    line()
  
