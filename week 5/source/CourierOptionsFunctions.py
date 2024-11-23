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

#Function to print couriers and return a list of couriers
def print_couriers():
    #Connect to database
    try:
        con = pymysql.connect(
            host=host_name,
            database=database_name,
            user=user_name,
            password=user_password
        )       
        with con.cursor() as cursor:
            #Select everything from the courier table
            cursor.execute("SELECT courier_id, first_name, last_name FROM couriers")
            couriers = cursor.fetchall()
            couriers_list = [list(courier) for courier in couriers]
            if not couriers_list:
                print("No couriers found in the database.")
            else:
                print("Fetched couriers:")
                for courier in couriers_list:
                    print(f"ID: {courier[0]}. {courier[1]} {courier[2]}")
            return couriers_list           
    except pymysql.MySQLError as e:
        print("MySQL Error:", e)
        return []
    finally:
        #Close connection
        con.close()

#Function to return a list of couriers to add another courier
def create_new_courier():
    def add_courier():
        #Connect to database
        try:
            with pymysql.connect(
                host=host_name,
                database=database_name,
                user=user_name,
                password=user_password
            ) as con:
                cursor = con.cursor()
                new_courier_fname = input("Please enter first name: ")
                new_courier_lname = input("Please enter last name: ")
                #Input values into the table
                sql = """
                INSERT INTO couriers (first_name, last_name)
                VALUES (%s, %s)
                """
                courier_values = (new_courier_fname, new_courier_lname)
                cursor.execute(sql, courier_values)
                #Save changes
                con.commit()
                #Close connection
                cursor.close()
        except Exception as ex:
            print('Failed to:', ex)
    add_courier()
    #Ask the user if they would like to enter another courier
    while True:
        another_courier = input("Would you like to add another courier (yes or no): ").lower()
        if another_courier in ("yes", "y"):
            add_courier()
        elif another_courier in ("no", "n"):
            break
        else:
            print("Invalid option. Please try again")

#Function to return a list of couriers to update
def update_existing_courier():
    def update_courier():
        couriers = print_couriers()
        if not couriers:
            print("Courier list is empty")
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
                        courier_id = int(input("Enter the ID of the courier you want to update: "))
                        courier_ids = [courier[0] for courier in couriers]
                        if courier_id not in courier_ids:
                            print("Invalid courier ID. Please try again.")
                            continue
                        #Enter new updates or leave blank to keep the old one
                        new_courier_fname = input("Enter new courier first name (leave blank to keep old first name): ")
                        new_courier_lname = input("Enter new courier last name (leave blank to keep old last name): ")
                        sql = "UPDATE couriers SET "
                        #Update first or last name or both
                        update_data = []
                        if new_courier_fname:
                            sql += "first_name = %s, "
                            update_data.append(new_courier_fname)
                        if new_courier_lname:
                            sql += "last_name = %s, "
                            update_data.append(new_courier_lname)
                        sql = sql.rstrip(", ") + " WHERE courier_id = %s"
                        update_data.append(courier_id)
                        cursor.execute(sql, update_data)
                        #Save changes
                        con.commit()
                        print("Courier updated successfully!")
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid numeric courier ID.")
                    except Exception as ex:
                        print("Failed to update courier:", ex)
                        break
        except Exception as ex:
            print("Failed to connect to the database:", ex)
    update_courier()
    #Ask if the user would like to update another courier
    while True:
        update_another_courier = input("Would you like to update another courier (yes or no): ").lower()
        if update_another_courier in ("yes", "y"):
            update_courier()
        elif update_another_courier in ("no", "n"):
            break
        else:
            print("Invalid option. Please try again")        

#Function to return a list of couriers to delete
def delete_courier():
    courier_list = print_couriers()   
    if not courier_list:
        print("courier list is empty")
        return
    while True:
        print("Current courier list:")
        for courier in courier_list:
            print(f"ID: {courier[0]}. {courier[1]} {courier[2]}")
        try:
            #Ask for ID
            remove_courier_id = int(input("Enter the ID of the courier you want to remove: "))
            courier_ids = [courier[0] for courier in courier_list]
            if remove_courier_id not in courier_ids:
                print("Invalid courier ID. Please try again.")
                continue
            #Connect to database           
            with pymysql.connect(
                host=host_name,
                database=database_name,
                user=user_name,
                password=user_password
            ) as con:
                cursor = con.cursor()
                cursor.execute("DELETE FROM couriers WHERE courier_id = %s", (remove_courier_id,))
                con.commit()
                print(f"Removed courier with ID: {remove_courier_id}")
                courier_list = print_couriers()
                if not courier_list:
                    print("courier list is empty")
                    return
        except Exception as ex:
            print("Failed to delete courier:", ex)
        #Ask the user if they would like to delete another record
        delete_another_courier = input("Would you like to delete another courier (yes or no): ").lower()
        if delete_another_courier not in ("yes", "y"):
            break