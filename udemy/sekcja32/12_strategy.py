# Wzorzec projektowy Strategia jest używany do definiowania rodziny algorytmów,
# enkapsulując każdy z nich i umożliwiając ich wymienność.

# Zalety:
# 1. Umożliwia wymianę algorytmów w czasie działania programu.
# 2. Oddziela implementację algorytmu od jego użycia.
# 3. Może zwiększyć czytelność i organizację kodu.

# Wady:
# 1. Może prowadzić do zwiększenia liczby klas.
# 2. Klienci muszą zrozumieć różnice między strategiami.

from abc import ABC, abstractmethod

# Interfejs strategii
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Konkretne strategie
class BankTransferStrategy(PaymentStrategy):
    def pay(self, amount):
        print(f"Opłata {amount} zł zrealizowana przelewem bankowym.")

class BlikStrategy(PaymentStrategy):
    def pay(self, amount):
        print(f"Opłata {amount} zł zrealizowana za pomocą BLIK.")

class PostalOrderStrategy(PaymentStrategy):
    def pay(self, amount):
        print(f"Opłata {amount} zł zrealizowana przekazem pocztowym.")

# Kontekst wykorzystujący strategię
class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def execute_payment(self, amount):
        self.strategy.pay(amount)

# Użycie wzorca Strategia
amount = 100
payment_processor = PaymentProcessor(BankTransferStrategy())
payment_processor.execute_payment(amount)

payment_processor.strategy = BlikStrategy()
payment_processor.execute_payment(amount)

payment_processor.strategy = PostalOrderStrategy()
payment_processor.execute_payment(amount)

# W tym przykładzie:
# 'PaymentStrategy' to interfejs strategii, a 'BankTransferStrategy', 'BlikStrategy',
# i 'PostalOrderStrategy' to konkretne implementacje tej strategii.
# 'PaymentProcessor' używa różnych strategii płatności, które mogą być wymieniane
# w zależności od potrzeb użytkownika.

