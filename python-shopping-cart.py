try:

    def emirhan():
        while True:
            x = input("Please write \"123\" for confirmation: ")
            if x == "123":
                print('"{}"'.format(x), "Thanks for the correct answer!")

                while True:
                    print("Please enter your complete user data")
                    username = ("Your username: ")  # Emirhan BULUT
                    username1 = (
                            username + input("Are You a Customer?, Then Enter a Username: "))
                    print(username1)
                    usernamesal = input(
                        "Do you approve? \"If you give consent\" Say \"yes\": ")
                    if usernamesal == "yes":
                        print("Thanks! You can continue..")
                        while True:
                            password = ("You have carefully entered your password: ")  # 2003709
                            password1 = (password + input("Enter Your Password Beautifully: "))
                            print(password1)
                            passwordsal = input(
                                "Do you approve? \"If you give consent\" Say \"yes\": ")
                            if passwordsal == "yes":
                                print("Thanks! You can continue..")

                                while True:
                                    print("""*** EMIRHAN AI MARKET ***
                                        For the operation, please express the numbers from the required menu:
                                        1. Shopping List
                                        2. Add Product to Shopping List
                                        3. Delete Product from shopping list
                                        4. Check If The Product Is On The Shopping List
                                        5. Delete Shopping List
                                        6. You can exit
                                        """)

                                    emirhan_ai = input("Please choose...: ")

                                    emirhan_list = [
                                        "1- License Plate Reading AI", "2-Voice to Text AI", "3-Chatbot AI",
                                        "4-Text to Voice AI"]

                                    def emirhan_ai_list():
                                        print()
                                        print("*** Shopping list ***")
                                        for i in emirhan_list:
                                            print("* " + i)

                                    def prduct_add():
                                        emirhan_data_add = input(
                                            "Enter the product you want to add to the shopping list: ")
                                        emirhan_list.append(emirhan_data_add)
                                        print(emirhan_data_add + " added to the shopping list.")

                                    def prduct_clear():
                                        emirhan_data_add = input(
                                            "Enter the product you want to remove from the shopping list: ")
                                        emirhan_list.remove(emirhan_data_add)
                                        print(emirhan_data_add + " removed from the shopping list.")

                                    def emirhan_control():
                                        emirhan_data_add = input(
                                            "Which product would you like to check on the shopping list: ")
                                        if emirhan_data_add in emirhan_list:
                                            print("Evet, " + emirhan_data_add + " on the shopping list.")
                                        else:
                                            print("Hayır, " + emirhan_data_add + " not on the shopping list.")

                                    def urun_listele():
                                        print("These", len(emirhan_list), "products in the shopping list.")

                                    def list_clear():
                                        emirhan_list.clear()
                                        print("The shopping list is now empty.")

                                    if emirhan_ai == "1":
                                        emirhan_ai_list()
                                    elif emirhan_ai == "2":
                                        prduct_add()
                                    elif emirhan_ai == "3":
                                        prduct_clear()
                                    elif emirhan_ai == "4":
                                        emirhan_control()
                                    elif emirhan_ai == "5":
                                        list_clear()
                                    elif emirhan_ai == "6":
                                        sys.exit()
                                    else:
                                        print("Please choose again...: ")

                            elif passwordsal == "no":
                                print("Try agaaaain..")
                    elif usernamesal == "no":
                        break

            else:
                print("Try again!")



    emirhan()

except:
    print("Try again..")
