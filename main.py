from customer import Customer
from navigation import Navigation
from login import Login
from menu import welcome, Log_in, create_user_account
import time

if __name__ == '__main__':
    try:
        navigation = Navigation()
        navigation.menu_option = welcome()
        match navigation.menu_option:
            case 1:
                username, password = Log_in()
            case 2:
                create_user_account()
            case 3:
                pass
            case 4:
                pass
            case 5:
                print("Exiting System...")
                time.sleep(3)
                print("Good-Bye!")
                exit(0)

    except KeyboardInterrupt:
        print("\nGood bye!\n")

