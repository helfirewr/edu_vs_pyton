from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

# Parametry połączenia z bazą danych
DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost/sqlalchemy'

# Nawiązywanie połączenia z bazą danych
engine = create_engine(DATABASE_URI)
Base = declarative_base()

# Definiowanie modelu tabeli
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String)

# Tworzenie tabeli w bazie danych
Base.metadata.create_all(engine)

# Dodawanie użytkownika (Create)
def add_user(username, email):
    with Session(engine) as session:
        new_user = User(username=username, email=email)
        session.add(new_user)
        session.commit()

# Pobieranie wszystkich użytkowników (Read)
def get_all_users():
    with Session(engine) as session:
        users = session.query(User).all()
        return users

# Aktualizowanie użytkownika (Update)
def update_user(user_id, new_username, new_email):
    with Session(engine) as session:
        user_to_update = session.query(User).filter(User.id == user_id).one()
        user_to_update.username = new_username
        user_to_update.email = new_email
        session.commit()

# Usuwanie użytkownika (Delete)
def delete_user(user_id):
    with Session(engine) as session:
        user_to_delete = session.query(User).filter(User.id == user_id).one()
        session.delete(user_to_delete)
        session.commit()

# Testowanie funkcji
add_user('janek', 'janek@example.com')
add_user('anna', 'anna@example.com')

print("Users after adding:")
all_users = get_all_users()
for user in all_users:
    print(f"{user.id}: {user.username}, {user.email}")

update_user(1, 'janek_updated', 'updated_janek@example.com')

print("\nUsers after update:")
all_users = get_all_users()
for user in all_users:
    print(f"{user.id}: {user.username}, {user.email}")

delete_user(2)

print("\nUsers after delete:")
all_users = get_all_users()
for user in all_users:
    print(f"{user.id}: {user.username}, {user.email}")
