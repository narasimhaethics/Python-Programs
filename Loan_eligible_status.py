'''

The Metro Bank provides various types of loans such as car loans, business loans and house loans to its account holders. Write a python program to implement the following requirements:

Initialize the following variables with appropriate input values:account_number, account_balance, salary, loan_type, loan_amount_expected and customer_emi_expected.

The account number should be of 4 digits and its first digit should be 1.

The customer should have a minimum balance of Rupees 1 Lakh in the account.

If the above rules are valid, determine the eligible loan amount and the EMI that the bank can provide to its customers based on their salary and the loan type they expect to avail.

The bank would provide the loan, only if the loan amount and the number of EMI’s requested by the customer is less than or equal to the loan amount and the number of EMI’s decided by the bank respectively.

Display appropriate error messages for all invalid data. If all the business rules are satisfied ,then display account number, eligible and requested loan amount and EMI’s.
Test your code by providing different values for the input variables.

Salary    Loan type   Eligibleloan amount     No. of EMI’s required to repay

> 25000    Car        500000                           36

> 50000   House       6000000                          60

> 75000  Business     7500000                          84

'''

class CustomerApplication:
    __account_number=""
    __account_balance=""
    __salary=""
    __loantype=""
    __loan_amount_expected=""
    __customer_emi_expected=""
    def __init__(self,accnumber,accbalance,salary,loantype,loan_expected,emi_expected):
        self.__account_balance=accbalance
        self.__account_number=str(accnumber)
        self.__customer_emi_expected=emi_expected
        self.__loan_amount_expected=loan_expected
        self.__loantype=loantype
        self.__salary=salary
    def verifyAccountNumber(self):
        if len(self.__account_number)==4 and self.__account_number.startswith('1'):
            return True
        else:
            return False
    def check_minimum_balance(self):
        if self.__account_balance>=100000:
            return True
        else:
            return False
    def check_eligibility(self):
        if self.verifyAccountNumber():
            pass
        else:
            return "invalid account number"
        if self.check_minimum_balance():
            pass
        else:
            return "Minumum balance should be 100000"
        
        if self.verifyAccountNumber() and self.check_minimum_balance():
            if self.__salary>25000:
                if self.__loantype=="Car" and self.__loan_amount_expected<=500000 and self.__customer_emi_expected<=36:
                    return "Eligible for loan"
                if self.__salary>50000:
                    if self.__loantype=="House" and self.__loan_amount_expected<=6000000 and self.__customer_emi_expected<=60:
                        return "Eligible for loan"
                if self.__salary>75000:
                    if self.__loantype=="Business" and self.__loan_amount_expected<=7500000 and self.__customer_emi_expected<=84:
                        return "Eligible for loan"
            else:
                return "Minumum salary should be 25000 to avail loan"
        else:
            return "Not Eligible"
    
    def display_customer_loan_details(self):
        print("Account NUmber: ",self.__account_number)
        print("Account balance: ",self.__account_balance)
        print("Salary: ",self.__salary)
        print("Loan type: ",self.__loantype)
        print("EMI Expected: ",self.__customer_emi_expected)
        print("Loan Amount :",self.__loan_amount_expected)
        print(self.check_eligibility())

c1=CustomerApplication(1000,140000,45000,"Car",350000,24)
c1.check_eligibility()
c1.display_customer_loan_details()
