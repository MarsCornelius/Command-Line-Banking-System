from login import Login
from customer import Customer


def welcome():
    print("Welcome to Mars Student Bank")
    print("Select one of the following to get started: ")
    option = input("1.Login \n2.Create an Account \n3.Reset Password \n4.Exit \n-->")
    print()
    return option


def log_in():
    print("~LOGIN CREDENTIALS~")

    user = input("Primary Account Number: ")
    Login.username = user

    password = input("Password: ")
    Login.password = password

    return Login.username, Login.password


def create_user_account():
    print("~CREATE AN ACCOUNT~")
    customer_info = {}

    Customer.first_name = input("First Name: ").capitalize()
    customer_info["first"] = Customer.first_name

    Customer.last_name = input("Last Name: ").capitalize()
    customer_info["last"] = Customer.last_name

    Customer.birth_date = input("Date of Birth: ")
    customer_info["birth"] = Customer.birth_date

    Customer.address = input("Address: ").title()
    customer_info["address"] = Customer.address

    Customer.city = input("City: ").capitalize()
    customer_info["city"] = Customer.city

    Customer.province = input("Province: ").capitalize()
    customer_info["province"] = Customer.province

    Customer.country = input("Country: ").title()
    customer_info["country"] = Customer.country

    print("\ndata submitted...")

    return customer_info


def reset_password():
    print("~RESET MY PASSWORD~")

    user_to_reset = input("Enter Username: ")

    return user_to_reset
