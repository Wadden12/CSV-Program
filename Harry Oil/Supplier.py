# FileName: Supplier
# Harry's Top Fuel Company: Looking to switching from Paper to electronic system.
# Author: Mike Wadden
# Date: November 11th, 2021

def Supplier():
    """Supplier Module"""
    # Constants

    with open('Constant.txt', 'r') as f:
        COMPANY_NAME = f.readline()

    from random import randint
    import csv
    from Func import Name_Validation
    from Func import Check_Email
    from Func import Write
    from Func import Write_Space

    # Province Information
    P = {"Newfoundland Labrador: NL", "Prince Edward Island: PE", "Nova Scotia: NS", "New Brunswick: NB",
             "Quebec: QC", "Ontario: ON", "Manitoba: MB", "Saskatchewan: SK", "Alberta: AB",
             "British Columbia: BC", "Yukon: YT", "Northwest Territories: NT", "Nunavut: NU"}

    Province_List = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]
    while True: #Loop To Make another Entry
        while True: #User Confirmation Loop

            SupplierID = randint(1000, 9000)  # Creates a Random Supplier ID
            # Checks for Duplicate Entries
            with open('Supplier.txt', 'r') as f:
                Reader = csv.reader(f)
                Header = next(Reader)
                for row in Reader:
                    while True:
                        if row[0] == str(SupplierID): #Changes the Supplier ID if it already exists
                            SupplierID = randint(1000, 9000)
                            SupplierID = str(SupplierID)
                        else:
                            break


            # User Inputs

            while True:
                Supplier_Name = input("    Supplier Name: ").lstrip().rstrip()
                if Supplier_Name == "":
                    print("Supplier_Name Input cannot be blank: ")
                elif len(Supplier_Name) > 30:
                    print("Invalid Entry Supplier_Name Length: Cannot be longer than 30 characters ")
                else:
                    break

            while True:
                Street_Address = input("    Street Address: ").lstrip().rstrip().title()
                if Street_Address == "":
                    print("Street Address Input cannot be blank: ")
                elif len(Street_Address) > 35:
                    print("Invalid Entry Street Address Length: Cannot be longer than 35 characters ")
                else:
                    break

            while True:
                City = input("    City: ").lstrip().rstrip()
                if City == "":
                    print("City Input cannot be blank: ")
                elif len(City) > 20:
                    print("Invalid Entry City Length: Cannot be longer than 20 characters ")
                else:
                    break

            while True:
                Province = input("    Enter two Digit Province Code: ").upper()
                if Province in Province_List:
                    break
                else:
                    print()
                    print("Invalid Entry: Please Enter two Digit Province Code: ")
                    print()
                    for Code in P:
                        print(Code)

            while True:
                Postal_Code = input("    Postal Code: ").upper().strip()
                if Postal_Code == "":
                    print("Postal Code Entry Cannot be Blank. Please Re-enter")
                elif (Postal_Code[0].isalpha() == True and Postal_Code[1].isdigit() == True and len(Postal_Code) == 6
                      and Postal_Code[2].isalpha() == True and Postal_Code[3].isdigit() == True and Postal_Code[4].isalpha()
                      and Postal_Code[5].isdigit() == True):
                    break
                else:
                    print("Invalid Postal Code: Please Re-Enter (A1A1A1)")

            print()
            print("Supplier Contact Person Details")
            print()

            while True:
                Sup_First_Name = input("    First Name: ").title().lstrip().rstrip()
                if Sup_First_Name == "":
                    print("First Name cannot be blank: Please Re-Enter")
                elif len(Sup_First_Name) > 25:
                    print("Invalid First Name Length: Cannot be longer than 25 letters ")
                elif Name_Validation(Sup_First_Name) == False:  # Function to Validate Name Input
                    print("Invalid Name Entered: Please use letters between (a-z), (-) and (') ")
                else:
                    break

            while True:
                Sup_Last_Name = input("    Last Name: ").title().lstrip().rstrip()
                if Sup_Last_Name == "":
                    print("Last Name cannot be blank: Please Re-Enter")
                elif len(Sup_Last_Name) > 30:
                    print("Invalid Last Name Length: Cannot be longer than 30 letters ")
                elif Name_Validation(Sup_Last_Name) == False:  # Function to Validate Name Input
                    print("Invalid Name Entered: Please use letters between (a-z), (-) and (') ")
                else:
                    break

            while True:
                Phone_Number = input("    Enter 10 Digit Phone Number: ").strip().replace("-", "")

                if Phone_Number.isdigit() == False:
                    print("Invalid Entry!: Enter 10 Digit Phone Number no '-' needed")
                elif len(Phone_Number) != 10:
                    print("Invalid Entry!: Enter 10 Digit Phone Number no '-' needed")
                else:
                    break

            while True:
                Sup_Email = input("    Email: ").lstrip().rstrip()
                if Check_Email(Sup_Email) == True:
                    break
                else:
                    print("Invalid Email Entry: Please Enter a Valid Email")

            # Information needed for Purchasing
            print()
            print(" Supplier Details")
            print()
            print("Enter 0 if not Applicable")
            print()

            while True:
                try:
                    Lead_Time = int(input("    Supplier Estimate lead time in days: "))
                except:
                    print("Invalid Entry: Input the lead time in days")
                else:
                    if Lead_Time < 0 :
                        print("Invalid Entry: Lead time cannot be less than 0: ")
                    else:

                        break

            while True:
                try:
                    Term_Day = int(input("    Supplier terms in days: "))
                except:
                    print("Invalid Entry: Input the terms in days")
                else:
                    if Term_Day < 0 :
                        print("Invalid Entry: Terms cannot be less than 0: ")
                    else:
                        break
            while True:
                try:
                    Term_Disc = int(input("    Enter Terms Discount in Percent: ie(Enter 2 for 2%)  "))
                except:
                    print("Invalid Entry: Enter Terms Discount in Percent: ie(Enter 2 for 2%)")
                else:
                    if Term_Disc < 0 :
                        print("Invalid Entry: Lead time cannot be less than 0: ")
                    else:
                        break
            while True:
                try:
                    Freight_Per = int(input("    Enter Freight Rate Percent: ie(Enter 2 for 2%)  "))
                except:
                    print("Invalid Entry: Enter Freight Rate in Percent: ie(Enter 2 for 2%)")
                else:
                    if Freight_Per < 0 :
                        print("Invalid Entry: Freight Rate cannot be less than 0: ")
                    else:
                        break

            print()
            anykey = input("Press any key to display inputs")
            #Func.Clear()
            print()

            #Output for User
            print()
            print(f"       {COMPANY_NAME}")
            print()
            print("----------Supplier-------------")
            print(f" Supplier ID:   {SupplierID}")
            print(f" Supplier Name: {Supplier_Name}")
            print("----------Contact Person-------")
            print(f" Name:  {Sup_First_Name} {Sup_Last_Name}")
            print(f" Phone: {Phone_Number}")
            print(f" Email: {Sup_Email}")
            print("----------Address--------------")
            print(f" {Street_Address}")
            print(f" {City} {Province}, {Postal_Code}")
            print("----------Supplier Details------")
            print(f" Terms {Term_Disc}% net {Term_Day} days")
            print(f" Lead time: {Lead_Time:2} days")
            print(f" Freight Charge: {Freight_Per:2}%")
            print("---------------------------------")

            while True:
                Data_Check = input("Is this Entry Correct (Y)-yes or (N)-No: ").upper()

                if Data_Check == "":
                    print("Invalid Entry: Input Cannot be Blank")
                elif Data_Check == "Y":

                    # Writing File to Customer.dat on confirmation of Correct Data
                    with open('Supplier.txt', 'a') as f:
                        Write(SupplierID, f)
                        Write(Supplier_Name, f)
                        Write(Sup_First_Name, f)
                        Write(Sup_Last_Name, f)
                        Write(Phone_Number,f )
                        Write(Sup_Email,f)
                        Write(Street_Address, f)
                        Write(City, f)
                        Write(Province, f)
                        Write(Postal_Code, f)
                        Write(Term_Disc, f)
                        Write(Term_Day, f)
                        Write(Lead_Time, f)
                        Write_Space(Freight_Per, f)

                    print()
                    print("********************")
                    print("Supplier Entry Saved")
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
                # Func.Clear()
                break
            elif Continue == "N":
                print()
                break
            else:
                print("Incorrect Value entered, Please Enter Y or N")

        if Continue == "N":
            print()
            # Func.Clear()
            break
    return

