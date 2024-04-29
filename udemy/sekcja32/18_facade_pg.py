import psycopg2

# Wzorzec projektowy Fasada jest używany do stworzenia uproszczonego interfejsu dla złożonego systemu.

# Zalety:
# 1. Uproszczenie interfejsu: Ułatwia korzystanie ze skomplikowanych systemów poprzez zapewnienie prostszego interfejsu.
# 2. Izolacja klienta od złożonych podsystemów: Klient nie musi znać szczegółów wewnętrznych podsystemów.

# Wady:
# 1. Może stać się God Object , jeśli za dużo funkcjonalności będzie zgrupowane w jednej fasadzie.
# 2. Może ograniczać elastyczność klienta, który chce używać tylko części skomplikowanego systemu.

conn = psycopg2.connect(dbname="py_test", user="postgres", password="admin12345", host="localhost")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS orders;")
cur.execute("DROP TABLE IF EXISTS delivery_methods;")
cur.execute("""
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100),
    product_name VARCHAR(100)
);
""")
cur.execute("""
CREATE TABLE delivery_methods (
    id SERIAL PRIMARY KEY,
    order_id INT,
    method VARCHAR(100),
    cost DECIMAL
);
""")
conn.commit()

class DeliverySubsystem:
    def select_delivery_method(self, order_id, method):
        if method == "standard":
            cost = 10.00
        elif method == "express":
            cost = 20.00
        else:
            raise ValueError("Nieznana metoda dostawy")
        
        cur.execute("INSERT INTO delivery_methods (order_id, method, cost) VALUES (%s, %s, %s) RETURNING id;",
                    (order_id, method, cost))
        delivery_id = cur.fetchone()[0]
        conn.commit()
        return delivery_id

class OrderSubsystem:
    def place_order(self, customer_name, product_name):
        cur.execute("INSERT INTO orders (customer_name, product_name) VALUES (%s, %s) RETURNING id;",
                    (customer_name, product_name))
        order_id = cur.fetchone()[0]
        conn.commit()
        return order_id

class DeliveryFacade:
    def __init__(self):
        self.order_subsystem = OrderSubsystem()
        self.delivery_subsystem = DeliverySubsystem()

    def place_order_with_delivery(self, customer_name, product_name, delivery_method):
        order_id = self.order_subsystem.place_order(customer_name, product_name)
        delivery_id = self.delivery_subsystem.select_delivery_method(order_id, delivery_method)
        return order_id, delivery_id

# Użycie wzorca Fasada
delivery_facade = DeliveryFacade()
order_id, delivery_id = delivery_facade.place_order_with_delivery("Jan Kowalski", "Laptop", "express")
print(f"Zamówienie ID: {order_id}, Dostawa ID: {delivery_id}")

