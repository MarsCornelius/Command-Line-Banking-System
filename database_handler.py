import mysql.connector
import smtplib
import ssl


database = mysql.connector.connect(username="root", password="marscornelius", host='localhost', database="bank")
cursor = database.cursor()


def connect_to_database(username, password):
    try:
        db = mysql.connector.connect(username=username, password=password, host='localhost', database="bank")
        curr = db.cursor()
        return db, curr

    except mysql.connector.Error as e:
        print("Error: ", e)


def database_validate_credentials(user_info):
    pass


def database_create_user(customer_info):
    add_to_user = ("INSERT INTO customer( first_name, last_name, birth_date, address, city, postal_code, "
                   "province, country, mobile_no, email) VALUES (%s, %s, %s, %s, %s, %s ,%s, %s, %s, %s);")
    cursor.execute(add_to_user, (customer_info[0], customer_info[1], customer_info[2], customer_info[3],
                                 customer_info[4], customer_info[5], customer_info[6], customer_info[7],
                                 customer_info[8], customer_info[9]),)
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


def send_email(first_name, last_name, email):
    ca_cert_path = "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/certifi/cacert.pem"
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = ""
    password = ""
    message = f"""\
    Mars Student Bank

    Welcome {first_name} {last_name}.

    Here is your username and password.

    Enjoy!
    """

    context = ssl.create_default_context(cafile=ca_cert_path)
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, email, message)
