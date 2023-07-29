from clbs_functions.database_handler import database_validate_credentials, database_reset_password
from clbs_classes.navigation import Navigation
from clbs_functions.menu import welcome, log_in, create_user_account, reset_password
import time


def main():
    try:
        navigation = Navigation()
        navigation.menu_option = welcome()
        match navigation.menu_option:
            case 1:
                login_info = log_in()
                database_validate_credentials(login_info)
            case 2:
                create_user_account()
            case 3:
                reset_password()
            case 4:
                print("\nExiting System...")
                time.sleep(3)
                print("Good-Bye!")
                exit(0)

    except KeyboardInterrupt:
        print("\nExiting System...")
        time.sleep(3)
        print("Good-Bye!")
        exit(0)


if __name__ == '__main__':
   # database_reset_password(" 100024", "KibGoo", "pineapple")
    main()