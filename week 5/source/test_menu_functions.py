import unittest
from main_app import clear_screen, products_options, order_options, courier_options, main_menu
from ProductOptionsFunctions import print_products, add_new_product, update_existing_product, delete_product
from OrderOptionsFunctions import print_orders, create_new_order, update_existing_order_status, update_existing_order, delete_order
from CourierOptionsFunctions import print_couriers, create_new_courier, update_existing_courier, delete_courier