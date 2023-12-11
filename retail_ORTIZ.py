# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 21:09:46 2023

@author: artur
"""

class RetailItem:
    def __init__(self, description, units_in_inventory, price):
        self._description = description
        self._units_in_inventory = units_in_inventory
        self._price = price

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_units_in_inventory(self):
        return self._units_in_inventory

    def set_units_in_inventory(self, units_in_inventory):
        self._units_in_inventory = units_in_inventory

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price
        