# Parent class
class BankAccount:
    def __init__(self, balance, account_number): #class attribute (balance, account_number)
        self. balance = balance
        self.account_number = account_number

        #creating the class methods
    def deposit(self, amount):
            if amount > 0:
                self.balance += amount
                print(f"You depositted R{amount} into account number {self.account_number}")
            else:
                  print("Invalid amount")

            #pass
    def withdraw(self, amount):
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                print(f"You withdrew R{amount} from {self.account_number}")
            else:
                  print("Invalid withdrawal or insufficiant funds")
            #pass
    def check_balance(self):
            print(f"""Account: {self.account_number}
Balance: R{self.balance}""")
            #pass

# #creating the bank account object


# #accesdding the attributes
# print(bank_account.balance) #prints the value of the balance attribute
# print(bank_account.account_number) #prints the value of the account_number attribute

# #calling the methods

# 
# bank_account.check_balance()

#INHERITANCE
#creating a subclass that claculates interest on the balance
class InterestAccount(BankAccount): # Child class
      def __init__(self,balance, account_number, interest_rate=0.01):
            super().__init__(balance, account_number)
            self.interest_rate = interest_rate

      def calculate_interest(self):
            interest = self.balance * self.interest_rate
            self.deposit(interest)
            print(f"Interested calculated: R{interest}")

bank_account = BankAccount(2500, 1693446679)
bank_account.deposit(100)
bank_account.withdraw(500)
bank_account.check_balance()
# interest account
interest = InterestAccount(1200, 1693446679, 0.1)
interest.calculate_interest()
interest.check_balance()
