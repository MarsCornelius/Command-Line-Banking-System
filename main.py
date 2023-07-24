from navigation import Navigation
from menu import welcome, log_in, create_user_account, reset_password
import time


def main():
    try:
        navigation = Navigation()
        navigation.menu_option = welcome()
        match navigation.menu_option:
            case 1:
                user_info = log_in()
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
    main()
