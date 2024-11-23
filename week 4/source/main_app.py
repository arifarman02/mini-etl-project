from ProductOptionsFunctions import *
from OrderOptionsFunctions import *
from CourierOptionsFunctions import *
import csv

#Function to call other product functions
def products_options():
    print("These are the product options.")
    print("0 - Return to main menu, 1 - Print products List, 2 - Create new product, 3 - Update existing product, 4 - Delete product")
    while True:
        try:
            product_menu_input = int(input("Please select an option: "))
            if product_menu_input in (0, 1, 2, 3, 4):
                break
            else:
                print("Invalid option entered. Please try again")
        except ValueError:
                        print("Invalid input. Please enter a number.")
    if product_menu_input == 0:
                main_menu()
    elif product_menu_input == 1:
                print_products()
                products_options()
    elif product_menu_input == 2: #Adds a new product to the list. 
                add_new_product()
                products_options()
    elif product_menu_input == 3:
          update_existing_product()
          products_options()
    elif product_menu_input == 4:
           delete_product()
           products_options()

#Function to call other order functions
def order_options():
    print("These are the order options")
    print("0 - Return to main menu, 1 - Print orders, 2 - Create new order, 3 - Update existing order status, 4 - Update existing order, 5 - Delete order")
    while True:
        try:
            order_options_input = int(input("Please select an option: "))
            if order_options_input in (0, 1, 2, 3, 4, 5):
                break
            else:
                print("Invalid option entered. Please try again")
        except ValueError:
                        print("Invalid input. Please enter a number.")
    if order_options_input == 0:
                main_menu()
    elif order_options_input == 1:
                print_orders()
                order_options()
    elif order_options_input == 2: 
                create_new_order()
                order_options()
    elif order_options_input == 3:
      update_existing_order_status()
      order_options()
    elif order_options_input == 4:
           update_existing_order()
           order_options()
    elif order_options_input == 5:
           delete_order()
           order_options()

#Function to call other courier options
def courier_options():
      print("These are the couriers options")
      print("0 - Return to main menu, 1 - Print couriers list, 2 - Create a new courier, 3 - Update existing courier, 4 - Delete courier")
      while True:
            try:
                  courier_options_input = int(input("Please select an option: "))
                  if courier_options_input in (0, 1, 2, 3, 4):
                        break
                  else:
                        print("Invalid options entered. Please try again")
            except ValueError:
                  print("Invalid input. Please enter a number.")
      if courier_options_input == 0:
            main_menu()
      elif courier_options_input == 1:
            print_couriers()
            courier_options()
      elif courier_options_input == 2:
            create_new_courier()
            courier_options()
      elif courier_options_input == 3:
            update_existing_courier()
            courier_options()
      elif courier_options_input == 4:
            delete_courier()
            courier_options()

#Function to navigate to and from products, couriers and order options
def main_menu():
    print("Welcome to the admin menu.")
    print("0 - Exit app", "1 - Products options", "2 - Couriers", "3 - Order options")
    while True:
        try:
            menu_input = int(input("Please select an option: "))
            if menu_input in (0, 1, 2, 3):
                break
            else:
                print("Invalid option entered. Please try again")
        except ValueError:
                        print("Invalid input. Please enter a number.")
    if menu_input == 0:
        exit()
    elif menu_input == 1:
          products_options()
    elif menu_input == 2:
          courier_options()
    elif menu_input == 3:
          order_options()

main_menu()
