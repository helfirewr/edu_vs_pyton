import psycopg2

# Wzorzec projektowy Adapter jest używany do umożliwienia współpracy między klasami o niekompatybilnych interfejsach.

# Zalety:
# 1. Umożliwia współpracę klas, które nie mogłyby współpracować ze względu na niekompatybilne interfejsy.
# 2. Oddziela i ukrywa szczegóły implementacji klas od klienta.

# Wady:
# 1. Może komplikować kod, jeśli używany nadmiernie lub w niewłaściwym kontekście.
# 2. Zwiększa złożoność systemu poprzez dodatkową warstwę abstrakcji.

conn = psycopg2.connect(dbname="py_test", user="postgres", password="admin12345", host="localhost")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS payments;")
cur.execute("""
CREATE TABLE payments (
    id SERIAL PRIMARY KEY,
    transaction_id VARCHAR(100),
    amount DECIMAL,
    method VARCHAR(50)
);
""")
conn.commit()

class PaymentProcessor:
    def pay(self, transaction_id, amount):
        raise NotImplementedError

class PayPalPayment:
    def make_payment(self, paypal_transaction_id, amount):
        print(f"Processing PayPal payment: Transaction ID: {paypal_transaction_id}, Amount: {amount}")
        # Tutaj mogą znajdować się rzeczywiste wywołania API PayPal

class PayPalPaymentAdapter(PaymentProcessor):
    def __init__(self):
        self.paypal_payment = PayPalPayment()

    def pay(self, transaction_id, amount):
        self.paypal_payment.make_payment(transaction_id, amount)
        cur.execute("INSERT INTO payments (transaction_id, amount, method) VALUES (%s, %s, %s)",
                    (transaction_id, amount, "PayPal"))
        conn.commit()

class CreditCardPayment:
    def process_payment(self, card_transaction_id, amount):
        print(f"Processing credit card payment: Transaction ID: {card_transaction_id}, Amount: {amount}")
        # Tutaj mogą znajdować się rzeczywiste wywołania API do przetwarzania kart kredytowych

class CreditCardPaymentAdapter(PaymentProcessor):
    def __init__(self):
        self.credit_card_payment = CreditCardPayment()

    def pay(self, transaction_id, amount):
        self.credit_card_payment.process_payment(transaction_id, amount)
        cur.execute("INSERT INTO payments (transaction_id, amount, method) VALUES (%s, %s, %s)",
                    (transaction_id, amount, "CreditCard"))
        conn.commit()

# Użycie wzorca Adapter
paypal_adapter = PayPalPaymentAdapter()
paypal_adapter.pay("TRX123", 100.00)

credit_card_adapter = CreditCardPaymentAdapter()
credit_card_adapter.pay("TRX456", 200.00)

# Zamykanie połączenia z bazą danych
cur.close()
