# Wzorzec projektowy Mediator jest używany do zmniejszenia bezpośredniej 
# komunikacji między obiektami,
# centralizując komunikację poprzez jednego mediatora.

# Zalety:
# 1. Zmniejsza bezpośrednie zależności między klasami, co ułatwia 
#    ich rozszerzanie i utrzymanie.
# 2. Centralizuje kontrolę nad sposobem komunikacji między obiektami.

# Wady:
# 1. Mediator może stać się zbyt skomplikowany, jeśli koncentruje 
#    zbyt wiele logiki komunikacyjnej.

from abc import ABC, abstractmethod

# Klasa Mediator
class OrderMediator(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass

# Konkretne komponenty
class OrderDepartment:
    def __init__(self, mediator):
        self.mediator = mediator

    def receive_order(self, order_details):
        print(f"Dział zamówień otrzymał zamówienie: {order_details}")
        self.mediator.notify(self, "OrderReceived")

class Warehouse:
    def __init__(self, mediator):
        self.mediator = mediator

    def prepare_order(self):
        print("Magazyn przygotowuje zamówienie")
        self.mediator.notify(self, "OrderPrepared")

class DeliveryDepartment:
    def __init__(self, mediator):
        self.mediator = mediator

    def dispatch_order(self):
        print("Dział dostaw wysyła zamówienie")

# Konkretny Mediator
class ConcreteOrderMediator(OrderMediator):
    def __init__(self):
        self.order_department = OrderDepartment(self)
        self.warehouse = Warehouse(self)
        self.delivery_department = DeliveryDepartment(self)

    def notify(self, sender, event):
        if event == "OrderReceived":
            self.warehouse.prepare_order()
        elif event == "OrderPrepared":
            self.delivery_department.dispatch_order()

# Użycie wzorca Mediator
mediator = ConcreteOrderMediator()
mediator.order_department.receive_order("Pizza Margherita")

# W tym przykładzie:
# 'ConcreteOrderMediator' pełni rolę mediatora, koordynując komunikację 
# między różnymi działami.
# Działy 'OrderDepartment', 'Warehouse' i 'DeliveryDepartment' komunikują się 
# ze sobą za pośrednictwem
# mediatora, a nie bezpośrednio. Pozwala to na centralizację logiki przepływu 
# zamówień i jej łatwe zarządzanie.

