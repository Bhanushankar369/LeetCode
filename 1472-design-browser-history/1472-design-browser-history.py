class BrowserHistory:

    def __init__(self, homepage: str):
        self.urls = [homepage]
        self.ind = 0

    def visit(self, url: str) -> None:
        self.urls = self.urls[:self.ind+1]
        self.urls.append(url)
        self.ind += 1

    def back(self, steps: int) -> str:
        self.ind = max(0, self.ind - steps)
        return self.urls[self.ind]

    def forward(self, steps: int) -> str:
        self.ind = min(len(self.urls)-1, self.ind + steps)
        return self.urls[self.ind]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)