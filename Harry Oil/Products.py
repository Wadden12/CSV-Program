# FileName: Products
# Harry's Top Fuel Company: Looking to switching from Paper to electronic system.
# Author: Mike Wadden
# Date: November 12th, 2021

def Products():
    """Products Module"""
    # Constants

    with open('Constant.txt', 'r') as f:
        COMPANY_NAME = f.readline()

    from random import randint
    import csv
    from Func import Write
    from Func import Write_Space
    from Func import As_Dollars
    from Func import Clear
    while True: # Another Entry Loop
        while True: # User Confirmation Loop

            # inputs and Validation
            while True:
                try:
                    print()
                    print("Enter 0 to Display Supplier Details")
                    print()
                    SupplierID = int(input("    Enter 4 Digit Supplier ID: "))
                    Data = []

                    # creates a list to be used to make sure the supplier id is set up
                    with open('Supplier.txt', 'r') as r:
                        Read = csv.reader(r)
                        Header = next(Read)
                        for Sup in Read:
                            Data.append(Sup[0])
                            if Sup[0] == str(SupplierID):  # Links to the Supplier ID to use as needed in this module
                                Supplier_Name = Sup[1]
                                print()
                                print(f"      Supplier Name: {Supplier_Name}")
                                print()
                except:
                    print("Invalid Entry: Please Enter 4 digit Supplier ID: Enter 0 to Display all ID's")
                else:
                    if SupplierID == 0:

                        # Displays Suppliers ID for Reference
                        with open('Supplier.txt', 'r') as f:
                            Reader = csv.DictReader(f)
                            for row in Reader:
                                print(row['SupplierID'], row['Supplier_Name'])

                    # Checking List to make sure the Supplier ID is set up
                    elif str(SupplierID) not in Data:
                        print()
                        print("Invalid Supplier ID:")
                    else:
                        break

            Random_ID = randint(100, 999)  # Creates part of the Product ID
            ProductID = str(SupplierID)[0:3] + str(Random_ID)
            # creates a list to be used to check for duplicate entries and picks another number

            # Checks for Duplicate Entries
            with open('Product.txt', 'r') as f:
                Reader = csv.reader(f)
                Header = next(Reader)
                for row in Reader:
                    while True:
                        if row[0] == ProductID: # Changes the Supplier ID if it already exists
                            ProductID = str(SupplierID)[0:3] + str(randint(100, 999))
                        else:
                            break
            while True:
                Prod_Or_Service = input("  Product or Service: Enter (P)-Product or (S)-Service: ").upper().strip()
                if Prod_Or_Service == "":
                    print("Invalid Entry: Cannot be Blank")
                elif Prod_Or_Service == "P":
                    Message = "Product"
                    # Input Inventory Control and update QOH
                    Qty_On_Hand = 0
                    break
                elif Prod_Or_Service == "S":
                    Message = "Service"
                    # No Inventory for Services
                    Qty_On_Hand = ""
                    break
                else:
                    print("Incorrect Value entered, Please Enter P or S")

            if Prod_Or_Service == "P":
                print()
                print(f" Enter The follow {Message} Details")
                print()
                print("Enter 0 if not applicable")
            elif Prod_Or_Service == "S":
                print()
                print(f" Enter {Message} Details")
                print()
                print("Enter 0 if not applicable")
                print()

            while True:
                Prod_Desc = input(f"{Message} Description: ")
                if Prod_Desc == "":
                    print("Invalid Entry Description cannot be Blank")
                elif len(Prod_Desc) > 25:
                    print("Invalid Entry: Product Description Cannot be more than 25 chars")
                else:
                    break

            while True:
                try:
                    Prod_Cost = float(input(f"{Message} Cost: $"))
                except:
                    print(f"Invalid Entry: Enter The {Message} Cost ")

                else:
                    break

            # Uses the Margin to Determine the Selling price. This could be set up as a constant if the User wanted
            while True:
                try:
                    Margin = int(input(f"{Message} Margin Percent: ie(Enter 2 for 2%)  "))
                except:
                    print(f"Invalid Entry: Input {Message} Margin Rate in Percent: ie(Enter 2 for 2%)")
                else:
                    if Margin < 0:
                        print("Invalid Entry: Margin Rate cannot be less than 0: ")
                    else:

                        break

            Sell_Price = Prod_Cost * (1 + (Margin/100))
            # Field to be filled in by the purchasing table
            Order_Point = 0
            Max_Level = 0

            print()
            anykey = input("Press any key to display inputs")
            #Func.Clear()
            print()

            #Output for User
            print()
            print(f"       {COMPANY_NAME}")
            print()
            print(f"----------{Message}------------")
            print(f" {Message} ID:  {ProductID}")
            print(f" {Message} Description ")
            print(f" {Prod_Desc}")
            print(f" {Message} Cost: {As_Dollars(Prod_Cost)}")
            print(f" {Message} Price: {As_Dollars(Sell_Price)}")
            print("----------Supplier-------------")
            print(f" Supplier ID:   {SupplierID}")
            print(f" Supplier Name: {Supplier_Name}")

            while True:
                print()
                Data_Check = input("Is this Entry Correct (Y)-yes or (N)-No: ").upper()

                if Data_Check == "":
                    print("Invalid Entry: Input Cannot be Blank")
                elif Data_Check == "Y":

                    # Writing File to Customer.dat on confirmation of Correct Data
                    with open('Product.txt', 'a') as f:
                        Write(ProductID, f)
                        Write(Prod_Or_Service, f)
                        Write(Prod_Desc, f)
                        Write(Prod_Cost, f)
                        Write(Sell_Price, f)
                        Write(SupplierID, f)
                        Write(Qty_On_Hand, f)
                        Write(Order_Point, f)
                        Write_Space(Max_Level, f)

                    print()
                    print("********************")
                    print("Product Entry Saved")
                    print("********************")
                    print()

                    break
                elif Data_Check == "N":
                    print()
                    break
                else:
                    print("Incorrect Value entered, Please Enter Y or N")

            if Data_Check == "Y":
                break
        # This code prompts the user if they want to make another entry
        while True:
            Continue = input("Do you want to make another Entry?  (Y) or (N) ").upper()
            if Continue == "Y":
                print()
                #Func.Clear()
                break
            elif Continue == "N":
                print()
                break
            else:
                print("Incorrect Value entered, Please Enter Y or N")

        if Continue == "N":
            print()
            #Func.Clear()
            break
    return
