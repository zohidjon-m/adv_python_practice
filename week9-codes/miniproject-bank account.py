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
        self.c
        pass

    # =====================================================
    # STEP 2 — Return the customer's name string.
    # =====================================================
    def getCName(self):
        # EXPLAIN: Simply return the stored name (self.cname).
        pass

    # =====================================================
    # STEP 3 — Return the customer's id (int).
    # =====================================================
    def getCid(self):
        # EXPLAIN: Simply return the stored id (self.cid).
        pass

    # =====================================================
    # STEP 4 — Return the customer's job string.
    # =====================================================
    def getCJob(self):
        # EXPLAIN: Simply return the stored job (self.cjob).
        pass

    # =====================================================
    # STEP 5 — Update the customer's job.
    # =====================================================
    def setCJob(self, new_job):
        # EXPLAIN: Assign new_job to self.cjob (no extra checks here).
        pass



# =========================================================
# STEP 6 — Define Account and STORE its three attributes:
#          customer (Customer), account_number (int),
#          balance (number).
# =========================================================
class Account:
    def __init__(self, customer, account_number, balance):
        # EXPLAIN: Save all three inputs to self:
        #   self.customer, self.account_number, self.balance
        pass

    # =====================================================
    # STEP 7 — Deposit: add `amount` to the current balance.
    # =====================================================
    def deposit(self, amount):
        # EXPLAIN: Increase self.balance by amount.
        pass

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
        pass

    # =====================================================
    # STEP 9 — Return the stored Customer object.
    # =====================================================
    def getCustomer(self):
        # EXPLAIN: Return self.customer.
        pass

    # =====================================================
    # STEP 10 — Return the stored account number (int).
    # =====================================================
    def getAccountNumber(self):
        # EXPLAIN: Return self.account_number.
        pass

    # =====================================================
    # STEP 11 — Return the current balance (number).
    # =====================================================
    def getBalance(self):
        # EXPLAIN: Return self.balance.
        pass



# =========================================================
# STEP 12 — Define BankAccounts that MANAGES many accounts.
#           STORE the incoming list in self.alist.
# =========================================================
class BankAccounts:
    def __init__(self, accounts):
        # EXPLAIN: Save the provided list reference into self.alist.
        pass

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
        pass

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
        pass

    # =====================================================
    # STEP 15 — Print each customer's name and their balance
    #           using the getters exactly like:
    #           print(i.getCustomer().getCName(), i.getBalance())
    # =====================================================
    def printAllCBalances(self):
        # EXPLAIN: Loop through self.alist and print as above.
        pass



############################################################
# STEP 16 — TEST SCENARIO (UNCOMMENT AFTER YOU IMPLEMENT)
############################################################
# c1 = Customer("Alice", 12345, "Student")
# c2 = Customer("Jack", 12333, "Teacher")
#
# c1_account = Account(c1, 100, 0)
# c2_account = Account(c2, 101, 5000)
#
# bas = BankAccounts([])
# bas.addAccount(c1_account)
# bas.addAccount(c2_account)
# bas.addAccount(c2_account)  # duplicate test (should print a warning)
#
# c1_account.deposit(20000)
# c1_account.withdraw(230)
# c2_account.withdraw(1500)
#
# bas.printAllCBalances()
# bas.removeAccount(c2_account)
# bas.printAllCBalances()
#####################################################################
######################################################################
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
        pass

    def withdraw(self, amount):
        # ToDo:
        #   • Check if balance - amount < min_balance.
        #   • If true → print "Cannot withdraw below minimum balance!"
        #   • Otherwise → call parent withdraw() using super().
        pass


# ============================================================
# STEP 2️⃣ – Create LoanAccount subclass
# ============================================================
class LoanAccount(Account):
    def __init__(self, customer, account_number, principal):
        # ToDo:
        #   Call parent constructor with super().__init__.
        #   For loans, the "balance" can be negative (principal owed).
        pass

    def withdraw(self, amount):
        # ToDo:
        #   Loan accounts do not allow withdrawal.
        #   Just print "Loans do not support direct withdrawal!"
        pass


# ============================================================
# STEP 3️⃣ – Demonstrate Polymorphism
# ============================================================
# ToDo:
#   Create one SavingsAccount and one LoanAccount.
#   Then loop through them in a list and call withdraw().
#   Each will behave differently even though the same method name is called.
#
# Example:
#   for acc in [sa, la]:
#       acc.withdraw(1000)
#
# EXPECTED BEHAVIOR:
#   SavingsAccount → checks min balance and possibly withdraws.
#   LoanAccount     → prints warning message only.
pass
