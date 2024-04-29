import pytest
from account_manager import AccountManager

@pytest.fixture
def account_manager():
    """Fixture tworzący instancję AccountManager dla każdego testu, zapewniając świeże środowisko."""
    return AccountManager()

def test_register(account_manager):
    # Testuje rejestrację nowego użytkownika i sprawdza, czy zakończyła się sukcesem.
    result = account_manager.register("user1", "password123")
    # Sprawdza, czy użytkownik został zarejestrowany pomyślnie.
    assert result == "User registered successfully."
    # Sprawdza, czy dane użytkownika zostały dodane do słownika.
    assert "user1" in account_manager.user_data

def test_register_existing_user(account_manager):
    # Testuje próbę rejestracji użytkownika, który już istnieje, i oczekuje komunikatu o błędzie.
    account_manager.register("user1", "password123")  # Najpierw rejestruje użytkownika.
    result = account_manager.register("user1", "newpassword")  # Próbuje zarejestrować tego samego użytkownika ponownie.
    assert result == "Username already exists."  # Sprawdza, czy zwrócono komunikat o istniejącej już nazwie użytkownika.

def test_login(account_manager):
    # Testuje proces logowania dla zarejestrowanego użytkownika z prawidłowym hasłem.
    account_manager.register("user1", "password123")  # Najpierw rejestruje użytkownika.
    result = account_manager.login("user1", "password123")  # Następnie próbuje się zalogować z prawidłowym hasłem.
    assert result == "Logged in successfully."  # Sprawdza, czy logowanie zakończyło się sukcesem.
    assert account_manager.is_logged_in() == True  # Sprawdza, czy status zalogowania jest prawdziwy.

def test_login_with_wrong_password(account_manager):
    # Testuje próbę logowania z nieprawidłowym hasłem.
    account_manager.register("user1", "password123")  # Najpierw rejestruje użytkownika.
    result = account_manager.login("user1", "wrongpassword")  # Próbuje się zalogować z błędnym hasłem.
    assert result == "Incorrect password."  # Oczekuje komunikatu o błędnym haśle.

def test_logout(account_manager):
    # Testuje wylogowywanie zalogowanego użytkownika.
    # Najpierw rejestruje użytkownika i loguje go.
    account_manager.register("user1", "password123")
    account_manager.login("user1", "password123")
    # Następnie próbuje się wylogować.
    result = account_manager.logout()
    # Sprawdza, czy wylogowanie zakończyło się sukcesem.
    assert result == "Logged out successfully."
    # Sprawdza, czy status zalogowania jest fałszywy.
    assert account_manager.is_logged_in() == False

def test_change_password(account_manager):
    # Testuje zmianę hasła dla zarejestrowanego użytkownika.
    # Najpierw rejestruje użytkownika.
    account_manager.register("user1", "password123")
    # Następnie zmienia jego hasło.
    result = account_manager.change_password("user1", "password123", "newpassword")
    # Sprawdza, czy zmiana hasła zakończyła się sukcesem.
    assert result == "Password changed successfully."
    # Sprawdza, czy hasło zostało zmienione.
    assert account_manager.user_data["user1"] == "newpassword"

def test_change_password_with_incorrect_old_password(account_manager):
    # Testuje próbę zmiany hasła z użyciem błędnego starego hasła.
    account_manager.register("user1", "password123")  # Najpierw rejestruje użytkownika.

    # Próbuje zmienić hasło, używając błędnego starego hasła.
    result = account_manager.change_password("user1", "wrongpassword", "newpassword")

    # Oczekuje komunikatu o błędnym starym haśle.
    assert result == "Incorrect old password."

