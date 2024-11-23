import pymysql
import os
from dotenv import load_dotenv
import csv

#Set variables to connect to database
load_dotenv()
host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")

#Function to print orders and return a list of orders
def print_orders():
    #Connect to database
    try:
        con = pymysql.connect(
            host=host_name,
            database=database_name,
            user=user_name,
            password=user_password
        )        
        with con.cursor() as cursor:
            #Select everything from the order table
            cursor.execute("SELECT order_id, name, address, phone_number, order_status FROM orders")
            orders = cursor.fetchall()
            orders_list = [list(order) for order in orders]
            if not orders_list:
                print("No orders found in the database.")
            else:
                print("Fetched orders:")
                for order in orders_list:
                    print(f"ID: {order[0]}. name: {order[1]}, address: {order[2]}, phone_number: {order[3]}, order_status: {order[4]}")
            return orders_list          
    except pymysql.MySQLError as e:
        print("MySQL Error:", e)
        return []
    finally:
        #Close connection
        con.close()

#Function to return a list of orders to add another order
def create_new_order():
    def add_order():
        #Connect to database
        try:
            with pymysql.connect(
                host=host_name,
                database=database_name,
                user=user_name,
                password=user_password
            ) as con:
                cursor = con.cursor()
                new_order_name = input("Please enter a name: ")
                new_order_address = input("Please enter an address: ")
                new_order_phone_number = input("Please enter a phone number: ")
                new_order_status = "PREPARING"
                #Input values into the table
                sql = """
                INSERT INTO orders (name, address, phone_number, order_status)
                VALUES (%s, %s, %s, %s)
                """
                order_values = (new_order_name, new_order_address, new_order_phone_number, new_order_status)
                cursor.execute(sql, order_values)
                #Save changes
                con.commit()
                #Close connection
                cursor.close()
        except Exception as ex:
            print('Failed to:', ex)
    add_order()
    #Ask the user if they would like to enter another order
    while True:
        another_order = input("Would you like to add another order (yes or no): ").lower()
        if another_order in ("yes", "y"):
            add_order()
        elif another_order in ("no", "n"):
            break
        else:
            print("Invalid option. Please try again")

#Function to return a list of orders to update
def update_existing_order():
    def update_order():
        orders = print_orders()
        if not orders:
            print("Order list is empty")
            return
        #Connect to database
        try:
            with pymysql.connect(
                host=host_name,
                database=database_name,
                user=user_name,
                password=user_password
            ) as con:
                cursor = con.cursor()
                while True:
                    #Ask for ID
                    try:
                        order_id = int(input("Enter the ID of the order you want to update: "))
                        order_ids = [order[0] for order in orders]
                        if order_id not in order_ids:
                            print("Invalid order ID. Please try again.")
                            continue
                        #Enter new updates or leave blank to keep the old one
                        new_order_name = input("Enter new order name (leave blank to keep old name): ")
                        new_order_address = input("Enter new order address (leave blank to keep old address): ")
                        new_order_phone_number = input("Enter new order phone number (leave blank to keep old phone number): ")
                        sql = "UPDATE orders SET "
                        #Update name or address or phone number or all
                        update_data = []
                        if new_order_name:
                            sql += "order_name = %s, "
                            update_data.append(new_order_name)
                        if new_order_address:
                            sql += "order_address = %s, "
                            update_data.append(new_order_address)
                        if new_order_phone_number:
                            sql += "phone_number = %s, "
                            update_data.append(new_order_phone_number)
                        sql = sql.rstrip(", ") + " WHERE order_id = %s"
                        update_data.append(order_id)
                        cursor.execute(sql, update_data)
                        #Save changes
                        con.commit()
                        print("Order updated successfully!")
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid numeric order ID.")
                    except Exception as ex:
                        print("Failed to update order:", ex)
                        break
        except Exception as ex:
            print("Failed to connect to the database:", ex)
    update_order()
    #Ask the user if they would like to enter another order
    while True:
        update_another_order = input("Would you like to update another order (yes or no): ").lower()
        if update_another_order in ("yes", "y"):
            update_order()
        elif update_another_order in ("no", "n"):
            break
        else:
            print("Invalid option. Please try again")   

#Function to return a list of orders to update
def update_existing_order_status():
    orders_list = print_orders()
    if not orders_list:
        print("Orders list is empty")
        return
    while True:
        print("Current orders list:")
        for order in orders_list:
            print(f"ID: {order[0]}. {order[1]}, {order[2]}, {order[3]}, {order[4]}")      
        while True:
            #Select ID
            try:
                update_order_id = int(input(f"Enter the ID of the order you want to update: "))
                order_ids = [order[0] for order in orders_list]
                if update_order_id not in order_ids:
                    print("Invalid order ID. Please try again.")
                    continue
                new_status = input("Enter the new status for the order: ")
                break
            except ValueError:
                print("Invalid input. Please enter a valid numeric order ID.")
            except Exception as ex:
                print("Failed to update order status:", ex)
                break
        #Connect to database
        try:
            with pymysql.connect(
                host=host_name,
                database=database_name,
                user=user_name,
                password=user_password
            ) as con:
                cursor = con.cursor()
                #Inser values
                cursor.execute(
                    "UPDATE orders SET order_status = %s WHERE order_id = %s",
                    (new_status, update_order_id)
                )
                #Save changes
                con.commit()
                print(f"Order status updated for order with ID {update_order_id}.")
                orders_list = print_orders()
                if not orders_list:
                    print("Orders list is empty")
                    return
        except Exception as ex:
            print("Failed to connect to the database or update the order:", ex)       
        another_update = input("Would you like to update another order status (yes or no): ").lower()
        if another_update not in ("yes", "y"):
            break

#Function to return a list of orders to delete
def delete_order():
    order_list = print_orders()   
    if not order_list:
        print("Order list is empty")
        return
    while True:
        print("Current order list:")
        for order in order_list:
            print(f"ID: {order[0]}. {order[1]} {order[2]} {order[3]}")
        #Ask for ID
        try:
            remove_order_id = int(input("Enter the ID of the order you want to remove: "))
            order_ids = [order[0] for order in order_list]
            if remove_order_id not in order_ids:
                print("Invalid product ID. Please try again.")
                continue
            #Connect to database                 
            with pymysql.connect(
                host=host_name,
                database=database_name,
                user=user_name,
                password=user_password
            ) as con:
                cursor = con.cursor()
                cursor.execute("DELETE FROM orders WHERE order_id = %s", (remove_order_id,))
                con.commit()
                print(f"Removed order with ID: {remove_order_id}")
                order_list = print_orders()
                if not order_list:
                    print("Order list is empty")
                    return
        except Exception as ex:
            print("Failed to delete order:", ex)
        #Ask the user if they would like to delete another record
        delete_another_order = input("Would you like to delete another order (yes or no): ").lower()
        if delete_another_order not in ("yes", "y"):
            break