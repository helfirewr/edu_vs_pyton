class AccountManager:
    def __init__(self):
        self.user_data = {}  # Słownik przechowujący dane użytkownika: login i hasło
        self.logged_in = False  # Status zalogowania

    def register(self, username, password):
        if username in self.user_data:
            return "Username already exists."
        self.user_data[username] = password
        return "User registered successfully."

    def login(self, username, password):
        if username not in self.user_data:
            return "Username not found."
        if self.user_data[username] == password:
            self.logged_in = True
            return "Logged in successfully."
        return "Incorrect password."

    def logout(self):
        if self.logged_in:
            self.logged_in = False
            return "Logged out successfully."
        return "User not logged in."

    def change_password(self, username, old_password, new_password):
        if username not in self.user_data:
            return "Username not found."
        if self.user_data[username] == old_password:
            self.user_data[username] = new_password
            return "Password changed successfully."
        return "Incorrect old password."

    def is_logged_in(self):
        return self.logged_in
