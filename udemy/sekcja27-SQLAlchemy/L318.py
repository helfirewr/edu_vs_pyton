from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.orm import declarative_base, Session
from tkinter import Tk, Label, Button
import random

# Parametry połączenia z bazą danych
DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost/sqlalchemy'
engine = create_engine(DATABASE_URI)
Base = declarative_base()

class Quote(Base):
    __tablename__ = 'quotes'
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)

def init_db():
    Base.metadata.create_all(engine)
    quotes = [
        "Życie jest albo śmiałą przygodą, albo niczym. - Helen Keller",
        "To, co robimy dla siebie, umiera z nami. To, co robimy dla innych i świata, pozostaje i jest nieśmiertelne. - Albert Pine",
        "Dwóch rzeczy nie możemy wybrać: epoki, w której mamy żyć, i rodziny, w której mamy się urodzić. - Kofi Annan",
        "Jedyną rzeczą, której musimy się bać, jest strach sam w sobie. - Franklin D. Roosevelt",
        "Bądź zmianą, którą chcesz zobaczyć w świecie. - Mahatma Gandhi",
        "Inteligencja to zdolność do adaptacji do zmian. - Stephen Hawking",
        "Nigdy nie bój się podnosić do góry; powoli, nagle, będziesz żył wśród gwiazd. - Virginia Woolf",
        "Nasze życie zaczyna się kończyć w dniu, w którym milkniemy w ważnych kwestiach. - Martin Luther King Jr.",
        "Najważniejsze jest to, by nie przestawać zadawać pytań. - Albert Einstein",
        "Jedynym sposobem, aby zrobić świetną pracę, jest kochanie tego, co robisz. - Steve Jobs"
    ]

    with Session(engine) as session:
        if session.query(Quote).count() == 0:
            for quote_text in quotes:
                session.add(Quote(text=quote_text))
            session.commit()

def show_random_quote():
    with Session(engine) as session:
        quote_count = session.query(Quote).count()
        random_id = random.randint(1, quote_count)
        random_quote = session.execute(select(Quote).where(Quote.id == random_id)).scalar_one()
        quote_label.config(text=random_quote.text)

init_db()

root = Tk()
root.title("Losowy cytat")
root.geometry("500x250")  # Zwiększenie rozmiaru okna

quote_label = Label(root, text="", wraplength=480)
quote_label.pack(pady=20)

# wraplength określa długość, po której tekst zostanie zawinięty do nowej linii.
random_quote_button = Button(root, text="Losowy cytat", command=show_random_quote)
random_quote_button.pack(pady=10)

# Funkcja wywoływana przy zamykaniu okna
def on_closing():
    engine.dispose()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Wyświetlenie losowego cytatu przy starcie aplikacji
show_random_quote()

root.mainloop()
