import random
import threading
from for_print import error, enter, re_enter, success, prints, command
from managers.emailmanager import EmailManager
from managers.residentsmanager import ResidentsManager


def check_email(email: str) -> bool:
    # checks if the email is valid
    if 'mail.com' in email:
        return True
    else:
        return False


def check_code(verification_code: str) -> bool:
    # checks if the code is similar to the one that was sent
    received_code = input(enter + 'Enter code that you received: ')
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


def personal_page(username):
    text = """
1. Read my data
2. Update my data
3. Delete my account
"""
    print(command + text)
    user_input = input(enter + 'Enter your choice: ')
    if user_input == '1':
        print('Hello!')
        ResidentsManager(username).get_resident_data()
    elif user_input == '2':
        new_full_name = input(enter + "Enter your new full name: ")
        new_username = input(enter + "Enter your new username: ")
        if ResidentsManager(username).check_existence_by_username():
            new_email = input(enter + "Enter your new email: ")
            if check_email(new_email):
                verification_code = random.randint(10000, 99999)
                verification_code = str(verification_code)
                th1 = threading.Thread(target=verify_password, args=(new_email, verification_code,))
                th1.start()
                if check_code(verification_code):
                    if ResidentsManager(username).update_resident(new_full_name, new_username, new_email):
                        print(success + 'Successfully updated!')
                        resident_page(new_username)
    elif user_input == '3':
        if ResidentsManager(username).delete_resident():
            print(success + "Successfully deleted!")
            auth_menu()
    resident_page(username)


def resident_page(username):
    print(success + "Successfully logged in!")
    text = """
1. Personal Cabinet.
2. Requests page.
3. 
    """
    print(command + text)
    user_input = input(enter + "Choose an option: ")
    if user_input == '1':
        personal_page(username)
    elif user_input == '2':
        pass


def login_page():
    username = input(enter + 'Enter your username: ')
    password = input(enter + 'Enter your password: ')
    if ResidentsManager(username).check_existence_by_username():
        if ResidentsManager(username).check_password(password):
            resident_page(username)
    print(error + 'Username or password doesn\'t match')
    auth_menu()


def register_page():
    full_name = input(enter + 'Enter your full name: ')
    email = input(enter + 'Enter your email address: ')
    if check_email(email):
        verification_code = random.randint(10000, 99999)
        verification_code = str(verification_code)
        th1 = threading.Thread(target=verify_password, args=(email, verification_code,))
        th1.start()
        if check_code(verification_code):
            print(success + 'Your code has been verified!')
            username = input(enter + 'Enter your username: ')
            password = input(enter + 'Enter your password: ')
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
    print(command + text)
    user_input = input(enter + "Enter your choice: ")
    if user_input == "1":
        login_page()
    elif user_input == "2":
        register_page()
    elif user_input == "3":
        pass


if __name__ == "__main__":
    auth_menu()
