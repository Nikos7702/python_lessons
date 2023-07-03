from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

class CreditCard(PaymentMethod):
    def make_payment(self, amount):
        print(f"Made a payment of {amount} using a credit card.")

class BankTransfer(PaymentMethod):
    def make_payment(self, amount):
        print(f"Made a bank transfer of {amount}.")

class EWallet(PaymentMethod):
    def make_payment(self, amount):
        print(f"Made a payment of {amount} using an e-wallet.")

class PaymentProcessor:
    def __init__(self):
        self.payment_methods = []

    def add_payment_method(self, payment_method):
        self.payment_methods.append(payment_method)

    def process_payment(self, amount, payment_method_index):
        payment_method = self.payment_methods[payment_method_index]
        payment_method.make_payment(amount)

credit_card = CreditCard()
bank_transfer = BankTransfer()
e_wallet = EWallet()
payment_processor = PaymentProcessor()

payment_processor.add_payment_method(credit_card)
payment_processor.add_payment_method(bank_transfer)
payment_processor.add_payment_method(e_wallet)


payment_processor.process_payment(100, 0)
payment_processor.process_payment(200, 1)
payment_processor.process_payment(50, 2)