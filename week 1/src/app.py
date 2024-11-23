products_list = ["Water", "Coffee", "Coke", "Whisky"]
main_menu = ["0 - Exit app", "1 - Print Products List", "2 - Create New Product", "3 - Update Existing Product", "4 - Delete Product"]

print(main_menu)
 

while True: #Creates a repeating loop, only exiting when we enter 0
    menu_input = int(input("Choose an option: "))
    if menu_input == 0:
        exit() #Exits the entire program
    elif menu_input == 1: #Prints product list
        print(products_list)
    elif menu_input == 2: #Adds a new product to the list. 
        new_product = input("Please enter new product: ")
        products_list.append(new_product)
        print(products_list)
    elif menu_input == 3:  # Updates an existing product
        print(products_list)
        # Improved input validation for index selection
        while True:
            try:
                update_index = int(input("Enter the index of the product you want to update (0 to " + str(len(products_list) - 1) + "): "))
                if 0 <= update_index < len(products_list):
                    break  # Valid index entered, exit loop
                else:
                    print("Invalid index. Please enter a number between 0 and", len(products_list) - 1)
            except ValueError:
                print("Invalid input. Please enter a number.")
        updated_product = input("Enter the new name for the product: ")
        products_list[update_index] = updated_product
        print(f"Product at index {update_index} updated to '{updated_product}'. Updated list:", products_list)
    elif menu_input == 4:
        print(products_list)
        remove_product = int(input("Enter the index of the product you want to remove: ")) #Removes a product. Have to give the index though
        products_list.remove(products_list[remove_product])
        print (products_list)