product_list = ["Water", "Coffee", "Coke", "Whisky"]
main_menu = ["0 - Exit app", "1 - Print Products options", "2 - Orders"]
product_options = ["0 - Return to main menu", "1 - Print Products List", "2 - Create New Product", "3 - Update Existing Product", "4 - Delete Product"]
orders_options = ["0 - Return to main menu", "1 - Print orders", "2 - Create New order", "3 - Update Existing order status", "4 - Update Existing order", "5 - Delete order"]
orders = []
couriers = []
courier_options = ["0 - Return to main menu", "1 - Print Courier List", "2 - Create New Courier", "3 - Update Existing Courier", "4 - Delete Courier"]

def take_order():
    name = input("Please enter name: ")
    address = input("Please enter address: ")
    phone_number = int(input("Please enter phone number: "))
    order_status = "PREPARING"
    order = {"name": name, "address": address, "phone_number": phone_number, "order status": order_status}
    orders.append(order)

print(main_menu)
 

while True: #Creates a repeating loop, only exiting when we enter 0
    menu_input = int(input("Choose from the main menu options: "))
    print(main_menu)
    if menu_input == 0:
        exit() #Exits the entire program
    elif menu_input == 1:
        while True:
            print(product_options) #Prints product list
            product_menu_input = int(input("Choose product options: "))
            if product_menu_input == 0:
                print(main_menu)
                break
            elif product_menu_input == 1:
                print(product_list)
            elif product_menu_input == 2: #Adds a new product to the list. 
                new_product = input("Please enter new product: ")
                product_list.append(new_product)
                print(product_list)
            elif product_menu_input == 3:  # Updates an existing product
                #print(product_list)
                for index, product in enumerate(product_list):
                    print(index, product)
                while True:
                    try:
                        update_index = int(input("Enter the index of the product you want to update (0 to " + str(len(product_list) - 1) + "): "))
                        if 0 <= update_index < len(product_list):
                            break  # Valid index entered, exit loop
                        else:
                            print("Invalid index. Please enter a number between 0 and", len(product_list) - 1)
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                updated_product = input("Enter the new name for the product: ")
                product_list[update_index] = updated_product
                print(f"Product at index {update_index} updated to '{updated_product}'. Updated list:", product_list)
            elif product_menu_input == 4:
                print(product_list)
                while True:
                    try:
                        remove_product = int(input("Enter the index of the product you want to remove (0 to " + str(len(product_list) - 1) + "): "))
                        if 0 <= remove_product < len(product_list):
                            break  # Valid index entered, exit loop
                        else:
                            print("Invalid index. Please enter a number between 0 and", len(product_list) - 1)
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                #remove_product = int(input("Enter the index of the product you want to remove: ")) #Removes a product. Have to give the index though
                product_list.remove(product_list[remove_product])
                print (product_list)
    elif menu_input == 2:
        while True:
            print()




    elif menu_input == 3:
        while True:
            print (orders_options)
            orders_options_input = int(input("Choose order options: "))
            if orders_options_input == 0:
                break
            elif orders_options_input == 1:
                print (f"Here are the current {orders}")
            elif orders_options_input == 2:
                take_order()
            elif orders_options_input == 3:
                print("update status")
            
            elif orders_options_input == 4:
                    for index, order in enumerate(orders):
                        print(index, order)
                    while True:
                        try:
                            update_order_index = int(input("Enter the index of the order you want to update (0 to " + str(len(orders) - 1) + "): "))
                            if 0 <= update_order_index < len(orders):
                                break  # Valid index entered, exit loop
                            else:
                                print("Invalid index. Please enter a number between 0 and", len(orders) - 1)
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                    update_order = orders[update_order_index]
                    for key in update_order:
                        print(key)
                    while True:
                        key_input = input("Enter the key you want to update: ")
                        if key_input in update_order:
                            break
                        else:
                            print("Invalid key. Enter one of the valid keys")
                    new_value = input("Input the new value: ")
                    update_order[key_input] = new_value
                    print(f"Order at index {update_order_index} updated. Updated order: {update_order}")
                    print("Updated list of orders:", orders)
            elif orders_options_input == 5:
                if not order:
                    print("No orders.")
                    continue
                for index, order in enumerate(orders):
                    print(index, order)
                while True:
                    try:
                        delete_order_index = int(input("Enter the index of the order you want to delete: "))
                        if 0 <= delete_order_index < len(orders):
                            del orders[delete_order_index]
                            break
                        else:
                            print("Invalid index. Please enter a number between 0 and", len(orders)-1)
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                print("Order deleted. Updates list of orders:", orders)        
