class Bank:

    def __init__(self, balance: List[int]):
        self.accounts = [0] * (len(balance) + 1)
        for i, b in enumerate(balance):
            self.accounts[i + 1] = b
        self.n = len(balance)

        """
        accounts: {
            0: 0,
            1: 10,
            2: 100,
            3: 10,
            4: 50,
            5: 30
        }
        """

    def isValidAccNo(self, accNo):
        return 1 <= accNo <= self.n

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.isValidAccNo(account1) or not self.isValidAccNo(account2) or self.accounts[account1] < money:
            return False
        
        self.accounts[account1] -= money
        self.accounts[account2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self.isValidAccNo(account):
            return False
        self.accounts[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.isValidAccNo(account) or self.accounts[account] < money:
            return False
        
        self.accounts[account] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
