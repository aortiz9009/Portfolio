# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 22:46:52 2023

@author: artur
"""

import empOrtiz

class Main:
   
    def main(args):
        print("Enter your name:", end="")
        name = input()
        print("Enter your ID number:", end="")
        ID = input()
        print("Enter the shift number:", end="")
        S_num = input()
        print("Enter your hourly rate:", end="")
        pay = input()

        p = empOrtiz.ProductionWorker(name, ID, S_num, pay)

        print("Production Worker Information:")
        print("Name: " + p.getName())
        print("ID number: " + str(p.getID()))
        print("Shift: " + str(p.getShiftNumber()))
        x = "{0:.2f}".format(float(p.getPayRate()))
        print("Hourly Pay Rate: $" + str(x))

if __name__ == "__main__":
    Main.main([])

