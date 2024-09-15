# admin username and password == 'admin'
import random
import threading
from for_print import error, enter, success, command
from managers.emailmanager import EmailManager
from managers.residentsmanager import ResidentsManager
from managers.regionsmanagers import RegionsManagers
from managers.districtsmanagers import DistrictsManager
from managers.requestsmanager import RequestsManager


def check_email(email: str) -> bool:
    # checks if the email is valid
    if '@' in email:
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


def personal_page(username: str):
    text = """
1. Read my data
2. Update my data
3. Delete my account
4. Exit
"""
    print(command + text)
    user_input = input(enter + 'Enter your choice: ')
    if user_input == '1':
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
    elif user_input == '4':
        resident_page(username)
    else:
        print(error + 'Invalid input. Try again!')
    personal_page(username)


def request_page(username: str):
    text = """
1. Create a request
2. See all requests
3. Edit a request
4. Delete a request  
5. Exit  
"""
    print(command + text)
    user_input = input(enter + 'Enter your choice: ')
    if user_input == '1':
        subject = input(enter + 'Enter your subject: ')
        request = input(enter + 'Enter your request: ')
        money_needed = int(input(enter + 'Enter money needed: '))
        district_id = ResidentsManager(username).get_district_id()
        owner_id = ResidentsManager(username).get_resident_id()
        RequestsManager().create_request(owner_id, district_id, subject, request, money_needed)
        print(success + 'Successfully created!')
        request_page(username)
    elif user_input == '2':
        RequestsManager().get_all_requests()
        input(enter + "Press enter to continue: ")
        request_page(username)
    elif user_input == '3':
        owner_id = ResidentsManager(username).get_resident_id()
        RequestsManager().get_my_requests(owner_id)
        request_id = input(enter + 'Enter the id of a request you want to delete: ')
        new_subject = input(enter + "Enter your new subject: ")
        new_request = input(enter + "Enter your new request: ")
        new_money_needed = int(input(enter + "Enter money needed: "))
        RequestsManager().edit_requests(new_subject, new_request, new_money_needed, request_id)
        print(success + "Successfully edited!")
        resident_page(username)
    elif user_input == '4':
        owner_id = ResidentsManager(username).get_resident_id()
        RequestsManager().get_my_requests(owner_id)
        request_id = input(enter + 'Enter the id of a request you want to delete: ')
        if RequestsManager().delete_request(request_id):
            print(success + 'Successfully deleted!')
            resident_page(username)
    elif user_input == '5':
        resident_page(username)


def resident_page(username: str):
    text = """
1. Personal Cabinet.
2. Requests page.
3. Logout
    """
    print(command + text)
    user_input = input(enter + "Choose an option: ")
    if user_input == '1':
        personal_page(username)
    elif user_input == '2':
        request_page(username)
    elif user_input == '3':
        auth_menu()


def resident_management():
    text = """
1. See residents by location
2. Edit a resident
3. Delete a resident
4. Exit
"""
    print(command + text)
    user_input = input(enter + "Choose an option: ")
    if user_input == '1':
        RegionsManagers().print_all_regions()
        region_id = input(enter + "Enter region id: ")
        DistrictsManager().get_all_districts(region_id)
        district_id = input(enter + "Enter district id: ")
        ResidentsManager.print_by_district(district_id)
    elif user_input == '2':
        ResidentsManager.see_all_residents()
        resident_id = input(enter + 'Enter the resident id: ')
        username = ResidentsManager.get_resident_username(resident_id)
        new_full_name = input(enter + "Enter your new full name: ")
        new_username = input(enter + "Enter your new username: ")
        new_email = input(enter + "Enter your new email: ")
        if check_email(new_email):
            verification_code = random.randint(10000, 99999)
            verification_code = str(verification_code)
            th1 = threading.Thread(target=verify_password, args=(new_email, verification_code,))
            th1.start()
            if check_code(verification_code):
                if ResidentsManager(username).update_resident(new_full_name, new_username, new_email):
                    print(success + 'Successfully updated!')
    elif user_input == '3':
        ResidentsManager.see_all_residents()
        resident_id = input(enter + 'Enter the resident id: ')
        username = ResidentsManager.get_resident_username(resident_id)
        if ResidentsManager(username).delete_resident():
            print(success + "Successfully deleted!")
    elif user_input == '4':
        admin_page()
    else:
        print(error + 'Invalid input. Try again!')
    resident_management()


def request_management():
    text = """
1. Approve/Deny a request
2. See approved requests
3. See denied requests
4. Exit
"""
    print(command + text)
    user_input = input(enter + "Choose an option: ")
    if user_input == '1':
        RequestsManager().get_null_requests()
        request_id = input(enter + "Enter request ID to manage: ")
        response = input(enter + "Approve or Deny a request? A/D: ")
        if response == 'A':
            if RequestsManager().approve_request(request_id):
                print(success + "Request Approved")
            else:
                print(error + "Error")
                request_management()
        elif response == 'D':
            if RequestsManager().deny_request(request_id):
                print(success + "Request Denied")
            else:
                print(error + "Error")
        else:
            print(error + 'Invalid input. Try again!')
    elif user_input == '2':
        RequestsManager().see_approved_requests()
        input(enter + "Press enter to continue...")
    elif user_input == '3':
        RequestsManager().see_denied_requests()
        input(enter + "Press enter to continue...")
    elif user_input == '4':
        admin_page()
    else:
        print("Invalid input. Try again!")
    request_management()


def location_management():
    text = """
1. See all regions
2. See all districts
3. Add a region
4. Add a district
5. Exit
"""
    print(command + text)
    user_input = input(enter + "Choose an option: ")
    if user_input == '1':
        RegionsManagers().print_all_regions()
        input("Press enter to continue...")
    elif user_input == '2':
        RegionsManagers().print_all_regions()
        region_id = input(enter + "Enter region id: ")
        DistrictsManager().get_all_districts(region_id)
    elif user_input == '3':
        region_name = input(enter + "Enter region name: ")
        if RegionsManagers().add_region(region_name):
            print(success + "Successfully added a region!")
    elif user_input == '4':
        RegionsManagers().print_all_regions()
        region_id = int(input(enter + "Enter region id: "))
        DistrictsManager().get_all_districts(region_id)
        district_name = input(enter + "Enter the district name: ")
        if DistrictsManager().add_district(region_id, district_name):
            print(success + "Successfully added a district!")
    elif user_input == '5':
        admin_page()
    else:
        print("Invalid input. Try again!")
    location_management()


def statistics():
    text = """
1. Total money requested
2. Average money requested per request
3. Requests grouped by district
4. Requests grouped by region
5. Top 5 highest money requests
6. Exit
    """
    print(command + text)
    user_input = input(enter + "Choose an option: ")
    if user_input == '1':
        RequestsManager().get_total_money_requested()
        input("Press enter to continue...")
    elif user_input == '2':
        RequestsManager().get_avg_money_requested()
        input("Press enter to continue...")
    elif user_input == '3':
        RequestsManager().requests_by_district_id()
        input("Press enter to continue...")
    elif user_input == '4':
        RequestsManager().requests_by_region_id()
        input("Press enter to continue...")
    elif user_input == '5':
        RequestsManager().top5_high_money_requests()
        input("Press enter to continue...")
    elif user_input == '6':
        admin_page()
    else:
        print(error + "Invalid input. Try again!")
    statistics()


def admin_page():
    text = """
1. Resident Management
2. Request Management
3. Location Management
4. Statistics
5. Logout
"""
    print(command + text)
    user_input = input(enter + "Choose an option: ")
    if user_input == '1':
        resident_management()
    elif user_input == '2':
        request_management()
    elif user_input == '3':
        location_management()
    elif user_input == '4':
        statistics()
    elif user_input == '5':
        auth_menu()
    else:
        print("Invalid input. Try again!")
    admin_page()


def login_page():
    username = input(enter + 'Enter your username: ')
    password = input(enter + 'Enter your password: ')
    if username == 'admin' and password == 'admin':
        admin_page()
    elif ResidentsManager(username).check_existence_by_username():
        if ResidentsManager(username).check_password(password):
            resident_page(username)
    else:
        print(error + 'Username or password doesn\'t match')
    auth_menu()


def register_page():
    RegionsManagers().print_all_regions()
    region_id = input(enter + "Enter region id: ")
    DistrictsManager().get_all_districts(region_id)
    district_id = input(enter + "Enter district id: ")
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
                if ResidentsManager(username).create_resident(full_name, district_id, email, password):
                    print(success + "Successfully registered!")
                    auth_menu()
        else:
            print('Try again!')
    else:
        print('Invalid email!')


def auth_menu():
    text = """
    1. Login
    2. Register
    3. Exit
    """
    print(command + text)
    user_input = input(enter + "Enter your choice: ")
    if user_input == "1":
        login_page()
    elif user_input == "2":
        register_page()
    elif user_input == "3":
        exit()


if __name__ == "__main__":
    auth_menu()
