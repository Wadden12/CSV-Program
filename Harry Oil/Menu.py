# FileName: Menu
# Harry's Top Fuel Company: Looking to switching from Paper to electronic system.
# Author: Mike Wadden
# Date: November 9th, 2021

# Imports
from Func import Clear
import Employee_Menu
import Customer_Menu
import Call_Menu
import AutoService
import Prod_Serv_Menu
# On Load Program's
# Automatic Service Program: Books service Calls
AutoService.Auto_Service()

#Constant

with open('Constant.txt', 'r') as f:
    COMPANY_NAME = f.readline()

while True:
    # Main Menu
    print()
    print(f"{COMPANY_NAME}")
    print(f"{'Main Menu':^20}")
    print()
    print("1. Customer Menu.")
    print("2. Employee Menu.")
    print("3. Product/Services Menu.")
    print("4. Call Menu")
    print("5. Account.")
    print("6. Blank.")
    print("7. Reports.")
    print("8. Quit.")
    print()

    try:
        Choice = int(input(" Enter choice 1-8: "))

    except:
        print("Invalid Entry Please Enter a Number Between (1-8)")
        #Clear()
    else:
        if Choice < 1 or Choice > 8:
            print("Invalid Entry Select a number Between 1-8")

        elif Choice == 1:  #Customer Menu Program
            #Clear()
            Customer_Menu.Customer_Menu()

        elif Choice == 2: #Employee
            #Clear()
            Employee_Menu.Employee_Menu()

        elif Choice == 3: #Products/Services
            Clear()
            Prod_Serv_Menu.Prod_Serv_Menu()

        elif Choice == 4: # Call Program
            Clear()
            Call_Menu.Call_Menu()


        elif Choice == 8:
            print()
            print("Closing Program")
            print()
            break


