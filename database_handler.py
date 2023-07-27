import mysql.connector


def connect_to_database(username, password):
    try:
        database = mysql.connector.connect(username=username, password=password, host='localhost', port=3306)
        cursor = database.connect()
        return database, cursor

    except mysql.connector.Error as e:
        print("Error: ", e)

def database_validate_credentials(user_info):
    pass


def database_create_user(customer_info):
    pass


def database_reset_password(username):
    pass

def database_fetch_transaction_history(account_no, acct_type):
    pass

def database_select_transactions(account_no, transaction_id, amount, date):
    pass


def database_export_transactions(account_no):
    pass