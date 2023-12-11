# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 22:44:48 2023

@author: artur
"""

class Employee:
    def __init__(self, name, ID_number):
        self.name = name
        self.ID_number = ID_number

    def getName(self):
        return self.name

    def getID(self):
        return self.ID_number

    def setName(self, name):
        self.name = name

    def setID(self, ID_number):
        self.ID_number = ID_number


class ProductionWorker(Employee):
    def __init__(self, name, ID_number, shift_number, pay_rate):
        super().__init__(name, ID_number)
        self.shift_number = shift_number
        self.pay_rate = pay_rate

    def getShiftNumber(self):
        return self.shift_number

    def getPayRate(self):
        return self.pay_rate

    def setShiftNumber(self, shift_number):
        self.shift_number = shift_number

    def setPayRate(self, pay_rate):
        self.pay_rate = pay_rate
