import random
class Customer:
    def __init__(self, name, address, dob):
        self.name = name
        self.address = address
        self.dob = dob

class BankAccount:
    def __init__(self, account_number, customer):
        self.account_number = account_number
        self.customer = customer
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_balance(self):
        print(f"Account Balance for {self.customer.name}: ${self.balance}")


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f"Account added to {self.name}.")
    def get_accounts(self):
        li=[]
        for account in self.accounts:
            li.append(account.account_number)
        return li

    def display_all_accounts(self):
        print(f"All accounts in {self.name}:")
        for account in self.accounts:
            print(f"Account Number: {account.account_number}, Customer: {account.customer.name}")


# Example Usage:
if __name__ == "__main__":

    # Create a bank
    bank1 = Bank("ABC Bank")
    
    while True:
        print("1. New Customer 2. Existing Customer 3.Exit")
        choice=int(input())
        if choice==1:
            print("Customer Registration: \n")
            # Create a customer
            name=input("Enter Customer Name:")
            address=input('Enter Customer Address: ')
            dob=input("Enter Customer DOB: ")
            customer1 = Customer(name, address, dob)
            accnum=''.join(random.choice('1234567890') for i in range(6))
            # Create a bank account
            account1 = BankAccount(accnum, customer1)
            # Add the account to the bank
            bank1.add_account(account1)
            print("Your account Number is: ",accnum)
            bank1.display_all_accounts()
            print(bank1.get_accounts())
        elif choice==2:
            print("Welcome Back")
            acc_num=input("Enter Account number")
            if acc_num in bank1.get_accounts():
                while True:
                    print("1. Enter 1 to deposit\n2. Enter 2 to Withdrawl\n3. Enter 3 to Check the Balance\n4. Exit")
                    option=int(input("Enter your Option:\n"))
                    if option==1:
                        print("Welcome to Deposit Section\n")
                    
                        #print(bank1.get_accounts())
                        #if acc_num in list(bank1.accounts):
                        
                        deposit_amount=int(input("Enter Amount to deposit"))
                        account1.deposit(deposit_amount)
                        #print("Enter Correct Account Number")
                    elif option==2:
                        print("Welcome to withdrawl section:\n")
                        #acc_num=input("Enter Account number")
                        #if acc_num in bank1.accounts:
                        withdraw_amount=int(input('Enter the amount to withdraw:\n'))
                        account1.withdraw(withdraw_amount)
                        #print("Enter Correct Account Number")
                    elif option==3:
                        account1.display_balance()
                    elif option==4:
                        break
                    else:
                        print("Invalid Option")
            else:
                 print("Enter Correct account number")
            
        elif choice==3:
            break
        else:
            print("Invalid Option")
