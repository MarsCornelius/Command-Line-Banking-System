from clbs_classes.login import Login
from datetime import datetime
from clbs_functions.database_handler import database_add_user_info
import maskpass


def welcome():
    print("Welcome to Mars Student Bank")
    print("Select one of the following to get started: ")
    try:
        option = input("1.Login \n2.Create an Account \n3.Reset Password \n4.Exit \n-->")
        print()
    except ValueError:
        print("Welcome Error: Invalid option")
        return None
    return option


def log_in():
    print("~LOGIN CREDENTIALS~")
    try:
        user = input("Primary Account Number: ")
        Login.username = user

        password = maskpass.askpass(prompt="Password:",mask="*")
        Login.password = password
    except ValueError:
        print("Login Error: Invalid credentials.")
        return None

    return Login.username, Login.password


def create_user_account():
    data = 0
    no_of_fields = 10
    c_info = []
    while data < no_of_fields:
        if data == 0:
            try:
                f_name = input("First Name: ").capitalize()
                if f_name.isalpha():
                    c_info.append(f_name)
                    data += 1
                else:
                    print("Invalid input. Please enter a valid First Name.")
            except ValueError:
                print("Invalid input. Please enter a valid First Name.")
        elif data == 1:
            l_name = input("Last Name: ").capitalize()
            if l_name.isalpha():
                c_info.append(l_name)
                data += 1
            else:
                print("Invalid input. Please enter a valid Last Name.")
        elif data == 2:
            try:
                year, month, day = input("Birth date (YYYY MM DD): ").split()
                if year.isdigit() and month.isdigit() and day.isdigit():
                    if len(year) == 4 and len(month) == 2 and len(day):
                        if int(year) <= (datetime.now().year - 14) and int(month) <= 12 and int(day) <= 31:
                            birth_date = f"{year}-{month}-{day}"
                            c_info.append(birth_date)
                            data += 1
                        else:
                            print("Invalid input. Please enter a valid Birth Date (YYYY MM DD).")
                    else:
                        print("Invalid input. Please enter a valid Birth Date (YYYY MM DD).")
                else:
                    print("Invalid input. Please enter a valid Birth Date (YYYY MM DD).")
            except ValueError:
                print("Invalid input. Please enter a valid Birth Date (YYYY MM DD).")
            except UnboundLocalError:
                print("Invalid input. Please enter a valid Birth Date (YYYY MM DD).")
        elif data == 3:
            try:
                address = input("Address: ").title()
                c_info.append(address)
                data += 1
            except ValueError:
                print("Invalid input. Please enter a valid address.")
        elif data == 4:
            try:
                city = input("City: ").capitalize()
                if city.isalpha():
                    c_info.append(city)
                    data += 1
                else:
                    print("Invalid input. Please enter a valid City.")
            except ValueError:
                print("Invalid input. Please enter a valid City.")
        elif data == 5:
            try:
                postal = input("Postal Code: ").upper()
                if any(char.isalpha() for char in postal) and any(char.isdigit() for char in postal)\
                        and len(postal) == 6:
                    c_info.append(postal)
                    data += 1
                else:
                    print("Invalid input. Please enter a valid postal code.")
            except ValueError:
                print("Invalid input. Please enter a valid postal code.")
        elif data == 6:
            try:
                province = input("Province: ").title()
                if province.isalpha():
                    c_info.append(province)
                    data += 1
                else:
                    print("Invalid input. Please enter a valid Province.")
            except ValueError:
                print("Invalid input. Please enter a valid Province.")
        elif data == 7:
            try:
                country = input("Country: ").title()
                if country.isalpha():
                    c_info.append(country)
                    data += 1
                else:
                    print("Invalid input. Please enter a valid Country.")
            except ValueError:
                print("Invalid input. Please enter a valid Country.")
        elif data == 8:
            try:
                mobile_no = input("Mobile Number: ")
                if mobile_no.isdigit() and len(mobile_no) == 10:
                    c_info.append(mobile_no)
                    data += 1
                else:
                    print("Invalid input. Please enter a valid Mobile Number.")
            except ValueError:
                print("Invalid input. Please enter a valid Mobile Number.")
        elif data == 9:
            try:
                email = input("Email : ")
                start = email.find('@')
                if start > 0:
                    c_info.append(email)
                    data += 1
                else:
                    print("Invalid input. Please enter a valid email address.")
            except ValueError:
                print("Invalid input. Please enter a valid email address.")
    database_add_user_info(c_info)


def reset_password():
    print("~RESET MY PASSWORD~")
    try:
        user_to_reset = input("Enter Username: ")
    except ValueError:
        print("Reset Password Error: Invalid username")
        return None

    return user_to_reset