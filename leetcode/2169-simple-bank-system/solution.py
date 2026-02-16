from collections import defaultdict
class Bank:

    def __init__(self, balance: List[int]):
        self.total = len(balance)
        self.accounts = balance     

    def isAccValid(self, acc):
        return 1 <= acc <= self.total

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.withdraw(account1, money):
            return False
        if not self.deposit(account2, money):
            self.deposit(account1, money)
            return False
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self.isAccValid(account):
            return False
        self.accounts[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.isAccValid(account):
            return False
        if self.accounts[account - 1] < money:
            return False
        self.accounts[account - 1] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
