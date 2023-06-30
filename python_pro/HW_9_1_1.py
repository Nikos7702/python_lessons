class Bill:
    def __init__(self, init_balance):
        self._balance = init_balance

    @property
    def balance(self):
        return self._balance

    def __setattr__(self, name, value):
        if name == "balance":
            raise AttributeError()
        else:
            super().__setattr__(name, value)

    def __getattr__(self, name):
        if name == "balance":
            raise AttributeError()
        else:
            raise AttributeError(f"'{name}' does not exist.")



account = Bill(1000)

print(account.balance)



