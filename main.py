from managers import residentsmanager
from managers.residentsmanager import ResidentsManager

def check_email(email):

def login_page():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    if ResidentsManager(username).check_existence_by_username():
        if ResidentsManager(username).check_password(password):
            pass
    print('Username or password doesn\'t match')
    auth_menu()


def register_page():
    full_name = input('Enter your full name: ')
    email = input('Enter your email address: ')



def auth_menu() -> None:
    text = """
    1. Login
    2. Register
    3. Logout
    """
    user_input = input(text)
    if user_input == "1":
        login_page()
    elif user_input == "2":
        register_page()
    elif user_input == "3":
        pass


if __name__ == "__main__":
    auth_menu()
