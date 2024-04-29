from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session, validates
import datetime

# Parametry połączenia z bazą danych
DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost/sqlalchemy'

# Nawiązywanie połączenia z bazą danych
engine = create_engine(DATABASE_URI)
Base = declarative_base()

# Definiowanie modelu tabeli dla samochodów
class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    max_speed = Column(Integer)
    color = Column(String)

    @validates('year')
    def validate_year(self, key, year):
        current_year = datetime.datetime.now().year
        if year > current_year or year < 1900:
            raise ValueError("Rok produkcji musi być między 1900 a obecnym rokiem.")
        return year

    @validates('max_speed')
    def validate_max_speed(self, key, max_speed):
        if max_speed < 0 or max_speed > 300:
            raise ValueError("Maksymalna prędkość musi być w zakresie 0-300 km/h.")
        return max_speed

    @validates('color')
    def validate_color(self, key, color):
        if not color:
            raise ValueError("Kolor musi być podany.")
        return color

# Tworzenie tabeli w bazie danych
Base.metadata.create_all(engine)

# Dodawanie samochodu (Create)
def add_car(make, model, year, max_speed, color):
    with Session(engine) as session:
        try:
            new_car = Car(make=make, model=model, year=year,
                          max_speed=max_speed, color=color)
            session.add(new_car)
            session.commit()
        except ValueError as e:
            print(f"Błąd przy dodawaniu samochodu: {e}")
            session.rollback()

# Pobieranie wszystkich samochodów (Read)
def get_all_cars():
    with Session(engine) as session:
        cars = session.query(Car).all()
        return cars

# Testowanie funkcji
add_car('Toyota', 'Corolla', 2020, 180, 'Czerwony')
add_car('Honda', 'Civic', 2019, 200, 'Niebieski')
add_car('Test', 'Invalid', 2050, 400, '')  # Nieprawidłowe dane, powinien pojawić się błąd

# Pobieranie i wyświetlanie wszystkich samochodów
print("\nWszystkie samochody:")
all_cars = get_all_cars()
for car in all_cars:
    print(f"{car.id}: {car.make}, {car.model}, {car.year}, {car.max_speed} km/h, {car.color}")
