import hashlib
import random
import string
from datetime import datetime, timedelta

class User:
    def __init__(self, first_name, last_name, region, role):
        self.first_name = first_name
        self.last_name = last_name
        self.region = region
        self.role = role
        self.login = self.generate_login()
        self.password = self.generate_password()
        self.password_hash = self.hash_password(self.password)
        self.password_expiry = self.set_password_expiry()

    def generate_login(self):
        return (self.first_name[0] + self.last_name).lower()

    def generate_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for i in range(length))

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def set_password_expiry(self, days_valid=90):
        return datetime.now() + timedelta(days=days_valid)

    def __str__(self):
        return f"User(login={self.login}, region={self.region}, role={self.role})"

class Admin(User):
    def __init__(self, first_name, last_name, region, super_admin=False):
        super().__init__(first_name, last_name, region, 'admin')
        self.super_admin = super_admin

class UserManager:
    def __init__(self):
        self.users = []
        self.admins = []

    def add_user(self, first_name, last_name, region):
        user = User(first_name, last_name, region, 'user')
        self.users.append(user)
        return user

    def add_admin(self, first_name, last_name, region, super_admin=False):
        admin = Admin(first_name, last_name, region, super_admin)
        self.admins.append(admin)
        return admin

    def remove_user(self, login):
        self.users = [user for user in self.users if user.login != login]

    def remove_admin(self, login):
        self.admins = [admin for admin in self.admins if admin.login != login]

    def list_users(self, region=None, role=None):
        users = self.users
        if region:
            users = [user for user in users if user.region == region]
        if role:
            users = [user for user in users if user.role == role]
        return users

    def list_admins(self, region=None, super_admin=None):
        admins = self.admins
        if region:
            admins = [admin for admin in admins if admin.region == region]
        if super_admin is not None:
            admins = [admin for admin in admins if admin.super_admin == super_admin]
        return admins

# Example usage
if __name__ == "__main__":
    manager = UserManager()
    super_admin = manager.add_admin('John', 'Doe', 'Paris', super_admin=True)
    admin1 = manager.add_admin('Alice', 'Smith', 'Rennes')
    admin2 = manager.add_admin('Bob', 'Brown', 'Strasbourg')
    admin3 = manager.add_admin('Charlie', 'Davis', 'Grenoble')
    admin4 = manager.add_admin('Diana', 'Evans', 'Nantes')

    user1 = manager.add_user('Eve', 'Johnson', 'Rennes')
    user2 = manager.add_user('Frank', 'Miller', 'Strasbourg')

    print("All users:")
    for user in manager.list_users():
        print(user)

    print("\nAll admins:")
    for admin in manager.list_admins():
        print(admin)