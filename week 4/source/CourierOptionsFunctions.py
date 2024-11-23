import csv

#Return a list of couriers to make changes to
def print_couriers():
    couriers_list = []
    #Read from a file with error handling:
    try:
        with open("couriers.csv", "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                couriers_list.append(row)
    except FileNotFoundError:
        print("No couriers.csv file found. Starting with an empty couriers list.")
    #Add couriers from the csv file into a list
    if couriers_list:
        print("Current couriers list:")
        for index, courier in enumerate(couriers_list):
            print(index, courier)
    else:
        print("The couriers list is currently empty.")
    
    return couriers_list

#Return a list of couriers from a csv file. Input a courier first name and last name
def create_new_courier():
    couriers_list = print_couriers()
    
    def add_courier():
        new_courier_fname = input("Please enter first name: ")
        new_courier_lname = input("Please enter last name: ")
        new_courier = {"First name": new_courier_fname, "Last name": new_courier_lname}
        couriers_list.append(new_courier)
        #Write the new couriers list into the csv file
        print(f"Added new courier: {new_courier}")

    add_courier()
    #Ask the user if they would like to add another courier
    while True:
        another_courier = input("Would you like to add another courier (yes or no): ").lower()
        if another_courier in ("yes", "y"):
            add_courier()
        elif another_courier in ("no", "n"):
            break
        else:
            print("Invalid option. Please try again")

    with open("couriers.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["First name", "Last name"])
        writer.writeheader()
        writer.writerows(couriers_list)

#Return a list of couriers from a csv file and print out their index along with first name and last name
def update_existing_courier():
    couriers_list = print_couriers()
    
    while True:
        print("Current couriers list:")
        for index, name in enumerate(couriers_list):
            print(f"{index}. {name['First name']} {name['Last name']}")
        #Ask for index to update
        while True:
            try:
                update_courier_index = int(input(f"Enter the index of the courier you want to update (0 to {len(couriers_list) - 1}): "))
                if 0 <= update_courier_index < len(couriers_list):
                    break  # Valid index entered, exit loop
                else:
                    print(f"Invalid index. Please enter a number between 0 and {len(couriers_list) - 1}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        #Select the courier
        courier_to_update = couriers_list[update_courier_index]
        #Enter first name or last name or leave them blank to keep it the same
        updated_courier_fname = input(f"Enter the new first name for '{courier_to_update['First name']}' (leave blank to keep the same): ")
        if not updated_courier_fname:
            updated_courier_fname = courier_to_update['First name']
        
        updated_courier_lname = input(f"Enter the new last name for '{courier_to_update['Last name']}' (leave blank to keep the same): ")
        if not updated_courier_lname:
            updated_courier_lname = courier_to_update['Last name']

        couriers_list[update_courier_index] = {"First name": updated_courier_fname, "Last name": updated_courier_lname}

        print(f"Name at index {update_courier_index} updated to '{updated_courier_fname} {updated_courier_lname}'.")
        print("Updated courier list:")
        for index, name in enumerate(couriers_list):
            print(f"{index}. {name['First name']} {name['Last name']}")
        #Write the update into the csv file
        with open("couriers.csv", "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["First name", "Last name"])
            writer.writeheader()
            writer.writerows(couriers_list)
        #Ask the user to if they would like to update another courier
        while True:
            update_another_courier = input("Would you like to update another courier (yes or no): ").lower()
            if update_another_courier in ("yes", "y"):
                break
            elif update_another_courier in ("no", "n"):
                return
            else:
                print("Invalid option. Please enter 'yes' or 'no'.")

#Return list from a csv file to delete a courier
def delete_courier():
    couriers_list = print_couriers()
    
    if not couriers_list:
        print("Courier list is empty")
        return

    while True:
        print("Current courier list:")
        for index, name in enumerate(couriers_list):
            print(f"{index}. {name['First name']}: ${name['Last name']}")

        try:
            remove_courier_index = int(input(f"Enter the index of the courier you want to remove (0 to {len(couriers_list) - 1}): "))
            if 0 <= remove_courier_index < len(couriers_list):
                removed_courier = couriers_list.pop(remove_courier_index)
                print(f"Removed courier: {removed_courier['courier name']}")
                #Write the updated courier list into the csv file
                with open("couriers.csv", "w", newline="") as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=["First name", "Last name"])
                    writer.writeheader()
                    writer.writerows(couriers_list)

                break
            else:
                print(f"Invalid index. Please enter a number between 0 and {len(couriers_list) - 1}")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    while True:
        delete_another_courier = input("Would you like to delete another courier (yes or no): ").lower()
        if delete_another_courier in ("yes", "y"):
            if not couriers_list:
                print("Courier list is empty")
                return
            continue
        elif delete_another_courier in ("no", "n"):
            break
        else:
            print("Invalid option. Please enter 'yes' or 'no'.")