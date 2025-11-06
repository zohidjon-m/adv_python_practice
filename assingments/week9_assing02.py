############################################################
# Assignment: PremiumAccount using Multiple Inheritance
#
# Replace ONLY each `pass` with correct code.
# DO NOT remove or modify comments or class names.
############################################################

# =========================================================
# STEP 1 — Base banking behavior: Account 
# =========================================================
class Account:
    def __init__(self, customer, account_number, balance):
        # TODO 1: Save inputs to instance variables
        self.customer = customer
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        # TODO 2: Increase balance by amount
        self.balance += amount

    def withdraw(self, amount):
        # TODO 3: If enough balance, subtract; else print:
        #         "You do not have sufficient funds to make this withdrawal!"
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("You do not have sufficient funds to make this withdrawal!")

    def getBalance(self):
        # TODO 4: Return current balance
        return self.balance


# =========================================================
# STEP 2 — OnlineService mixin 
# =========================================================
class OnlineService:
    def login(self):
        # TODO 5: Print exactly:
        #         "User logged in via online portal"
        print("User logged in via online portal")


# =========================================================
# STEP 3 — RewardMixin 
# =========================================================
class RewardMixin:
    def apply_reward(self):
        # TODO 6: Print exactly:
        #         "Reward points applied to your account"
        print("Reward points applied to your account")


# =========================================================
# STEP 4 — PremiumAccount combining all behaviors 
# At least 3 parent classes: Account, OnlineService, RewardMixin
# =========================================================
class PremiumAccount(Account, OnlineService, RewardMixin):
    def __init__(self, customer, account_number, balance):
        # TODO 7: Call Account constructor using super()
        super().__init__(customer, account_number, balance)

    def bonus_interest(self):
        # TODO 8: Print exactly:
        #         "5% bonus interest applied"
        print("5% bonus interest applied")


# =========================================================
# STEP 5 — Minimal Customer helper class 
# =========================================================
class Customer:
    def __init__(self, cname):
        # TODO 9: Save cname
        self.cname = cname

    def getCName(self):
        # TODO 10: Return cname
        return self.cname


############################################################
# TEST CASE (You must keep this code unchanged)

# Expected output:
# User logged in via online portal
# Reward points applied to your account
# 5% bonus interest applied
# 12000
###########################################################
c1 = Customer("Aylin")
pa = PremiumAccount(c1, 300, 10000)
pa.login()            # from OnlineService
pa.apply_reward()     # from RewardMixin
pa.bonus_interest()   # from PremiumAccount
pa.deposit(2000)      # from Account
print(pa.getBalance())
