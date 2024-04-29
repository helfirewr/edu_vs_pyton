# Wzorzec projektowy Adapter jest używany do umożliwienia współpracy między klasami o 
# niekompatybilnych interfejsach. "Adaptuje" jeden interfejs dla drugiego.

# Zalety:
# 1. Umożliwia współpracę między klasami, które nie byłyby w stanie współpracować inaczej.
# 2. Oddziela i ukrywa szczegóły implementacji, umożliwiając klientowi 
#    korzystanie z interfejsu.

# Wady:
# 1. Komplikuje kod przez dodanie dodatkowych warstw.
# 2. Może prowadzić do nieporządnej architektury, jeśli jest nadużywany.

class OldPaymentSystem:
    def process_payment(self, amount):
        print(f"Przetwarzanie starej płatności w wysokości {amount}")

class NewPaymentSystem:
    def pay(self, amount):
        print(f"Przetwarzanie nowej płatności w wysokości {amount}")

# Klasa Adapter
class PaymentAdapter:
    def __init__(self, old_system):
        self.old_system = old_system

    def pay(self, amount):
        # Adaptuje interfejs starego systemu do nowego systemu
        self.old_system.process_payment(amount)

# Użycie wzorca Adapter
old_payment_system = OldPaymentSystem()
adapter = PaymentAdapter(old_payment_system)
new_payment_system = NewPaymentSystem()

# Nowy system płatności korzystający ze starego systemu za pośrednictwem adaptera
adapter.pay(100)  # Wywołuje stary system płatności

# Bezpośrednie użycie nowego systemu płatności
new_payment_system.pay(150)  # Wywołuje nowy system płatności
