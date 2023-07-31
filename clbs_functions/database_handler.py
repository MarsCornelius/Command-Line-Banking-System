import bcrypt
import mysql.connector
import smtplib
import random
import string
from email.message import EmailMessage
from email.header import Header
database = mysql.connector.connect(username="root", password="marscornelius", host='localhost', database="bank")
cursor = database.cursor()


def connect_to_database(username, password):
    try:
        db = mysql.connector.connect(username=username, password=password, host='localhost', database="bank")
        curr = db.cursor()

        if db.is_connected():
            print(f"\nGood Day {username}, \nWhat would you like to do today?\n")
            return db, curr
        else:
            print("Server not found.")
    except mysql.connector.Error as e:
        print("Error: ", e)


def database_validate_credentials(login_info):
    try:
        get_username = "SELECT username FROM users where username = %s"
        cursor.execute(get_username, (login_info[0],))
        username = cursor.fetchone()

        if username[0] is not None:
            get_password = "SELECT password FROM users WHERE username = %s"
            cursor.execute(get_password, (login_info[0],))
            stored_password = cursor.fetchone()
            if bcrypt.checkpw(login_info[1].encode('utf-8'), stored_password[0].encode('utf-8')):
                print("\nLogin Successful.")
            else:
                print("Login failed.")

        connect_to_database(login_info[0], login_info[1])
    except mysql.connector.errors.DatabaseError as e:
        print("Validate Credentials: ", e)


def database_add_user_info(customer_info):
    try:
        add_user = ("INSERT INTO customer( first_name, last_name, birth_date, address, city, postal_code, "
                    "province, country, mobile_no, email) VALUES (%s, %s, %s, %s, %s, %s ,%s, %s, %s, %s);")
        cursor.execute(add_user, (customer_info[0], customer_info[1], customer_info[2], customer_info[3],
                                  customer_info[4], customer_info[5], customer_info[6], customer_info[7],
                                  customer_info[8], customer_info[9]))
        database.commit()

        send_email(customer_info[0], customer_info[1], customer_info[9])

        cursor.close()
        database.close()
    except mysql.connector.errors.DatabaseError as e:
        print("Database Add User: ", e)


def database_reset_password(customer_id, username, new_password):
    try:
        update_password = "UPDATE users SET password = %s WHERE customer_id = %s"
        new_encrypted_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())

        cursor.execute(update_password, (new_encrypted_password, customer_id))
        database.commit()

        update_mysql_password = "ALTER user %s@'localhost' IDENTIFIED BY %s"
        cursor.execute(update_mysql_password, (username, new_password))
        database.commit()

        refresh = "FLUSH PRIVILEGES"
        cursor.execute(refresh)
    except mysql.connector.ProgrammingError as e:
        print("Database Reset Password: ", e)
    except mysql.connector.errors.DatabaseError as e:
        print("Database Reset Password: ", e)


def database_fetch_transaction_history(account_no, acct_type):
    pass


def database_process_transactions(outer, inner, acct_no, amt):
    if outer == 1:
        # Deposits
        pass
        if inner == 1:
            print("huzzah")
            pass
        elif inner == 2:
            # make withdrawal
            pass
        elif inner == 3:
            pass
        elif inner == 4:
            pass
        else:
            print("Error processing transactions")
    elif outer == 2:
        # Loans
        pass
        if inner == 1:
            # make payment
            pass
        elif inner == 2:
            # make principal
            pass
        elif inner == 3:
            # make interest payment
            pass
        elif inner == 4:
            # make payoff
            pass
    else:
        print("Error processing transactions")


def database_generate_username_and_password():
    try:
        pool = string.ascii_letters + string.digits
        password = ''
        for _ in range(12):
            password += random.choice(pool)

        return password
    except IndexError as e:
        print("Username and Password Error: ", e)


def database_create_user(username, password):
    try:
        get_customer_id = "SELECT max(customer_id) from customer"
        cursor.execute(get_customer_id)
        customer_id = cursor.fetchone()[0]

        # add user to the users table, to facilitate validation.
        add_to_user = "INSERT INTO users (customer_id, username, password) values (%s, %s,%s)"
        encrypted_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        cursor.execute(add_to_user, (customer_id, username, encrypted_password), )
        database.commit()

        # add user to the mysql.user table to facilitate login.
        add_to_mysql_user = "CREATE USER %s@'localhost' IDENTIFIED BY %s"
        cursor.execute(add_to_mysql_user, (username, password))
        database.commit()

        grant_permission = "GRANT ALL PRIVILEGES ON bank.* TO %s@'localhost'"
        cursor.execute(grant_permission, (username, ))
        database.commit()

        refresh = "FLUSH PRIVILEGES;"
        cursor.execute(refresh)
    except mysql.connector.ProgrammingError as e:
        print("Database Create User: ", e)
    except mysql.connector.errors.DatabaseError as e:
        print("Database Create User: ", e)


def send_email(first_name, last_name, email):
    try:
        username = first_name[0:3] + last_name[0:3]
        password = database_generate_username_and_password()

        database_create_user(username, password)

        msg = EmailMessage()
        msg.set_content(f'Welcome {first_name} {last_name},\n\n'
                        f'Thank you for choosing us!\n\n'
                        f'Here are your credentials:\n\n'
                        f'Username:{username}\n'
                        f'Password:{password}\n')
        msg['Subject'] = 'Sign up'
        msg['From'] = str(Header("Customer Support <kibwemc.dev@gmail.com>"))
        msg['To'] = email

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("kibwemc.dev@gmail.com", "rvveonrniggxvosa")
        server.send_message(msg)
        server.quit()
    except smtplib.SMTPException as e:
        print("Send Email Error: ", e)
    except Exception as e:
        print("Send Email Error: ", e)
