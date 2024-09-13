import random
import threading

from managers.emailmanager import EmailManager
from managers.residentsmanager import ResidentsManager


def check_email(email: str) -> bool:
    # checks if the email is valid
    if '@gmail.com' in email:
        return True
    else:
        return False


def check_code(verification_code: str) -> bool:
    # checks if the code is similar to the one that was sent
    received_code = input('Enter code that you received: ')
    if received_code == verification_code:
        return True
    else:
        check_code(verification_code)
        return False


def verify_password(email: str, verification_code: str):
    # sends email to the user
    receiver = email
    subject = 'Verification Code'
    message = f'Here is your verification code: {verification_code}'
    if EmailManager(receiver, subject, message).send_email():
        print('Email is sent!\n')
        return True


def resident_page(username):
    print("Welcome to resident page!")


def login_page():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    if not ResidentsManager(username).check_existence_by_username():
        if ResidentsManager(username).check_password(password):
            pass
    print('Username or password doesn\'t match')
    auth_menu()


def register_page():
    full_name = input('Enter your full name: ')
    email = input('Enter your email address: ')
    if check_email(email):
        verification_code = random.randint(10000, 99999)
        verification_code = str(verification_code)
        th1 = threading.Thread(target=verify_password, args=(email, verification_code,))
        th1.start()
        if check_code(verification_code):
            print('Your code has been verified!')
            username = input('Enter your username: ')
            password = input('Enter your password: ')
            if not ResidentsManager(username).check_existence_by_username():
                if ResidentsManager(username).create_resident(full_name, email, password):
                    resident_page(username)

        else:
            print('Try again!')
    else:
        print('Invalid email!')
    auth_menu()


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
