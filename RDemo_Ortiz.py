# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 23:20:53 2023

@author: artur
"""

class RetailItem:
    def __init__(self, description, units_in_inventory, price):
        self.description = description
        self.units_in_inventory = units_in_inventory
        self.price = price

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_units_in_inventory(self):
        return self.units_in_inventory

    def set_units_in_inventory(self, units_in_inventory):
        self.units_in_inventory = units_in_inventory

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price


# Create three RetailItem objects
prod1 = RetailItem("Jacket", 12, 249.99)
prod2 = RetailItem("Designer Jeans", 30, 199.99)
prod3 = RetailItem("Shirt", 45, 49.99)

# Print the attributes of the objects
print("Product 1:")
print("Description:", prod1.get_description())
print("Units in Inventory:", prod1.get_units_in_inventory())
print("Price:", prod1.get_price())
print()

print("Product 2:")
print("Description:", prod2.get_description())
print("Units in Inventory:", prod2.get_units_in_inventory())
print("Price:", prod2.get_price())
print()

print("Product 3:")
print("Description:", prod3.get_description())
print("Units in Inventory:", prod3.get_units_in_inventory())
print("Price:", prod3.get_price())
print()
