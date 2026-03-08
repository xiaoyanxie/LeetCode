class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.index = 0

    def visit(self, url: str) -> None:
        """
        ["leetcode.com", "google.com", "facebook.com", "linkedin.com"]
               i
        """
        while len(self.history) > self.index + 1:
            self.history.pop()
        
        assert self.index == len(self.history) - 1
        assert len(self.history) > 0
        self.history.append(url)
        self.index += 1

    def back(self, steps: int) -> str:
        if self.index - steps >= 0:
            self.index -= steps
        else:
            self.index = 0
        return self.history[self.index]

    def forward(self, steps: int) -> str:
        if self.index + steps < len(self.history):
            self.index += steps
        else:
            self.index = len(self.history) - 1
        return self.history[self.index]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
