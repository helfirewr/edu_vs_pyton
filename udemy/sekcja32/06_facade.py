# Wzorzec projektowy Fasada (Facade) jest używany do zapewnienia uproszczonego interfejsu do
# skomplikowanego zestawu klas, biblioteki lub frameworka.

# Zalety:
# 1. Uproszczenie interfejsu: Klienci korzystają z jednego uproszczonego interfejsu zamiast bezpośrednio
#    z skomplikowanego systemu klas.
# 2. Rozdzielenie kodu klienta od skomplikowanego systemu: Ułatwia utrzymanie kodu i jego rozwój.

# Wady:
# 1. Może stać się trudna w utrzymaniu, jeśli fasada będzie mieć zbyt wiele funkcjonalności.
# 2. Może ograniczać użytkowników, którzy potrzebują większej kontroli nad skomplikowanym systemem.

class KitchenSystem:
    def prepare_dish(self, dish_name):
        return f"Przygotowano danie: {dish_name}"

class CustomerService:
    def take_order(self, order_details):
        return f"Zamówienie przyjęte: {order_details}"

class InventorySystem:
    def check_inventory(self, item_name):
        return f"Sprawdzono zapasy: {item_name}"

class RestaurantFacade:
    def __init__(self):
        self.kitchen = KitchenSystem()
        self.customer_service = CustomerService()
        self.inventory = InventorySystem()

    def place_order(self, dish_name):
        if self.inventory.check_inventory(dish_name):
            order_details = self.customer_service.take_order(dish_name)
            dish = self.kitchen.prepare_dish(dish_name)
            return f"{order_details}, {dish}"
        else:
            return "Danie nie jest dostępne"

# Użycie wzorca Fasada
restaurant = RestaurantFacade()
print(restaurant.place_order("Pizza Margherita"))

# W tym przykładzie:

# KitchenSystem, CustomerService i InventorySystem to skomplikowane podsystemy 
# wewnątrz restauracji.
# RestaurantFacade to fasada, która udostępnia uproszczony interfejs do interakcji 
# z tymi podsystemami.
# Klient (w tym przypadku właściciel restauracji lub menedżer) 
# interaguje z systemem za pośrednictwem fasady, co znacznie upraszcza 
# proces realizacji zamówienia.
