user_account = {}

def register():
    print("Welcome to Dice Roll Game")
    print("\n\n----Register a New Account----")
    while True:
        try:
            user_name = input("Enter your name: ")
            if not user_name:
                main()
                if len(password) < 4:
                    print ("Your pin must be 4 characters.")
                    continue
                else:
                    continue
            elif user_name in user_account:
                print ("\nUsername taken. Try Again.")
                continue
            else:
                while True: 
                    try:
                        password = input("\nEnter your 8 digit password: ")
                        if not password:
                            main()
                        if len(password) < 8:
                            print ("Your pin must be 8 characters.")
                            continue
                        elif len(password) >= 8:
                            username = input("\nEnter your Username: ")
                            user_account[user_number]= {"username": username, "password": password}
                            print("\nSigned Up Successfully\n")
                            main()
                        else:
                            print("\nInvalid input. Try Again.")
                            continue
                    except ValueError as e:
                        register()
        except ValueError as e:
            register()

def main():
    print("/nWelcome to Dice Roll Game")
    print("1. Register/n2. Log-in/n3. Exit")
    print("Enter your choice or leave a blank to log in")

    if choice == 1:
        register()
    if choice == 2:
        log_in()
    if choice == 3:
        main()
    else:        
        main()

def log_in():
    login= input("\nEnter your Username: ")
    if 