# Parent class
class BankAccount:
    def __init__(self, balance, account_number): #class attribute (balance, account_number)
        self. balance = balance
        self.account_number = account_number

        #creating the class methods
    def deposit(self):
            print(f"You depositted R{self.balance} into account number {self.account_number}")
            #pass
    def withdraw(self):
            print(f"You withdrew R{self.balance} from {self.account_number}")
            #pass
    def check_balance(self):
            print(f"""Account: {self.account_number}
Balance: R{self.balance}""")
            #pass

#creating the bank account object
bank_account = BankAccount(2500, 1693446679)

#accesdding the attributes
print(bank_account.balance) #prints the value of the balance attribute
print(bank_account.account_number) #prints the value of the account_number attribute

#calling the methods
bank_account.deposit()
bank_account.withdraw()
bank_account.check_balance()

#INHERITANCE
#creating a subclass that claculates interest on the balance
class InterestAccount(BankAccount):
      def __init__(self,balance, account_number, interest):
            pass