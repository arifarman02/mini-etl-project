import csv

#Return a list of products to make changes to
def print_products():
    product_list = []
    #Read from a file with error handling:
    try:
        with open("products.csv", "r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) > 0:
                    product_list.append({"Product name": row[0], "Product price": row[1] if len(row) > 1 else "0"})
    except FileNotFoundError:
        print("No products.csv file found. Starting with an empty product list.")
    #Add products from the csv file into a list
    if product_list:
        print("Current product list:")
        for index, product in enumerate(product_list):
            print(f"{index}. {product['Product name']}: £{product['Product price']}")
    else:
        print("The product list is currently empty.")    
    return product_list

#Return a list of products from a csv file. Input a product name and price
def add_new_product():
    product_list = print_products()   
    def add_product():
        new_product_name = input("Please enter new product: ")
        new_product_price = input("Please enter product price: ")
        new_product = {"Product name": new_product_name, "Product price": new_product_price}
        product_list.append(new_product)
        #Write the new products list into the csv file
        with open("products.csv", "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["Product name", "Product price"])
            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerow(new_product)
        print(f"Added new product: {new_product}")

    add_product()
    #Ask the user if they would like to add another product
    while True:
        another_product = input("Would you like to add another product (yes or no): ").lower()
        if another_product in ("yes", "y"):
            add_product()
        elif another_product in ("no", "n"):
            break
        else:
            print("Invalid option. Please try again")
    

#Return a list of products from a csv file and print out their index along with name and price
def update_existing_product():
    product_list = print_products()
    
    while True:
        print("Current product list:")
        for index, product in enumerate(product_list):
            print(f"{index}. {product['Product name']}: £{product['Product price']}")
        #Ask for index to update
        while True:
            try:
                update_product_index = int(input(f"Enter the index of the product you want to update (0 to {len(product_list) - 1}): "))
                if 0 <= update_product_index < len(product_list):
                    break  # Valid index entered, exit loop
                else:
                    print(f"Invalid index. Please enter a number between 0 and {len(product_list) - 1}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        #Select the product
        product_to_update = product_list[update_product_index]
        #Enter name or price or leave them blank to keep it the same
        updated_product_name = input(f"Enter the new name for '{product_to_update['Product name']}' (leave blank to keep the same): ")
        if not updated_product_name:
            updated_product_name = product_to_update['Product name']
        
        updated_product_price_input = input(f"Enter the new price for '{updated_product_name}' (leave blank to keep the same): ")
        if updated_product_price_input:
            try:
                updated_product_price = float(updated_product_price_input)
            except ValueError:
                print("Invalid input. Keeping the old price.")
                updated_product_price = product_to_update['Product price']
        else:
            updated_product_price = product_to_update['Product price']

        product_list[update_product_index] = {"Product name": updated_product_name, "Product price": updated_product_price}

        print(f"Product at index {update_product_index} updated to '{updated_product_name}' with price {updated_product_price}.")
        print("Updated product list:")
        for index, product in enumerate(product_list):
            print(f"{index}. {product['Product name']}: £{product['Product price']}")
        #Write the update into the csv file
        with open("products.csv", "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["Product name", "Product price"])
            writer.writeheader()
            writer.writerows(product_list)
        #Ask the user to if they would like to update another prodcut
        while True:
            update_another_product = input("Would you like to update another product (yes or no): ").lower()
            if update_another_product in ("yes", "y"):
                break
            elif update_another_product in ("no", "n"):
                return
            else:
                print("Invalid option. Please enter 'yes' or 'no'.")


#Return list from a csv file to delete a product
def delete_product():
    product_list = print_products()
    
    if not product_list:
        print("Product list is empty")
        return

    while True:
        print("Current product list:")
        for index, product in enumerate(product_list):
            print(f"{index}. {product['Product name']}: £{product['Product price']}")

        while True:
            try:
                remove_product_index = int(input(f"Enter the index of the product you want to remove (0 to {len(product_list) - 1}): "))
                if 0 <= remove_product_index < len(product_list):
                    removed_product = product_list.pop(remove_product_index)
                    print(f"Removed product: {removed_product['Product name']}")
                    #Write the updated product list into the csv file
                    with open("products.csv", "w", newline="") as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=["Product name", "Product price"])
                        writer.writeheader()
                        writer.writerows(product_list)

                    break  
                else:
                    print(f"Invalid index. Please enter a number between 0 and {len(product_list) - 1}")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if not product_list:
            print("Product list is empty")
            return

        delete_another_product = input("Would you like to delete another product (yes or no): ").lower()
        if delete_another_product not in ("yes", "y"):
            break