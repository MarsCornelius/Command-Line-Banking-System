from functions.menu import account_menu, launch
from functions.database_handler import database_process_transactions


if __name__ == '__main__':
    launch()
    outer, inner, acct_no, amt = account_menu()
    database_process_transactions(outer, inner, acct_no, amt)