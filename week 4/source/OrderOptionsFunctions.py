import csv

#Return a list of orders to make changes to
def print_orders():
    orders_list = []
    #Read from a file with error handling:
    try:
        with open("orders.csv", "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                orders_list.append(row)
    except FileNotFoundError:
        print("No orders.csv file found. Starting with an empty orders list.")
    #Add orders from the csv file into a list
    if orders_list:
        print("Current orders list:")
        for index, order in enumerate(orders_list):
            print(index, order)
    else:
        print("The orders list is currently empty.")
    
    return orders_list
'''Make the output more clearer. It's in dictionary format'''

#Return a list of orders from a csv file. Input a name, address, phone number
def create_new_order():
    orders_list = print_orders()
    
    while True:
        name = input("Please enter name: ")
        address = input("Please enter address: ")
        phone_number = input("Please enter phone number: ")
        order_status = "PREPARING"
        order = {"name": name, "address": address, "phone_number": phone_number, "order_status": order_status}
        orders_list.append(order)
        print(order)
        #Write the new orders list into the csv file
        with open("orders.csv", "w", newline="") as csvfile:
            fieldnames = orders_list[0].keys() if orders_list else []
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(orders_list)
        #Ask the user if they would like to add another order
        another_order = input("Would you like to add another order (yes or no): ").lower()
        if another_order not in ("yes", "y"):
            break

#Return a list of orders from a csv file and print out their index along with name, address, phone number
def update_existing_order():
    orders_list = print_orders()
    if not orders_list:
        print("Orders list is empty")
        return

    while True:
        for index, order in enumerate(orders_list):
            print(index, order)
        #Ask for index to update
        while True:
            try:
                
                update_order_index = int(input(f"Enter the index of the order you want to update (0 to {len(orders_list) - 1}): "))
                if 0 <= update_order_index < len(orders_list):
                    break
                else:
                    print(f"Invalid index. Please enter a number between 0 and {len(orders_list) - 1}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        #Select the product
        update_order = orders_list[update_order_index]
        
        for key in update_order:
            print(key)
        #Enter a correct key to update
        while True:
            key_input = input("Enter the key you want to update: ")
            if key_input in update_order:
                break
            else:
                print("Invalid key. Enter one of the valid keys")
        
        new_value = input("Input the new value: ")
        update_order[key_input] = new_value
        
        print(f"Order at index {update_order_index} updated. Updated order: {update_order}")
        print("The orders list has been updated in place.")
        #Write the update into the csv file
        with open("orders.csv", "w", newline="") as csvfile:
            fieldnames = orders_list[0].keys() if orders_list else []
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(orders_list)
        #Ask the user to if they would like to update another order
        another_update = input("Would you like to update another order (yes or no): ").lower()
        if another_update not in ("yes", "y"):
            break

def update_existing_order_status():
    orders_list = print_orders()
    if not orders_list:
        print("Orders list is empty")
        return
    #Return a list of orders from a csv file and print out their index along with name, address, phone number
    while True:
        for index, order in enumerate(orders_list):
            print(index, order)
        
        while True:
            try:
                update_order_index = int(input(f"Enter the index of the order you want to update (0 to {len(orders_list) - 1}): "))
                if 0 <= update_order_index < len(orders_list):
                    break
                else:
                    print(f"Invalid index. Please enter a number between 0 and {len(orders_list) - 1}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        #Select the key
        update_order = orders_list[update_order_index]
        new_status = input("Enter the new status for the order: ")
        update_order["order_status"] = new_status

        print(f"Order status updated for order at index {update_order_index}. Updated order: {update_order}")
        print("The orders list has been updated in place.")
        #Write the update into the csv file
        with open("orders.csv", "w", newline="") as csvfile:
            fieldnames = orders_list[0].keys() if orders_list else []
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(orders_list)

        another_update = input("Would you like to update another order status (yes or no): ").lower()
        if another_update not in ("yes", "y"):
            break

#Return list from a csv file to delete an order
def delete_order():
    orders_list = print_orders()
    if not orders_list:
        print("No orders.")
        return

    while True:
        for index, order in enumerate(orders_list):
            print(index, order)

        while True:
            try:
                delete_order_index = int(input("Enter the index of the order you want to delete: "))
                if 0 <= delete_order_index < len(orders_list):
                    del orders_list[delete_order_index]
                    print("Order deleted.")
                    break
                else:
                    print(f"Invalid index. Please enter a number between 0 and {len(orders_list) - 1}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        #Write the updated order list into the csv file
        with open("orders.csv", "w", newline="") as csvfile:
            fieldnames = orders_list[0].keys() if orders_list else []
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(orders_list)

        another_delete = input("Would you like to delete another order (yes or no): ").lower()
        if another_delete not in ("yes", "y"):
            break