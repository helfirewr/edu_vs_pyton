from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, Session, relationship, joinedload

# Parametry połączenia z bazą danych
DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost/sqlalchemy'

# Nawiązywanie połączenia z bazą danych
engine = create_engine(DATABASE_URI)
Base = declarative_base()

# Definiowanie modelu tabeli dla autorów
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    # back_populates używane jest do ustanowienia relacji dwustronnej
    # pomiędzy dwoma modelami. Dzięki temu, obiekty obu klas mogą "wiedzieć" o sobie
    # nawzajem i zachować spójność danych.
    # uselist=False jest używane, gdy oczekujemy, że relacja będzie zawierać
    # tylko jeden obiekt (relacja jeden do jednego)
    profile = relationship("UserProfile", back_populates="user", uselist=False)

# Definiowanie modelu tabeli dla profilów użytkowników
class UserProfile(Base):
    __tablename__ = 'user_profiles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    profile_picture = Column(String)
    user = relationship("User", back_populates="profile")

# Tworzenie tabel w bazie danych
Base.metadata.create_all(engine)

# Dodawanie użytkownika i profilu użytkownika
def add_user_with_profile(username, profile_picture):
    with Session(engine) as session:
        user = User(username=username)
        user_profile = UserProfile(profile_picture=profile_picture, user=user)
        session.add_all([user, user_profile])
        session.commit()

# Pobieranie wszystkich użytkowników wraz z profilami
def get_all_users_with_profiles():
    with Session(engine) as session:
        users = session.query(User).options(joinedload(User.profile)).all()
        return users

# Testowanie funkcji
add_user_with_profile('jan_kowalski', 'jan_profile_pic.jpg')
add_user_with_profile('anna_nowak', 'anna_profile_pic.jpg')

# Wyświetlanie użytkowników i ich profili
print("Użytkownicy i ich profile:")
all_users = get_all_users_with_profiles()
for user in all_users:
    profile_picture = user.profile.profile_picture if user.profile else "Brak profilu"
    print(f"Użytkownik: {user.username}, Zdjęcie profilowe: {profile_picture}")
