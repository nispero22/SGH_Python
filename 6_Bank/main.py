class Customer:
    last_id=0
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return 'Customer[{},{},{}]'.format(self.id, self.firstname, self.lastname)


class Account:
    last_id = 0
    def __init__(self, customer):
        self.customer = customer
        Account.last_id += 1
        self.id = Account.last_id
        self._balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise IncorrectAmountException("Incorrect amount", self._balance)
        self._balance += amount

    def charge(self, amount):
        if amount < 0:
            raise IncorrectAmountException("Incorrect amount", self._balance)
        if amount > self._balance:
            raise InsufficientBalanceException("Insufficient Balance, current balance is: " + str(self._balance), self._balance)
            #raise InsufficientBalanceException("Insufficient Balance, current balance is: " + self._balance)
        self._balance -= amount


    def __repr__(self):
        return '{}[{},{},{}]'.format(self.__class__.__name__, self.id, self.customer.lastname, self._balance)


class SavingsAccount(Account):
    def calc_interest(self,interest_rate):
        return interest_rate * self._balance

class CheckingAccount(Account):
    pass


class Bank:
    def __init__(self):
        self.account_list = []
        self.customer_list = []

# permet de sauvegarder dans la banque l'objet Customer que l'on a créé :
    def create_customer(self, firstname, lastname):
        c= Customer(firstname, lastname)
        self.customer_list.append(c)
        return c

    def create_account(self,customer, type_of_account):
        if type_of_account == "CheckingAccount":
            a = CheckingAccount(customer)
            self.account_list.append(a)
        elif type_of_account == "SavingsAccount":
            a = SavingsAccount(customer)
            self.account_list.append(a)
        else:
            raise MissingTypeOfAccount("Type of account not precised/not well entered")
        return a

    def transfer(self, from_acc_id, to_acc_id, amount):
        list_of_id = []
        for account in self.account_list:
            list_of_id.append(account.id)
        # check if the account in the bank
        if (not from_acc_id in list_of_id) or (not to_acc_id in list_of_id):
            raise AccountIsNotInTheBank("The account is not in the bank")

        for account in self.account_list:
            if account.id == from_acc_id:
                account.charge(amount)
        for account in self.account_list:
            if account.id == to_acc_id:
                account.deposit(amount)


    def __repr__(self):
        return 'Bank[{},{}]'.format(self.customer_list, self.account_list)


class BankException(Exception):
    def __init__(self, msg, balance=-100):
        super().__init__(msg)
        self.balance = balance

class IncorrectAmountException(BankException):
    pass

class InsufficientBalanceException(BankException):
    pass

class MissingTypeOfAccount(Exception):
    pass

class AccountIsNotInTheBank(Exception):
    pass






bank = Bank()

c1 = bank.create_customer('Anna', 'Smith')
print(c1)
c2 = bank.create_customer('John', 'Brown')
print(c2)
print('-------')
print(bank)
print('-------')



a1 = Account(c1)
a2 = Account(c2)
a3 = Account(c2)
print(a1)
print(a3.id)
try:
    a1.deposit(100)
    print(a1)
    b = 50
    #print('gsg' + b)
    a1.charge(150)
    print(a1)
except IncorrectAmountException as iae:
    print('Incorrect.. Exception raised: ' + str(iae))
except InsufficientBalanceException as iae:
    #print('Exception raised: ')
    print('Exception raised: ' + str(iae))
    print(iae.balance)
a1.charge(80)
print("a1",a1)



a4=SavingsAccount(c1)
print(a4)
print(isinstance(a4,SavingsAccount))
print(isinstance(a4,Account))


a6= bank.create_account(c2,"SavingsAccount")
a8= bank.create_account(c2,"CheckingAccount")
#a7= bank.create_account(c2,"SavingAccount")
print(a6)
print(bank)
print(c2.id)

print("----")


a6.deposit(600)
a8.deposit(3000)

print(a6._balance)
print(a8._balance)

bank.transfer(a6.id,a8.id,100)
print(a6)
print(a8)

print(bank)


# This should not work because the customer is not in the bank.
#c10=Customer("Audrey","Bernier")
#a10=SavingsAccount(c10)
#print(a10._balance)
#bank.transfer(a10.id,a6.id,100)
#print(a10)

