# # Low Jye Shan
# # TP059522
# # Teo Su Yin
# # TP059523

# # # # Preset Admin Files (In text file for permanent record) # #
# with open("Admin.txt", "w") as admin_file:
#     admin_file.write("Ain001.Ain@0619\nJessica002.Jes_8888\nJunLin003.He180#04\nJudyHua004.J@19900207\nMuthu005.M@1027\n")
# # ----------------------------------------------------------------------------------------------------
# # Preset Food Category Files (In text file) # #
# food_category_file = open("Rice.txt", "w")
# food_category_file.write("White Rice:1.00\n")
# food_category_file = open("Rice.txt", "a")
# food_category_file.write("TeoChew Fried Rice:5.00\n")
# food_category_file.write("Kampung Fried Rice:5.00\n")
# food_category_file.write("HaiNan Chicken Rice:5.50\n")
# food_category_file.write("Thailand Mango Sticky Rice:6.00\n")
# food_category_file.close()
#
# food_category_file = open("Noodle.txt", "w")
# food_category_file.write("Veggie Noodle:4.50\n")
# food_category_file = open("Noodle.txt", "a")
# food_category_file.write("Chicken Noodle Soup:5.50\n")
# food_category_file.write("Xi Dao Fish Ball Noodle Soup:5.50\n")
# food_category_file.write("Laksa:5.50\n")
# food_category_file.write("Fried Noodle:4.00\n")
# food_category_file.close()
#
# food_category_file = open("Western.txt", "w")
# food_category_file.write("Chicken Chop (Mushroom):10.00\n")
# food_category_file = open("Western.txt", "a")
# food_category_file.write("Chicken Chop (Black Pepper):10.00\n")
# food_category_file.write("Grilled Salmon:12.00\n")
# food_category_file.write("Fish and Chip:8.00\n")
# food_category_file.write("Chicken Burger:8.00\n")
# food_category_file.write("Fish Burger:8.00\n")
# food_category_file.close()
#
# food_category_file = open("Dessert.txt", "w")
# food_category_file.write("Strawberry Cake (slice):8.00\n")
# food_category_file = open("Dessert.txt", "a")
# food_category_file.write("Chocolate Cake (Slice):8.00\n")
# food_category_file.write("Oreo Cheese Cake (Slice):8.00\n")
# food_category_file.write("Strawberry Waffle:8.00\n")
# food_category_file.write("Chocolate Waffle:8.00\n")
# food_category_file.close()
#
# food_category_file = open("Beverage.txt", "w")
# food_category_file.write("Latte:4.00\n")
# food_category_file = open("Beverage.txt", "a")
# food_category_file.write("Cappuccino:4.00\n")
# food_category_file.write("Milo:3.00\n")
# food_category_file.write("Milo Dinosaur:5.00\n")
# food_category_file.close()
# # -----------------------------------------------------------------------------------------------------
# # # All Category File # #
# all_category = open("Category.txt", "w")
# all_category.write("Rice\nNoodle\nWestern\nDessert\nBeverage\n")
# all_category.close()
# # # ------------------------------------------------------------------------------------------------------
# # # # preset order record # #
# with open("order.txt", "w") as new_order_file:
#     new_order_file.write("Order ID: 001#Username: yaxuann_04#Name: Song Ya Xuan#Contact Number: 01767573702#")
# with open("order.txt", "a") as new_order_file:
#     new_order_file.write("Email: yxuan04@gmail.com#Address: No 3 Jalan Budaya Jaya 10 Taman Budaya Jaya 83000 Batu Pahat#")
#     new_order_file.write("1:Laksa:5.50#2:Latte:4.00#Receipt ID: PY001#Date: 31/07/2021#Time: 12:21:53#Payment Method: iPay88\n")
#
# with open("order.txt", "a") as new_order_file:
#     new_order_file.write("Order ID: 002#Username: jiaqi_1112#Name: Ma Jia Qi#Contact Number: 01118793786#")
#     new_order_file.write("Email: jiaqi2002@gmail.com#Address: No 22 Jalan Tasek Y, Taman Soga 83000 Batu Pahat Johor#")
#     new_order_file.write("2:Laksa:5.50#2:Cappuccino:4.00#Receipt ID: PY002#Date: 01/08/2021#Time: 10:27:42#Payment Method: iPay88\n")
#
# with open("order.txt", "a") as new_order_file:
#     new_order_file.write("Order ID: 003#Username: jiaqi_1112#Name: Ma Jia Qi#Contact Number: 01118793786#")
#     new_order_file.write("Email: jiaqi2002@gmail.com#Address: No 22 Jalan Tasek Y, Taman Soga 83000 Batu Pahat Johor#")
#     new_order_file.write("1:Oreo Cheese Cake (Slice):8.00#Receipt ID: PY003#Date: 01/08/2021#Time: 17:51:27#Payment Method: iPay88\n")
# # # ------------------------------------------------------------------------------------------------------
# # # current customers' data #
# with open("customers.txt", "w") as customers_file:
#     customers_file.write("yaxuann_04:song0324:Song Ya Xuan:+601767573702:yxuan04@gmail.com:No 3 Jalan Budaya Jaya 10 Taman Budaya Jaya 83000 Batu Pahat:\n")
# with open("customers.txt", "a") as customers_file:
#     customers_file.write("Hjhhanim68@:hnm9898#:Hajah Hanim bt Sulaiman:+601897026202:hanim98@gmail.com:No 6 Jalan Megah 7 Taman Megah 83000 Batu Pahat:\n")
#     customers_file.write("alinatzy2010:abcd1234!:Alina Tan:+60127652890:alina02@yahoo.com:No 52 Jalan Puteri Indah 6 Taman Puteri Indah 83000 Batu Pahat:\n")
#     customers_file.write("jiaqi_1112:ma0211#:Ma Jia Qi:+601118793786:jiaqi2002@gmail.com:No 22 Jalan Tasek Y, Taman Soga 83000 Batu Pahat:\n")


# # defining function needed # #
def start_menu():
    while True:
        try:
            # Choose type of login (Admin, Registered client or Guest)
            print("\nStart Menu")
            print("----------")
            print("(1) Admin Login\n(2) Customer Login\n(3) Visit as Guest\n(4) Exit")
            option = int(input("Please enter your choice: "))
            if option in range(1, 5):
                break
            else:
                print("Option does not exist!\n")
        except ValueError:
            print("Only integer is allowed!\n")

    if option == 1:
        admin_login()

    elif option == 2:
        customer_login()
        view_category()

    elif option == 3:
        guest_menu()

    else:
        print("Exiting...")
        exit()
# # -----------------------------------------------------------------------------------------------------


def admin_login():
    login_status = False  # default login_status as unsuccessful
    # max login times = 3, wrong more than 3 times will back to the start menu
    for i in range(2, -1, -1):
        admin_exist = []  # get the current exist admin username
        password_exist = []  # get current exist password
        print("\nAdmin Login\n-----------")
        with open("Admin.txt", "r") as open_admin_file:
            check_admin = open_admin_file.readlines()
            for admin in check_admin:
                strip_admin = admin.strip()
                split_admin = strip_admin.split(".")
                username = split_admin[0]
                password = split_admin[1]
                admin_exist.append(username)  # put every username into the list
                password_exist.append(password)  # put every password into a list
        admin_username = input("Enter your username: ")
        if admin_username in admin_exist:  # if the input username exist, get the password
            line_num = admin_exist.index(admin_username)  # get the index of username found in list
            admin_password = input("Enter your password: ")
            if password_exist[line_num] == admin_password:  # get the password with same index as the username
                print("Login Successful!")  # compare the password with user input password
                login_status = True  # when both username and password match, change status to success
                break  # if get the correct username and password, break the for loop
            else:  # if password wrong, won't change the login status, run for loop again
                print(f"Wrong password insert! You still have {i} chance. Please try again!")
        else:  # if username not exist in the list, won't change login status and will run the loop
            print(f"Username not found! You still have {i} chance.")

    if login_status:
        admin_menu()        # call admin menu when login status is success.
    else:
        print("3 Chances finished, automatically return to Start Menu.")
        start_menu()            # if after 3 times still not success, return to start menu
# # -----------------------------------------------------------------------------------------------------


def admin_menu():
    while True:
        try:
            print("\nAdmin Menu")       # Show what can an admin do
            print("----------")
            print("1. Add Food Item Category-wise\n2. Modify Food Item Details")
            print("3. Display All Food Category\n4. Display All Food Item Category-wise")
            print("5. Display All Customer Orders\n6. Display All Customer Payment")
            print("7. Search Specific Customer Order\n8. Search Specific Customer Payment\n9. Log Out")
            option1 = int(input("Enter your choice: "))
            if option1 in range(1, 10):
                break
            else:
                print("Invalid option! Please choose from 1 to 9.")
        except ValueError:
            print("Only integer is allowed!")

    if option1 == 1:
        add_food()
    elif option1 == 2:
        modify_food()
    elif option1 == 3:
        all_category()
    elif option1 == 4:
        all_food()
    elif option1 == 5:
        all_orders()
    elif option1 == 6:
        all_payments()
    elif option1 == 7:
        search_order()
    elif option1 == 8:
        search_payment()
    else:
        print("Logging Out...")
        start_menu()
# # -----------------------------------------------------------------------------------------------------


def admin_confirmation():
    while True:
        try:
            print("\nDo you want to log out?")          # After a process, ask admin whether to log out or not
            admin_choice = int(input("(0) Log Out\n(1) Admin Menu\nEnter your choice: "))
            if admin_choice in range(0, 2):
                break
            else:
                print("Invalid option! Please enter 0 or 1.")
        except ValueError:
            print("Only integer 0 or 1 is allowed.")

    if admin_choice == 0:
        print("Logging out...")
        start_menu()        # Log out admin system will back to start menu
    else:
        admin_menu()        # Continue to display admin menu
# # -----------------------------------------------------------------------------------------------------


def add_food():         # ii. Add food item category-wise
    while True:
        try:
            print("\nAdd Food Item")
            print("-------------")
            open_category_file = open("Category.txt", "r")
            count = 1
            for line in open_category_file.readlines():
                category = line.strip()
                print(f"{count}. {category}")
                count += 1                      # Show all category
            open_category_file.close()

            select_category = int(input("Enter the category you wish to add item: "))     # Choose which to add
            if select_category in range(1, 6):
                food_name = input("Enter the food name: ")        # Enter new food's name
                food_price = float(input(f"Enter {food_name}'s price: RM"))      # Enter it's price
                break
            else:
                print("Invalid option! Only 1 to 5 is available.")
        except ValueError:
             print("Only integer or float is allowed.")

    open_category_file = open("Category.txt", "r")
    lines = open_category_file.readlines()
    file = lines[select_category-1]
    stripped_file = file.strip()            # strip to delete \n
    add_into = open(f"{stripped_file}.txt", "a")
    add_into.write(f"{food_name}:{food_price}\n")       # Append new food into text file
    add_into.close()

    print("Food added!")
    print("=============================================================================================")

    while True:
        try:                            # Check whether admin wants to continue this function or not
            cont_statement = int(input("\n(1) Add other item\n(2) Exit this session\nYour option: "))
            if cont_statement in range(1, 3):
                break
            else:
                print("Option does not exist.")
        except ValueError:
            print("Only integer 1 and 2 are allowed.")

    if cont_statement == 1:
        add_food()
    else:
        admin_confirmation()            # check whether admin want to log out or not
# # ------------------------------------------------------------------------------------------------------


def modify_food():
    while True:
        try:
            print("\nModify Food Item")
            print("-------------")
            modify_option = int(input("(1) Edit current food item.\n"  # choose edit food details
                                      "(2) Delete current food item.\n"  # or delete the food
                                      "Enter you option: "))
            if modify_option in range(1, 3):
                break
            else:
                print("Invalid option! Enter 1 or 2 only.")
        except ValueError:
            print("Enter integer 1 or 2.")

    if modify_option == 1:
        edit_food()
    else:
        delete_food()
# # -----------------------------------------------------------------------------------------------------


def edit_food():
    while True:
        try:
            print("\nModify Food Price")
            print("-----------------")
            open_category_file = open("Category.txt", "r")
            count = 1
            for line in open_category_file.readlines():
                category = line.strip()
                print(f"{count}. {category}")
                count += 1                      # Show all category
            open_category_file.close()

            edit_category = int(input("Enter the food category: "))
            if edit_category in range(1, 6):
                break
            else:
                print("Invalid option! Only 1 to 5 is accepted.")
        except ValueError:
            print("Enter integer 1 to 5!")

    open_category_file = open("Category.txt", "r")
    lines = open_category_file.readlines()
    file = lines[edit_category - 1]
    stripped_file = file.strip()
    print(f"\n{stripped_file}")
    print("-" * 8)
    edit_food_file = open(f"{stripped_file}.txt", "r")
    count = 1
    for lines in edit_food_file.readlines():
        line = lines.strip()
        item = line.split(":")          # delete :
        food_name = item[0]             # after split will become a list
        food_price = item[1]
        print(f"{count}. {food_name} --> RM{float(food_price):.2f}")
        count += 1
    open_category_file.close()
    edit_food_file.close()

    while True:
        try:
            edit_food_file = open(f"{stripped_file}.txt", "r")
            current_data = edit_food_file.read()
            temp_list = current_data.splitlines()
            item_num = int(input("---------------------------------------------------------------\n"
                                 "Choose which food you want to modify the price: "))
            if item_num in range(1, count):  # make sure the food choose presents
                break
            else:
                print("Selected food not exist.")
        except ValueError:
            print("Enter the number of the food.")

    while True:
        try:
            edit_food_file = open(f"{stripped_file}.txt", "r")
            item_line = edit_food_file.readlines()
            item = item_line[item_num - 1]
            split_item = item.split(":")
            name = split_item[0]
            price = split_item[1]
            print(f"Modifying: {name} --> RM{float(price):.2f}")
            change = float(input("Enter a new price: RM"))
            edit_food_file.close()
            break
        except ValueError:
            print("Only integer or float is allowed.")

    temp_list[item_num-1] = f"{name}:{change}"          # write down new price
    open_category_file = open("Category.txt", "r")
    lines = open_category_file.readlines()
    file = lines[edit_category - 1]
    stripped_file = file.strip()
    edit_food_file = open(f"{stripped_file}.txt", "w")
    for data in temp_list:
        edit_food_file.writelines(data + "\n")
    open_category_file.close()
    edit_food_file.close()

    print(f"Food item modified successfully!")
    print("=============================================================================================")

    while True:
        try:
            cont_statement = int(input("\n(1) Modify other item\n(2) Exit this session\nYour option: "))
            if cont_statement in range(1, 3):
                break
            else:
                print("Option does not exist.")
        except ValueError:
            print("Only integer 1 and 2 are allowed.")

    if cont_statement == 1:
        edit_food()
    else:
        admin_confirmation()
# # -----------------------------------------------------------------------------------------------------


def delete_food():
    while True:
        try:
            print("\nDelete Food")
            print("-----------")
            open_category_file = open("Category.txt", "r")
            count = 1
            for line in open_category_file.readlines():
                category = line.strip()
                print(f"{count}. {category}")
                count += 1
            open_category_file.close()

            delete_category = int(input("Enter the food category: "))
            if delete_category in range(1, 6):
                break
            else:
                print("Invalid option! Only 1 to 5 is accepted.")
        except ValueError:
            print("Enter integer 1 to 5!")

    open_category_file = open("Category.txt", "r")
    lines = open_category_file.readlines()
    file = lines[delete_category - 1]
    stripped_file = file.strip()
    print(f"\n{stripped_file}")
    print("-" * 8)
    delete_food_file = open(f"{stripped_file}.txt", "r")
    count = 1
    for lines in delete_food_file.readlines():          # let admin see current menu
        line = lines.strip()
        item = line.split(":")
        food_name = item[0]
        food_price = item[1]
        print(f"{count}. {food_name} --> RM{float(food_price):.2f}")
        count += 1
    open_category_file.close()
    delete_food_file.close()

    while True:
        try:
            # choose which to delete
            delete_num = int(input("---------------------------------------------------------------\n"
                                   "Choose which food you want to delete: "))
            if delete_num in range(1, count):
                break
            else:
                print("Selected food not exist.")
        except ValueError:
            print("Enter the number of the food.")

    delete_food_file = open(f"{stripped_file}.txt", "r")
    read_line = delete_food_file.readlines()
    del read_line[delete_num-1]                 # delete the line selected
    delete_food_file = open(f"{stripped_file}.txt", "w")
    for current_line in read_line:
        delete_food_file.write(f"{current_line}")       # write again the remaining lines
    delete_food_file.close()

    print("Food item deleted!")
    print("=============================================================================================")

    while True:
        try:
            cont_statement = int(input("\n(1) Delete other item\n(2) Exit this session\nYour option: "))
            if cont_statement in range(1, 3):
                break
            else:
                print("Option does not exist.")
        except ValueError:
            print("Only integer 1 and 2 are allowed.")

    if cont_statement == 1:
        delete_food()
    else:
        admin_confirmation()
# # -----------------------------------------------------------------------------------------------------


def all_category():
    print("\nFood Category")
    print("-------------")
    open_category_file = open("Category.txt", "r")
    count = 1
    for line in open_category_file.readlines():
        category = line.strip()
        print(f"{count}. {category}")           # show all food category
        count += 1
    open_category_file.close()

    print("=============================================================================================")
    admin_confirmation()
# # -----------------------------------------------------------------------------------------------------


def all_food():
    print("\nDisplay All Food Item Category-wise")
    print("-----------------------------------")
    open_category_file = open("Category.txt", "r")
    count = 1
    for line in open_category_file.readlines():             # show category name
        category = line.strip()
        print(f"========================================\n"
              f"              {category}                \n"
              f"========================================")
        display_all_file = open(f"{category}.txt", "r")         # open and read the corresponding file
        for lines in display_all_file.readlines():
            line = lines.strip()
            item = line.split(":")
            food_name = item[0]
            food_price = item[1]
            print(f"{count}. {food_name} --> RM{float(food_price):.2f}")     # display the items inside
            count += 1
        display_all_file.close()
    open_category_file.close()

    print("=============================================================================================")
    admin_confirmation()
# # -----------------------------------------------------------------------------------------------------


def all_orders():
    open_order = open("order.txt", "r")     # open order record and print out them
    read_record = open_order.readlines()
    for record in read_record:              # print out each line as a record
        strip_record = record.strip()
        split_record = strip_record.split("#")
        order_id = split_record[0]
        username = split_record[1]
        name = split_record[2]
        tel = split_record[3]
        email = split_record[4]
        address = split_record[5]
        print("\n")
        print("=" * 100)
        print(f"{order_id}")
        print("-" * 100)
        print(f"{username}\n{name}\n{tel}\n{email}\n{address}")
        print("-" * 100)

        total = 0
        for item in split_record[6:-4]:
            split_item = item.split(":")
            quantity = split_item[0]
            food_name = split_item[1]
            food_price = split_item[2]
            print(f"{quantity}x\t{food_name} --> RM{float(food_price):.2f}")
            total += float(food_price) * float(quantity)
        print("-" * 100)
        print(f"Total: RM{total:.2f}")
        print("=" * 100)
    open_order.close()

    admin_confirmation()
# # -----------------------------------------------------------------------------------------------------


def all_payments():
    open_payment = open("order.txt", "r")
    read_record = open_payment.readlines()
    for record in read_record:
        strip_record = record.strip()
        split_record = strip_record.split("#")
        receipt_id = split_record[-4]
        order_id = split_record[0]
        username = split_record[1]
        email = split_record[4]
        payment_method = split_record[-1]
        date = split_record[-3]
        time = split_record[-2]
        print("\n")
        print("=" * 100)
        print("Receipt\n---------")
        print(f"{receipt_id}\n{order_id}\n{date}\n{time}\n{username}\n{email}")
        print("-" * 100)

        subtotal = 0
        for item in split_record[6:-4]:
            split_item = item.split(":")
            quantity = split_item[0]
            food_name = split_item[1]
            food_price = split_item[2]
            print(f"{quantity}x\t{food_name} --> RM{float(food_price):.2f}")
            subtotal += float(food_price) * float(quantity)
        print("-" * 100)
        print(f"Subtotal: RM{subtotal:.2f}")
        tax = subtotal * 6 / 100
        total = subtotal + tax
        print(f"Tax: RM{tax:.2f}")
        print(f"Total: RM{total:.2f}")
        print("-" * 100)
        print(payment_method)
        print("=" * 100)
    open_payment.close()

    admin_confirmation()
# # -----------------------------------------------------------------------------------------------------


def search_order():
    while True:
        try:
            print("\nSearch Customer's Order")
            print("------------------------")       # select search by which method
            select_by = int(input("(1) Order ID\n(2) Customer's Username\nSelect By: "))
            if select_by in range(1, 3):
                break
            else:
                print("Option does not exist!")
        except ValueError:
            print("Please enter integer 1 or 2.")

    if select_by == 1:
        while True:
            try:
                search_order_id = int(input("Enter Order ID (eg. 001): "))
                with open("order.txt", "r") as id_method:
                    id_line = id_method.readlines()
                    if search_order_id in range(1, len(id_line)+1):
                        record_needed = id_line[search_order_id-1]
                        break
                    else:
                        print("Order ID Not Found.\n")
            except ValueError:
                print("Only integer is allowed.\n")

        split_record = record_needed.split("#")
        order_id = split_record[0]
        username = split_record[1]
        name = split_record[2]
        tel = split_record[3]
        email = split_record[4]
        address = split_record[5]
        print("\n")
        print("=" * 100)
        print(f"{order_id}")
        print("-" * 100)
        print(f"{username}\n{name}\n{tel}\n{email}\n{address}")
        print("-" * 100)

        total = 0
        for item in split_record[6:-4]:
            split_item = item.split(":")
            quantity = split_item[0]
            food_name = split_item[1]
            food_price = split_item[2]
            print(f"{quantity}x\t{food_name} --> RM{float(food_price):.2f}")
            total += float(food_price) * float(quantity)
        print("-" * 100)
        print(f"Total: RM{total:.2f}")
        print("=" * 100)

    else:
        search_order_username = input("Enter username: ")
        with open("order.txt", "r") as username_method:
            counter_list = []
            counter = 0         # equals to line index
            username_lines = username_method.readlines()
            for lines in username_lines:
                split_lines = lines.split("#")
                title_username = split_lines[1]
                split_username = title_username.split(": ")
                username = split_username[1]
                if search_order_username == username:
                    counter_list.append(counter)            # if meet the condition then record down that line index
                counter += 1            # read one line by one line
            if len(counter_list) == 0:
                print("Record Not Found")

        for num in counter_list:            # for each number of index in counter list
            record_needed = username_lines[num]         # get the line with that index
            split_record = record_needed.split("#")
            order_id = split_record[0]
            username = split_record[1]
            name = split_record[2]
            tel = split_record[3]
            email = split_record[4]
            address = split_record[5]
            print("\n")
            print("=" * 100)
            print(f"{order_id}")
            print("-" * 100)
            print(f"{username}\n{name}\n{tel}\n{email}\n{address}")
            print("-" * 100)

            total = 0
            for item in split_record[6:-4]:
                split_item = item.split(":")
                quantity = split_item[0]
                food_name = split_item[1]
                food_price = split_item[2]
                print(f"{quantity}x\t{food_name} --> RM{float(food_price):.2f}")
                total += float(food_price) * float(quantity)
            print("-" * 100)
            print(f"Total: RM{total:.2f}")
            print("=" * 100)

    while True:
        try:
            cont_statement = int(input("\n(1) Search other records\n(2) Exit this session\nYour option: "))
            if cont_statement in range(1, 3):
                break
            else:
                print("Option does not exist.")
        except ValueError:
            print("Only integer 1 and 2 are allowed.")

    if cont_statement == 1:
        search_order()
    else:
        admin_confirmation()
# # -----------------------------------------------------------------------------------------------------


def search_payment():
    while True:
        try:
            print("\nSearch Customer's Payment")
            print("------------------------")
            search_method = int(input("(1) Receipt ID\n(2) Customer's Username\n(3) Customer's Email\n"
                                      "(4) Date\nSelect By: "))
            if search_method in range(1, 5):
                break
            else:
                print("Option does not exist!")
        except ValueError:
            print("Please enter integer 1, 2, 3 or 4.")

    if search_method == 1:
        while True:
            try:
                search_receipt_id = int(input("Enter Receipt ID (eg. 001): PY"))
                with open("order.txt", "r") as r_id_method:
                    r_id_line = r_id_method.readlines()
                    if search_receipt_id in range(1, len(r_id_line) + 1):
                        record_needed = r_id_line[search_receipt_id - 1]
                        break
                    else:
                        print("Receipt ID Not Found.\n")
            except ValueError:
                print("Only integer is allowed.\n")

        strip_record = record_needed.strip()
        split_record = strip_record.split("#")
        receipt_id = split_record[-4]
        order_id = split_record[0]
        date = split_record[-3]
        time = split_record[-2]
        username = split_record[1]
        email = split_record[4]
        payment_method = split_record[-1]
        print("\n")
        print("=" * 100)
        print("Receipt\n---------")
        print(f"{receipt_id}\n{order_id}\n{date}\n{time}\n{username}\n{email}")
        print("-" * 100)

        subtotal = 0
        for item in split_record[6:-4]:
            split_item = item.split(":")
            quantity = split_item[0]
            food_name = split_item[1]
            food_price = split_item[2]
            print(f"{quantity}x\t{food_name} --> RM{float(food_price):.2f}")
            subtotal += float(food_price) * float(quantity)
        print("-" * 100)
        print(f"Subtotal: RM{subtotal:.2f}")
        tax = subtotal * 6 / 100
        total = subtotal + tax
        print(f"Tax: RM{tax:.2f}")
        print(f"Total: RM{total:.2f}")
        print("-" * 100)
        print(payment_method)
        print("=" * 100)

    else:
        while True:
            if search_method == 2:
                search_payment_username = input("Enter username: ")
                with open("order.txt", "r") as r_username_method:
                    counter_list = []
                    counter = 0
                    target_line = r_username_method.readlines()
                    for lines in target_line:
                        split_lines = lines.split("#")
                        title_username = split_lines[1]
                        split_username = title_username.split(": ")
                        username = split_username[1]
                        if search_payment_username == username:
                            counter_list.append(counter)
                        counter += 1
                    if len(counter_list) == 0:
                        print("Record Not Found\n")
                    else:
                        break

            elif search_method == 3:
                search_payment_email = input("Enter customer's email: ")
                with open("order.txt", "r") as r_email_method:
                    counter_list = []
                    counter = 0
                    target_line = r_email_method.readlines()
                    for lines in target_line:
                        split_lines = lines.split("#")
                        title_email = split_lines[4]
                        split_email = title_email.split(": ")
                        email = split_email[1]
                        if search_payment_email == email:
                            counter_list.append(counter)
                        counter += 1
                    if len(counter_list) == 0:
                        print("Record Not Found.\n")
                    else:
                        break

            else:
                search_date = input("Enter payment date (dd/mm/yyyy): ")
                with open("order.txt", "r") as r_date_method:
                    counter_list = []
                    counter = 0
                    target_line = r_date_method.readlines()
                    for lines in target_line:
                        strip_lines = lines.strip()
                        split_lines = strip_lines.split("#")
                        title_date = split_lines[-3]
                        split_date = title_date.split(": ")
                        date = split_date[1]
                        if search_date == date:
                            counter_list.append(counter)
                        counter += 1
                    if len(counter_list) == 0:
                        print("Record Not Found.\n")
                    else:
                        break

        for num in counter_list:        # for each line index in the counter_list
            record_needed = target_line[num]        # get the line with that index
            strip_record = record_needed.strip()
            split_record = strip_record.split("#")
            receipt_id = split_record[-4]
            order_id = split_record[0]
            date = split_record[-3]
            time = split_record[-2]
            username = split_record[1]
            email = split_record[4]
            payment_method = split_record[-1]
            print("\n")
            print("=" * 100)
            print("Receipt\n---------")
            print(f"{receipt_id}\n{order_id}\n{date}\n{time}\n{username}\n{email}")
            print("-" * 100)

            subtotal = 0
            for item in split_record[6:-4]:
                split_item = item.split(":")
                quantity = split_item[0]
                food_name = split_item[1]
                food_price = split_item[2]
                print(f"{quantity}x\t{food_name} --> RM{float(food_price):.2f}")
                subtotal += float(food_price) * float(quantity)
            print("-" * 100)
            print(f"Subtotal: RM{subtotal:.2f}")
            tax = subtotal * 6 / 100
            total = subtotal + tax
            print(f"Tax: RM{tax:.2f}")
            print(f"Total: RM{total:.2f}")
            print("-" * 100)
            print(payment_method)
            print("=" * 100)

    while True:
        try:
            cont_statement = int(input("\n(1) Search other records\n(2) Exit this session\nYour option: "))
            if cont_statement in range(1, 3):
                break
            else:
                print("Option does not exist.")
        except ValueError:
            print("Only integer 1 and 2 are allowed.")

    if cont_statement == 1:
        search_payment()
    else:
        admin_confirmation()
# # -----------------------------------------------------------------------------------------------------


# menu for guest #
def guest_menu():
    print("\nSpiderman Food Menu")
    print("-"*35)
    with open("Category.txt", "r") as category_file:
        rice_item()        # print rice menu
        print("\n")
        noodle_item()      # print noodle menu
        print("\n")
        western_item()     # print western menu
        print("\n")
        dessert_item()     # print dessert menu
        print("\n")
        beverage_item()    # print beverage menu

    while True:
        try:
            print("\nDo you want to order? Come to register as Spiderman's customer now!")
            print("1. Register as a customer\n2. Exit")
            option = int(input("Please select a option:"))

            if option in range(1, 3):
                break
            else:
                print("Invalid option. Please choose from option 1 to 2.")
        except ValueError:
            print("Error! Please enter an appropriate option.")

    if option == 1:
        customer_register()  # load to customer register page
    else:
        print("Exit Successfully.\nThank you and have a nice day.")
        start_menu()    # back to start menu
# # -----------------------------------------------------------------------------------------------------


# New customer registration #
def customer_register():
    print("\n===============================")
    print("New Customer Registration Page")
    print("===============================")
    print("Please fill in the following information.")
    while True:
        try:
            customer_username = input("Username:")
            if customer_username != "":
                break

            else:
                print("\nPlease fill in your user name to proceed further.")

        except ValueError:
            print("\nPlease fill in your user name to proceed further.")

    while True:
        try:
            customer_name = input("Name:")
            if customer_name != "":
                break

            else:
                print("Please fill in your name to continue registration.")

        except ValueError:
            print("\nPlease fill in your name to continue registration.")

    while True:
        try:
            tel = int(input("Phone Number: +60"))
            if len(str(tel)) == 9 or len(str(tel)) == 10:
                break

            else:
                print("\nPlease fill in your phone number correctly to continue registration.")

        except ValueError:
            print("\nPlease fill in your phone number correctly to continue registration.")

    while True:
        try:
            email = input("Email:")
            if email != "":
                break

            else:
                print("\nPlease fill up your email to continue registration.")

        except ValueError:
            print("\nPlease fill up your email to continue registration.")

    while True:
        try:
            address = input("Delivery Address(No,Street,Region,Postcode,Town):")
            if address != "":
                break

            else:
                print("\nPlease fill in your address to continue registration.")

        except ValueError:
            print("\nPlease fill in your address to continue registration.")

    while True:
        try:
            customer_password = input("Please set a password(At least 7 characters):")
            if len(customer_password) >= 7:
                break

            else:
                print("\nPlease set your password correctly to continue registration.")

        except ValueError:
            print("\nPlease set your password correctly to continue registration.")

    password_confirm = input("Please confirm your password:")
    if password_confirm == customer_password:               # to confirm again the password that user set
        print("\nSuccessfully registered.\nYou can go to log in with your customer account to order food now!")
        customer_file = open("customers.txt", "a")
        customer_file.write(f"{customer_username}:{customer_password}:{customer_name}:+60{tel}:{email}:{address}:\n")
        customer_file.close()
        start_menu()        # load to start menu for the user to log in

    else:
        print("\nError! The password is different from the one entered before.\nPlease register again.")
        return customer_register()  # the second input of password not same as the first input so the user need to register again
# # -----------------------------------------------------------------------------------------------------


# for customer to log in with his/her account
def customer_login():
    # max login times = 3, wrong more than 3 times will back to the start menu
    for i in range(2, -1, -1):
        print("-" * 50)
        print("Customer Login Page")
        print("-"*50)
        customer_username = input("Please enter your username: ")
        customer_password = input("Please enter your password: ")
        with open("customers.txt", "r") as customer_file:
            lines = customer_file.readlines()
            # append customers in customers.txt into an empty list
            customer_list = []
            for customer in lines:
                customer_list.append(customer.strip().split(":"))
            row = 0
            idx = -1
            # loop through the customer_list to find the correct customer's account
            while row < len(customer_list):
                if (customer_username == customer_list[row][0]) and (customer_password == customer_list[row][1]):
                    # if the customer's username found, and the password is correct, set idx equal to the row
                    idx = row
                    break
                else:
                    row += 1

            if idx >= 0:
                print("Login successful!")
                with open("customers.txt", "r") as open_file:
                    for line in open_file:
                        line = line.strip()
                        if line.startswith(customer_username):
                            with open("temporary.txt", "w") as temporary_file:
                                temporary_file.write(f"{line}\n")
                break
            # the idx remain as -1 because the username and the password do not match the record in the list
            elif idx < 0:
                print(f"Wrong username or password! Please try again.\n{i} chance left.")
                print("-"*50)

        if i == 0:
            print("Back to Start Menu.")
            start_menu()     # 3 chances finish and return to start menu
# # -----------------------------------------------------------------------------------------------------


# display all the name of food category
def view_category():
    print("\nFood Category")
    print("-------------")
    open_category_file = open("Category.txt", "r")
    count = 1
    for line in open_category_file.readlines():
        category = line.strip()
        print(f"{count}. {category}")          # show all food category and count the food category
        count += 1
    open_category_file.close()
    print("6. Exit")
    print("="*41)
    view_food_item()       # call function to see the food item inside each category
# # -----------------------------------------------------------------------------------------------------


# Ask users what category of food items they want to see
def view_food_item():
    while True:
        try:
            option = int(input("Please select a food category:"))
            if option in range(1, 7):
                break

            else:
                print("Invalid option.Please choose from 1 to 6.")

        except ValueError:
            print("Invalid option. Please try again.")

    # show all the food item inside each category and ask user if they want to order
    if option == 1:
        rice_item()
        rice_order()

    elif option == 2:
        noodle_item()
        noodle_order()

    elif option == 3:
        western_item()
        western_order()

    elif option == 4:
        dessert_item()
        dessert_order()

    elif option == 5:
        beverage_item()
        beverage_order()

    else:
        print("Exit Successfully.\nThank you and have a nice day.\n")
        start_menu()
# # -----------------------------------------------------------------------------------------------------


# show all food item in rice file
def rice_item():
    print("="*41, "\n"
          "                Rice                  ",)
    print("="*41)
    with open("Rice.txt", "r") as rice_file:
        count = 1
        rice = rice_file.readlines()
        for line in rice:
            food = line.strip()
            item = food.split(":")
            name = item[0]
            price = item[1]
            print(count, name, "--> RM", price)
            count += 1
# # -----------------------------------------------------------------------------------------------------


# show all food item in noodle file
def noodle_item():
    print("="*41, "\n"
          "                Noodle                  ",)
    print("="*41)
    with open("Noodle.txt", "r") as noodle_file:
        count = 1
        noodle = noodle_file.readlines()
        for line in noodle:
            food = line.strip()
            item = food.split(":")
            name = item[0]
            price = item[1]
            print(count, name, "--> RM", price)
            count += 1
# # -----------------------------------------------------------------------------------------------------


# show all food item in western file
def western_item():
    print("="*41, "\n"
          "                Western                  ",)
    print("="*41)
    with open("Western.txt", "r") as western_file:
        count = 1
        western = western_file.readlines()
        for line in western:
            food = line.strip()
            item = food.split(":")
            name = item[0]
            price = item[1]
            print(count, name, "--> RM", price)
            count += 1
# # -----------------------------------------------------------------------------------------------------


# show all food item in dessert file
def dessert_item():
    print("="*41, "\n"
          "                Dessert                  ",)
    print("="*41)
    with open("Dessert.txt", "r") as dessert_file:
        count = 1
        dessert = dessert_file.readlines()
        for line in dessert:
            food = line.strip()
            item = food.split(":")
            name = item[0]
            price = item[1]
            print(count, name, "--> RM", price)
            count += 1
# # -----------------------------------------------------------------------------------------------------


# show all food item in beverage file
def beverage_item():
    print("="*41, "\n"
          "                Beverage                  ",)
    print("="*41)
    with open("Beverage.txt", "r") as beverage_file:
        count = 1
        beverage = beverage_file.readlines()
        for line in beverage:
            food = line.strip()
            item = food.split(":")
            name = item[0]
            price = item[1]
            print(count, name, "--> RM", price)
            count += 1
# # -----------------------------------------------------------------------------------------------------


# ask user if they want to order the food items in rice category
def rice_order():
    while True:
        try:
            print("-"*41)
            print("1. Order Food\n2. Back to Food Category\n3. Log Out")  # show what customer can do
            action = int(input("Please select an action:"))     # customer select an action he want
            print("-"*41)
            if action == 1:    # customer want to order food
                while True:
                    try:
                        print("\nPlease fill in the code of the food you want to order.")
                        line = int(input("Please enter a food code:"))
                        with open("Rice.txt", "r") as rice_file:
                            lines = rice_file.readlines()
                            rice_list = []
                            for item in lines:
                                rice_list.append(item.strip())  # append the food item inside a list
                        # make sure the customer select the food code that is available
                        # if the food code selected is available, write the food item into the file
                        if line in range(1, len(rice_list) + 1):
                            quantity = int(input("How much do you want to order:"))  # ask user how much want to order
                            with open("temporary.txt", "a") as temporary_file:
                                temporary_file.write(f"{quantity}:{rice_list[line - 1]}#")
                            print("\nSuccessfully added to the cart.")
                            cart()
                            break

                        else:
                            print("Invalid food code! Please select an appropriate food code.")

                    except ValueError:
                        print("Invalid food code! Please select an appropriate food code.")

            elif action == 2:
                view_category()      # return to category menu for selecting the other food category

            elif action == 3:
                print("Log out successful.")
                start_menu()  # return to start menu

            elif action == 4:
                break         # go to the next payment function

            else:
                print("Error! Please select an appropriate action.")

        except ValueError:
            print("\nError! Please select an appropriate action.")
# # -----------------------------------------------------------------------------------------------------


# ask user if they want to order the food items in noodle category
def noodle_order():
    while True:
        try:
            print("-"*41)
            print("1 Order Food\n2 Back to Food Category\n3 Log Out")
            action = int(input("Please select an action:"))
            print("-"*41)
            if action == 1:
                while True:
                    try:
                        print("\nPlease fill in the code of the food you want to order.")
                        line = int(input("Please enter a food code:"))
                        with open("Noodle.txt", "r") as noodle_file:
                            lines = noodle_file.readlines()
                            noodle_list = []
                            for item in lines:
                                noodle_list.append(item.strip())
                        if line in range(1, len(noodle_list) + 1):
                            quantity = int(input("How much do you want to order:"))
                            with open("temporary.txt", "a") as temporary_file:
                                temporary_file.write(f"{quantity}:{noodle_list[line - 1]}#")
                            print("\nSuccessfully added to the cart.")
                            cart()
                            break

                        else:
                            print("Invalid food code! Please select an appropriate food code.")

                    except ValueError:
                        print("Invalid food code! Please select an appropriate food code.")
                # break

            elif action == 2:
                view_category()

            elif action == 3:
                print("Log out successful.")
                start_menu()

            elif action == 4:
                break

            else:
                print("Error! Please select an appropriate action.")

        except ValueError:
            print("\nError! Please select an appropriate action.")
# # -----------------------------------------------------------------------------------------------------


# ask user if they want to order the food items in western category
def western_order():
    while True:
        try:
            print("-"*41)
            print("1 Order Food\n2 Back to Food Category\n3 Log Out")
            action = int(input("Please select an action:"))
            print("-"*41)
            if action == 1:
                while True:
                    try:
                        print("\nPlease fill in the code of the food you want to order.")
                        line = int(input("Please enter a food code:"))
                        with open("Western.txt", "r") as western_file:
                            lines = western_file.readlines()
                            western_list = []
                            for item in lines:
                                western_list.append(item.rstrip())
                        if line in range(1, len(western_list) + 1):
                            quantity = int(input("How much do you want to order:"))
                            with open("temporary.txt", "a") as temporary_file:
                                temporary_file.write(f"{quantity}:{western_list[line - 1]}#")
                            print("\nSuccessfully added to the cart.")
                            cart()
                            break

                        else:
                            print("Invalid food code! Please select an appropriate food code.")

                    except ValueError:
                        print("Invalid food code! Please select an appropriate food code.")
                # break

            elif action == 2:
                view_category()

            elif action == 3:
                print("Log out successful.")
                start_menu()

            elif action == 4:
                break

            else:
                print("Error! Please select an appropriate action.")

        except ValueError:
            print("\nError! Please select an appropriate action.")
# # -----------------------------------------------------------------------------------------------------


# ask user if they want to order the food items in dessert category
def dessert_order():
    while True:
        try:
            print("-"*41)
            print("1 Order Food\n2 Back to Food Category\n3 Log Out")
            action = int(input("Please select an action:"))
            print("-"*41)
            if action == 1:
                while True:
                    try:
                        print("\nPlease fill in the code of the food you want to order.")
                        line = int(input("Please enter a food code:"))
                        with open("Dessert.txt", "r") as dessert_file:
                            lines = dessert_file.readlines()
                            dessert_list = []
                            for item in lines:
                                dessert_list.append(item.strip())
                        if line in range(1, len(dessert_list) + 1):
                            quantity = int(input("How much do you want to order:"))
                            with open("temporary.txt", "a") as temporary_file:
                                temporary_file.write(f"{quantity}:{dessert_list[line - 1]}#")
                            print("\nSuccessfully added to the cart.")
                            cart()
                            break

                        else:
                            print("Invalid food code! Please select an appropriate food code.")

                    except ValueError:
                        print("Invalid food code! Please select an appropriate food code.")
                # break

            elif action == 2:
                view_category()

            elif action == 3:
                print("Log out successful.")
                start_menu()

            elif action == 4:
                break

            else:
                print("Error! Please select an appropriate action.")

        except ValueError:
            print("\nError! Please select an appropriate action.")
# # -----------------------------------------------------------------------------------------------------


# ask user if they want to order the food items in beverage category
def beverage_order():
    while True:
        try:
            print("-"*41)
            print("1. Order Food\n2. Back to Food Category\n3. Log Out")
            action = int(input("Please select an action:"))
            print("-"*41)
            if action == 1:
                while True:
                    try:
                        print("\nPlease fill in the code of the food you want to order.")
                        line = int(input("Please enter a food code:"))
                        with open("Beverage.txt", "r") as beverage_file:
                            lines = beverage_file.readlines()
                            beverage_list = []
                            for item in lines:
                                beverage_list.append(item.rstrip())
                        if line in range(1, len(beverage_list) + 1):
                            quantity = int(input("How much do you want to order:"))
                            with open("temporary.txt", "a") as temporary_file:
                                temporary_file.write(f"{quantity}:{beverage_list[line - 1]}#")
                            print("\nSuccessfully added to the cart.")
                            cart()
                            break

                        else:
                            print("Invalid food code! Please select an appropriate food code.")

                    except ValueError:
                        print("Invalid food code! Please select an appropriate food code.")
                # break

            elif action == 2:
                view_category()

            elif action == 3:
                print("Log out successful.")
                start_menu()

            elif action == 4:
                cart()

            else:
                print("Error! Please select an appropriate action.")

        except ValueError:
            print("\nError! Please select an appropriate action.")
# # -----------------------------------------------------------------------------------------------------


# display the food item in cart to customer
def cart():
    print("Your Cart")
    subtotal = 0
    # open the file that record all the food selected by the customer
    with open("temporary.txt", "r") as temporary_file:
        # read the second record of the file that storing the customer's order record
        order_record = temporary_file.readlines()[1]
        data_strip = order_record.strip()
        data = data_strip.split("#")
        for item in data[:-1]:
            split_item = item.split(":")
            quantity = split_item[0]
            food_name = split_item[1]
            food_price = split_item[2]
            # display all the food item that ordered by customer
            print(f"{quantity}x\t{food_name}\t----->\tRM{food_price}")
            subtotal += float(food_price) * float(quantity)    # count the subtotal of price of all the food ordered
        print("-" * 100)
        print(f"Subtotal: RM{subtotal:.2f}")
        print("=" * 100)
    while True:
        try:
            # ask customer whether customer want to check out
            checkout = int(input("Do you want to checkout?\n1. Yes\n2. No\nPlease select 1 for yes or 2 for no:"))
            # check the input from user whether it is available
            if checkout in range(1, 3):
                break

            else:
                print("Invalid option. Please choose from 1 to 2.")

        except ValueError:
            print("Invalid option. Please try again.")
    # if the input is available and equal to one, payment function will be called
    if checkout == 1:
        payment()

    else:
        return view_category()
# # -----------------------------------------------------------------------------------------------------


# for customers to make payment for their order
def payment():
    print("\n**\tOrder Confirmation\t**")
    print("." * 100)
    with open("order.txt", "r") as order_file:
        length = len(order_file.readlines())
        print(f"Order ID: 00{length + 1}")
    with open("temporary.txt", "r") as open_temporary:  # open order record and print out them
        order_record = open_temporary.readlines()[0]
        data_strip = order_record.strip()
        data = data_strip.split(":")
        username = data[0]
        name = data[2]
        tel = data[3]
        email = data[4]
        address = data[5]
        print(f"Username: {username}\nName: {name}\nContact Number: {tel}\nEmail: {email}\nAddress: {address}")
    print("\n")
    total = 0
    subtotal = 0
    with open("temporary.txt", "r") as temporary_file:
        order_record = temporary_file.readlines()[1]
        data_strip = order_record.rstrip()
        data = data_strip.split("#")
        for item in data[:-1]:
            split_item = item.split(":")
            quantity = split_item[0]
            food_name = split_item[1]
            food_price = split_item[2]
            print(f"{quantity}x\t{food_name}\t\tRM{float(food_price):.2f}")
            subtotal += float(food_price) * float(quantity)
        print("-" * 100)
        print(f"Subtotal: RM{subtotal:.2f}")
        tax = subtotal * 6 / 100
        total = subtotal + tax
        print(f"Tax: RM{tax:.2f}")
        print(f"Total: RM{total:.2f}")
        print("-" * 100)
    while True:
        try:
            print("1. Checkout.\n2. Change the delivery address.\n3. Back to Food Menu.\n4. Exit")
            print("\n*Please ensure your address is correct, and We will deliver the order to this address.")
            print("*If you want to change the address, please select option 2.")
            print(
                "**After selecting 'Checkout' you will be redirected to iPay88 to complete your transaction securely.")
            action = int(input("Please select an action:"))
            if action == 1:
                print("\nRedirected to iPay88\nProcessing...\nPlease wait a moment.\n")
                print("Payment Successful!\nYour order will be prepared as soon as possible.")
                print("=" * 100)
                print("Receipt")
                print("-" * 9)
                print(f"Receipt ID: PY00{length + 1}")
                print(f"Order ID: 00{length + 1}")
                from datetime import datetime
                now = datetime.now()
                date = now.strftime("%d/%m/%Y")
                time = now.strftime("%H:%M:%S")
                print("Date:", date)
                print("Time:", time)
                print("Username:", username)
                print("Email:", email)
                print("-" * 100)
                with open("temporary.txt", "r") as temporary_file:
                    order_record = temporary_file.readlines()[1]
                    data_strip = order_record.rstrip()
                    data = data_strip.split("#")
                    for item in data[:-1]:
                        split_item = item.split(":")
                        quantity = split_item[0]
                        food_name = split_item[1]
                        food_price = split_item[2]
                        print(f"{quantity}x\t{food_name}\t\tRM{float(food_price):.2f}")
                    print("-" * 100)
                    print(f"Subtotal: RM{subtotal:.2f}")
                    print(f"Tax: RM{tax:.2f}")
                    print(f"Total: RM{total:.2f}")
                    print("-" * 100)
                    print("Payment Method: iPay88")
                    print("=" * 100)
                with open("order.txt", "a") as open_order:
                    open_order.write(
                        f"Order ID: 00{length + 1}#Username: {username}#Name: {name}#Contact Number: {tel}#Email: {email}#Address: {address}#{data_strip}Receipt ID: PY00{length + 1}#Date: {date}#Time: {time}#Payment Method: iPay88\n")
                    break

            elif action == 2:
                while True:
                    try:
                        print("\nYour current address:", address)
                        new = input("Please enter the new address(No,Street,Region,Postcode,Town):")
                        if new != "":
                            with open("temporary.txt", "r") as open_temporary:  # open order record and print out them
                                order_record = open_temporary.readlines()[0]
                                data_strip = order_record.strip()
                                data = data_strip.split(":")
                                data[5] = new
                                update = ":".join(data)
                                with open("temporary.txt", "r") as temporary_file:
                                    rec = temporary_file.readlines()
                                del rec[0]  # delete the the first record (record of customer's detail)

                                with open("temporary.txt", "w+") as new_file:
                                    new_file.write(update)       # write the new record with new address into the file
                                    for i in rec:
                                        new_file.write(f"\n{i}")
                                print("Your address is updated successfully!")
                                print("." * 100)
                                print("." * 100)
                            print("**\tOrder Confirmation\t**")
                            print("." * 100)
                            print(f"Order ID: 00{length + 1}")
                            print(
                                f"Username: {username}\nName: {name}\nContact Number: {tel}\nEmail: {email}\nAddress: {new}")
                            print("\n")
                            with open("temporary.txt", "r") as temporary_file:
                                order_record = temporary_file.readlines()[1]
                                data_strip = order_record.rstrip()
                                data = data_strip.split("#")
                            for item in data[:-1]:  # need to write the code once again because of looping to write out all of the records
                                split_item = item.split(":")
                                quantity = split_item[0]
                                food_name = split_item[1]
                                food_price = split_item[2]
                                print(f"{quantity}x\t{food_name}\t\tRM{float(food_price):.2f}")
                            print("-" * 100)
                            print(f"Subtotal: RM{subtotal:.2f}")
                            print(f"Tax: RM{tax:.2f}")
                            print(f"Total: RM{total:.2f}")
                            print("-" * 100)
                            break

                        else:
                            print("Error! The address column cannot be empty.")

                    except ValueError:
                        print("Error! The address column cannot be empty.")

            elif action == 3:
                view_category()

            elif action == 4:
                print("Exit successfully.")
                start_menu()

            else:
                print("Error! Please select the action from 1 to 4.")

        except ValueError:
            print("Error! Please select an appropriate action.\n")

    # open the file that record the food ordered by the customer
    with open("temporary.txt", "r") as temporary_file:
        rec = temporary_file.readlines()

    del rec[1]  # delete the the second record (record of food ordered by the customer)

    with open("temporary.txt", "w+") as new_file:
        for data in rec:
            new_file.write(data)  # write again the remaining the record (customer's personal information) into the file

    print("1. Back to Food Category Menu\n2. Log out ")  # ask user what is the next after making the payment
    while True:
        try:
            action = int(input("Please select an option:"))
            # make sure the input is available
            if action in range(1, 3):
                break

            else:
                print("Please select an option from 1 to 2.")

        except ValueError:
            print("Please select an option from 1 to 2 only.")

    if action == 1:
        view_category()

    else:
        print("\nLog out successful.\nThank you and have a nice day.")
        start_menu()
# # -----------------------------------------------------------------------------------------------------

# # Main program # # #
print("\nWelcome to Spiderman Online Food Service!")
start_menu()


