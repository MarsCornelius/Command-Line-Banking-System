from navigation import Navigation
from menu import welcome, Log_in, create_user_account, reset_password, make_an_appointment
import time


def main():
    try:
        navigation = Navigation()
        navigation.menu_option = welcome()
        match navigation.menu_option:
            case 1:
                username, password = Log_in()
            case 2:
                create_user_account()
            case 3:
                reset_password()
            case 4:
                navigation.app_option = make_an_appointment()
                match navigation.app_option:
                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
            case 5:
                print("Exiting System...")
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
