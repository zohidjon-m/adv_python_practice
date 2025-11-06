############################################################
# BANK SYSTEM mini project
# Classes: Customer, Account, BankAccounts
# Instructions: Follow each STEP note and replace `pass`
# with your own implementation exactly as described.
############################################################


# =========================================================
# STEP 1 — Define Customer and STORE the three attributes
#          (name, id, job) given to __init__.
# =========================================================
class Customer:
    def __init__(self, cname, cid, cjob):
        # EXPLAIN: Save all three inputs into instance variables on self.
        #   self.cname should hold cname
        #   self.cid   should hold cid
        #   self.cjob  should hold cjob
        self.cname = cname
        self.cid = cid
        self.cjob = cjob

    # =====================================================
    # STEP 2 — Return the customer's name string.
    # =====================================================
    def getCName(self):
        # EXPLAIN: Simply return the stored name (self.cname).
        return self.cname

    # =====================================================
    # STEP 3 — Return the customer's id (int).
    # =====================================================
    def getCid(self):
        # EXPLAIN: Simply return the stored id (self.cid).
        return self.cid

    # =====================================================
    # STEP 4 — Return the customer's job string.
    # =====================================================
    def getCJob(self):
        # EXPLAIN: Simply return the stored job (self.cjob).
        return self.cjob

    # =====================================================
    # STEP 5 — Update the customer's job.
    # =====================================================
    def setCJob(self, new_job):
        # EXPLAIN: Assign new_job to self.cjob (no extra checks here).
        self.cjob = new_job



# =========================================================
# STEP 6 — Define Account and STORE its three attributes:
#          customer (Customer), account_number (int),
#          balance (number).
# =========================================================
class Account:
    def __init__(self, customer, account_number, balance):
        # EXPLAIN: Save all three inputs to self:
        #   self.customer, self.account_number, self.balance
        self.customer = customer
        self.account_number = account_number
        self.balance = balance

    # =====================================================
    # STEP 7 — Deposit: add `amount` to the current balance.
    # =====================================================
    def deposit(self, amount):
        # EXPLAIN: Increase self.balance by amount.
        self.balance += amount

    # =====================================================
    # STEP 8 — Withdraw:
    #   - If amount <= balance: subtract and succeed
    #   - Else: print the exact message below.
    #     "You do not have sufficient funds to make this withdrawal!"
    # =====================================================
    def withdraw(self, amount):
        # EXPLAIN: Compare amount with self.balance.
        #   If enough → update balance.
        #   Otherwise → print the message exactly as shown.
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("You do not have sufficient funds to make this withdrawal!")

    # =====================================================
    # STEP 9 — Return the stored Customer object.
    # =====================================================
    def getCustomer(self):
        # EXPLAIN: Return self.customer.
        return self.customer

    # =====================================================
    # STEP 10 — Return the stored account number (int).
    # =====================================================
    def getAccountNumber(self):
        # EXPLAIN: Return self.account_number.
        return self.account_number

    # =====================================================
    # STEP 11 — Return the current balance (number).
    # =====================================================
    def getBalance(self):
        # EXPLAIN: Return self.balance.
        return self.balance



# =========================================================
# STEP 12 — Define BankAccounts that MANAGES many accounts.
#           STORE the incoming list in self.alist.
# =========================================================
class BankAccounts:
    def __init__(self, accounts):
        # EXPLAIN: Save the provided list reference into self.alist.
        self.alist = accounts

    # =====================================================
    # STEP 13 — Add an Account object if it is not already in
    #           the list by IDENTITY (same object instance).
    #           If duplicate, print:
    #           "This account has already been added"
    # =====================================================
    def addAccount(self, account):
        # EXPLAIN: Loop over self.alist and compare with `is`.
        #   If found → print the message and return.
        #   Else → append account to self.alist.
        for a in self.alist:
            if a is account:
                print("This account has already been added")
                return
        self.alist.append(account)

    # =====================================================
    # STEP 14 — Remove an Account object by IDENTITY.
    #           Use a counter to track index as you loop.
    #           If found → pop and return.
    #           If not found → after loop print:
    #           "This account does not exist!"
    # =====================================================
    def removeAccount(self, account):
        # EXPLAIN: Walk through self.alist with a manual index (counter).
        #   If account is the same object as an element → pop and return.
        #   If loop ends with no match → print the message.
        idx = 0
        while idx < len(self.alist):
            if self.alist[idx] is account:
                self.alist.pop(idx)
                return
            idx += 1
        print("This account does not exist!")

    # =====================================================
    # STEP 15 — Print each customer's name and their balance
    #           using the getters exactly like:
    #           print(i.getCustomer().getCName(), i.getBalance())
    # =====================================================
    def printAllCBalances(self):
        # EXPLAIN: Loop through self.alist and print as above.
        for i in self.alist:
            print(i.getCustomer().getCName(), i.getBalance())



############################################################
# STEP 16 — TEST SCENARIO (UNCOMMENT AFTER YOU IMPLEMENT)
############################################################
c1 = Customer("Alice", 12345, "Student")
c2 = Customer("Jack", 12333, "Teacher")

c1_account = Account(c1, 100, 0)
c2_account = Account(c2, 101, 5000)

bas = BankAccounts([])
bas.addAccount(c1_account)
bas.addAccount(c2_account)
# bas.addAccount(c2_account)  # duplicate test (should print a warning)

# c1_account.deposit(20000)
# c1_account.withdraw(230)
# c2_account.withdraw(1500)


# bas.printAllCBalances()
# bas.removeAccount(c2_account)

# bas.printAllCBalances()
#####################################################################
# ######################################################################
# ---------- Polymorphism ----------
# Goal: Show different behaviors for the same method (withdraw)
#       depending on account type.

# ============================================================
# STEP 1️⃣ – Create SavingsAccount subclass
# ============================================================
class SavingsAccount(Account):
    def __init__(self, customer, account_number, balance, min_balance=500):
        # ToDo:
        #   Use super().__init__ to call the parent Account constructor.
        #   Then store the minimum allowed balance (min_balance).
        super().__init__(customer, account_number, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        # ToDo:
        #   • Check if balance - amount < min_balance.
        #   • If true → print "Cannot withdraw below minimum balance!"
        #   • Otherwise → call parent withdraw() using super().
        if self.balance - amount < self.min_balance:
            print("Cannot withdraw below minimum balance!")
        else:
            super().withdraw(amount)


# ============================================================
# STEP 2️⃣ – Create LoanAccount subclass
# ============================================================
class LoanAccount(Account):
    def __init__(self, customer, account_number, principal):
        # ToDo:
        #   Call parent constructor with super().__init__.
        #   For loans, the "balance" can be negative (principal owed).
        super().__init__(customer, account_number, principal)

    def withdraw(self, amount):
        # ToDo:
        #   Loan accounts do not allow withdrawal.
        #   Just print "Loans do not support direct withdrawal!"
        print("Loans do not support direct withdrawal!")


# ============================================================
# STEP 3️⃣ – Demonstrate Polymorphism
# ============================================================
# ToDo:
#   Create one SavingsAccount and one LoanAccount.
#   Then loop through them in a list and call withdraw().
#   Each will behave differently even though the same method name is called.
sa = SavingsAccount(Customer("Alice", 111, "Doctor"), 201, 2000, 500)
la = LoanAccount(Customer("Bob", 222, "Engineer"), 202, -5000)

for acc in [sa, la]:
    acc.withdraw(1000)

