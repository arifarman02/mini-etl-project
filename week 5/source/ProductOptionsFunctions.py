import csv
import pymysql
import os
from dotenv import load_dotenv

#Set variables to connect to database
load_dotenv()
host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")

#Function to print productss and return a list of productss
def print_products():
    #Connect to database
    try:
        con = pymysql.connect(
            host=host_name,
            database=database_name,
            user=user_name,
            password=user_password
        )
        with con.cursor() as cursor:
            #Select everything from the products table
            cursor.execute("SELECT product_id, product_name, product_price FROM products")
            products = cursor.fetchall()
            products_list = [list(product) for product in products]           
            if not products_list:
                print("No products found in the database.")
            else:
                print("Fetched products:")
                for product in products_list:
                    print(f"ID: {product[0]}. {product[1]} £{product[2]}")
            return products_list           
    except pymysql.MySQLError as e:
        print("MySQL Error:", e)
        return []
    finally:
        #Close connection
        con.close()

#Function to return a list of productss to add another products
def add_new_product():
    def add_product():
        #Connect to database
        try:
            with pymysql.connect(
                host=host_name,
                database=database_name,
                user=user_name,
                password=user_password
            ) as con:
                cursor = con.cursor()
                new_product_name = input("Please enter new product: ")
                new_product_price = input("Please enter product price: ")
                #Input values into the table
                sql = """
                INSERT INTO products (product_name, product_price)
                VALUES (%s, %s)
                """
                product_values = (new_product_name, new_product_price)
                cursor.execute(sql, product_values)
                #Save changes
                con.commit()
                #Close connection
                cursor.close()
        except Exception as ex:
            print('Failed to:', ex)
    add_product()
    #Ask the user if they would like to enter another products
    while True:
        another_product = input("Would you like to add another product (yes or no): ").lower()
        if another_product in ("yes", "y"):
            add_product()
        elif another_product in ("no", "n"):
            break
        else:
            print("Invalid option. Please try again") 

#Function to return a list of productss to update
def update_existing_product():
    def update_product():
        products = print_products()
        if not products:
            print("Product list is empty")
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
                        product_id = int(input("Enter the ID of the product you want to update: "))
                        product_ids = [product[0] for product in products]
                        if product_id not in product_ids:
                            print("Invalid product ID. Please try again.")
                            continue
                        #Enter new updates or leave blank to keep the old one
                        new_product_fname = input("Enter new product product name (leave blank to keep old product name): ")
                        new_product_lname = input("Enter new product price (leave blank to keep old price): ")
                        sql = "UPDATE products SET "
                        #Update product name or price or both
                        update_data = []
                        if new_product_fname:
                            sql += "product_name = %s, "
                            update_data.append(new_product_fname)
                        if new_product_lname:
                            sql += "product_price = %s, "
                            update_data.append(new_product_lname)
                        sql = sql.rstrip(", ") + " WHERE product_id = %s"
                        update_data.append(product_id)
                        cursor.execute(sql, update_data)
                        #Save changes
                        con.commit()
                        print("product updated successfully!")
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid numeric product ID.")
                    except Exception as ex:
                        print("Failed to update product:", ex)
                        break
        except Exception as ex:
            print("Failed to connect to the database:", ex)
    update_product()
    #Ask if the user would like to update another product
    while True:
        update_another_product = input("Would you like to update another product (yes or no): ").lower()
        if update_another_product in ("yes", "y"):
            update_product()
        elif update_another_product in ("no", "n"):
            break
        else:
            print("Invalid option. Please try again")

#Function to return a list of productss to delete
def delete_product():
    product_list = print_products()   
    if not product_list:
        print("Product list is empty")
        return
    while True:
        print("Current product list:")
        for product in product_list:
            print(f"ID: {product[0]}. {product[1]} £{product[2]}")
        try:
            #Ask for ID
            remove_product_id = int(input("Enter the ID of the product you want to remove: "))
            product_ids = [product[0] for product in product_list]
            if remove_product_id not in product_ids:
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
                cursor.execute("DELETE FROM products WHERE product_id = %s", (remove_product_id,))
                con.commit()
                print(f"Removed product with ID: {remove_product_id}")
                product_list = print_products()
                if not product_list:
                    print("Product list is empty")
                    return
        except Exception as ex:
            print("Failed to delete product:", ex)
        #Ask the user if they would like to delete another record
        delete_another_product = input("Would you like to delete another product (yes or no): ").lower()
        if delete_another_product not in ("yes", "y"):
            break