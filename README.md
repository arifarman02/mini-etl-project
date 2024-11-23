# About:
This is a small program written in Python to showcase what was learned in the Python lessons in the Generation UK Data Engineering bootcamp. This program is a simple coffee shop data management system. The progress of the project is divided into 5 weeks.

# Weekly requirements and application:
## Week 1 requirements:
Implement a simple main menu that prints, creates, updates and deletes a product. Products are stored in a simple list.

## Week 1 application:
The program creates a simple menu using a while loop with conditional statements for functionality, one of which is appending the product list, updating a product along with input validtion checking and deleting a product.

## Week 2 requirements:
The program should be able to create a product or order and add it to a list. View all products or orders and be able to update or delete a product or order. To store more information such as the customer's name, address and phone number, as well as the status of the order an order should be a dictionary. The user should be able to: 
- create a product or order and add it to a list
- view all products or orders
- STRETCH I want to be able to update or delete a product or order

## Week 2 application:
The second week contains the addition of other functionalities for a list of orders. Print orders, Create New order, Update Existing order status, Update Existing order, Delete order are all the new functionalities added. The Create New Order functionality is written in a function, which was a topic that was covered a few days prior to the update of the program in a Generation lesson.

## Week 3 requirements:
The program should be able to add a list of couriers. The program should be able to store our data into .txt files for data persistance. The user should be able to:
- create a product, courier, or order and add it to a list 
- view all products, couriers, or orders 
- update the status of an order 
- persist my data (products and couriers) 
- STRETCH update or delete a product, order, or courier 

## Week 3 applicaion:
This week, the program should have contained functionality for the couriers requirement. Print Courier List, Create New Courier, Update Existing Courier, Delete Courier. However these functionality along with data persistance were not added to the program this week but was left for the next, which will see a huge update.

## Week 4 requirements:
The program should use dictionaries for both product and courier and use `.csv` files rather than `.txt` to bring back our persistence functionality. The program should contain unit tests to prove that the application works correctly. The should be able to: 
- create a product, courier, or order dictionary and add it to a list
- view all products, couriers, or orders
- update the status of an order
- persist my data
- _STRETCH_ update or delete a product, order, or courier
- _BONUS_ list orders by status or courier

## Week 4 application:
This week, the code was refractored to contain functions as the program was getting larger and larger with the addition of new required and complex functionalites. Three separate files were created to contain the function for products, couriers, and orders. The program in this week also introduces data persistance with data being stored in CSV files in the data folder. Data is loaded into the program as lists of dictionaries and ecompasses all aspects of Python covered in lessons. The program however does not contain unit tests.

## Weel 5 requirements:
The application should be able to store couriers and products in a database. The user should be able to:
- create a product or courier and add it to a database table
- create an order and add the order dictionary to a list
- view all products, couriers, or orders
- update the status of an order
- persist my data
- _STRETCH_ update or delete a product, order, or courier
- _BONUS_ list orders by status or courier
- _BONUS_ track my product inventory
- _BONUS_ import/export my entities in CSV format

## Week 5 application:
The final week of the project replaces csv files with a database called coffee_shop and tables called products, couriers, and orders, each containing unique columns. The program was refracted to replace the code for reading and writing to a csv file. The new code connects to a database and then carries out functions like print, create, update and delete records using the pymysql Python library and mysql statements.

# Running the application:
There may be certain errors when reading and writing to files as the program and the files themselves are located in separate folders. They were separated to ensure proper division and to ensure the the miniproject folder is not cluttered.
In order to run the weekly application the .csv and the functionality (where the application needs them) files should be stored in the same folder as the main_app.

# Project reflections:
## How did the design go about meeting the project requirements?
The design of the application is kept as simple and logical as possible. Requirements and only the requirements were followed closely and then implemented.

## How did you guarentee the project requirements?
The application only contained the required functionalities and did not add anything more. This way the stakeholder requirements were met.

## If you had more time, what is the one thing that you would improve upon?
In the last part of the project covering databases, some extra functionality that should have been included to improve the application were not implemented. For example assigning a courier to an order. To implement this functionality, a join table would need to have been created in the database.

## What did you most enjoy implementing?
Reading to and from a csv file and then a database, which hugely improved the application and made it more useful.