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
        return db, curr

    except mysql.connector.Error as e:
        print("Error: ", e)


def database_validate_credentials(login_info):
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

    connect_to_database(login_info[0],login_info[1])


def database_add_user_info(customer_info):
    add_user = ("INSERT INTO customer( first_name, last_name, birth_date, address, city, postal_code, "
                "province, country, mobile_no, email) VALUES (%s, %s, %s, %s, %s, %s ,%s, %s, %s, %s);")
    cursor.execute(add_user, (customer_info[0], customer_info[1], customer_info[2], customer_info[3],
                              customer_info[4], customer_info[5], customer_info[6], customer_info[7],
                              customer_info[8], customer_info[9]))
    database.commit()

    send_email(customer_info[0], customer_info[1], customer_info[9])

    cursor.close()
    database.close()


def database_reset_password(username):
    pass


def database_fetch_transaction_history(account_no, acct_type):
    pass


def database_select_transactions(account_no, transaction_id, amount, date):
    pass


def database_export_transactions(account_no):
    pass


def generate_username_and_password():
    pool = string.ascii_letters + string.digits
    password = ''
    for _ in range(12):
        password += random.choice(pool)

    return password


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
        print(e)
    except mysql.connector.errors.DatabaseError as e:
        print(e)


def send_email(first_name, last_name, email):
    username = first_name[0:3] + last_name[0:3]
    password = generate_username_and_password()

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
