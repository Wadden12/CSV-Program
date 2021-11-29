# FileName: Customer
# Harry's Top Fuel Company: Looking to switching from Paper to electronic system.
# Author: Mike Wadden
# Date: November 9th, 2021

def Customer():
    # Constants

    with open('Constant.txt', 'r') as f:
        COMPANY_NAME = f.readline()
    print()
    print(f"{COMPANY_NAME.center(75)}")
    print(f"{'Customer Menu':^75}")

    # Imports
    import Func
    import datetime
    import csv

    # Province Information
    P = {"Newfoundland Labrador: NL", "Prince Edward Island: PE", "Nova Scotia: NS", "New Brunswick: NB",
         "Quebec: QC", "Ontario: ON", "Manitoba: MB", "Saskatchewan: SK", "Alberta: AB",
         "British Columbia: BC", "Yukon: YT", "Northwest Territories: NT", "Nunavut: NU"}

    Province_List = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]

    while True: # Loop to Make Another Entry

        while True: # Loop To Validate Entry
            # Inputs and Validation'
            print()
            print("Enter Customer Information")
            print()

            while True:
                Phone_Number = input("    Enter 10 Digit Phone Number: ").strip().replace("-", "")
                Data = []

                with open('Customer.txt', 'r') as f:  # creates a list to be used to check for duplicate entries
                    Reader = csv.reader(f)
                    Header = next(Reader)
                    for row in Reader:
                        Data.append(row[7])

                if Phone_Number in Data:
                    print(f"Invalid Entry: This Phone Number: {Phone_Number} is already linked to a account")
                elif Phone_Number.isdigit() == False:
                    print("Invalid Entry!: Enter 10 Digit Phone Number no '-' needed")
                elif len(Phone_Number) != 10:
                    print("Invalid Entry!: Enter 10 Digit Phone Number no '-' needed")
                else:
                    Account_Number = f"{Phone_Number[3:10]}"
                    break

            while True:
                Cus_First_Name = input("    First Name: ").title().lstrip().rstrip()
                if Cus_First_Name == "":
                    print("First Name cannot be blank: Please Re-Enter")
                elif len(Cus_First_Name) >25:
                    print("Invalid First Name Length: Cannot be longer than 25 letters ")
                elif Func.Name_Validation(Cus_First_Name) == False:                              #Function to Validate Name Input
                    print("Invalid Name Entered: Please use letters between (a-z), (-) and (') ")
                else:
                    break

            while True:
                Cus_Last_Name = input("    Last Name: ").title().lstrip().rstrip()
                if Cus_Last_Name == "":
                    print("Last Name cannot be blank: Please Re-Enter")
                elif len(Cus_Last_Name) > 30:
                    print("Invalid Last Name Length: Cannot be longer than 30 letters ")
                elif Func.Name_Validation(Cus_Last_Name) == False:                               #Function to Validate Name Input
                    print("Invalid Name Entered: Please use letters between (a-z), (-) and (') ")
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

            while True:
                Cus_Email = input("   Customer Email: ").lstrip().rstrip()
                if Func.Check_Email(Cus_Email) == True:
                    break
                else:
                    print("Invalid Email Entry: Please Enter a Valid Email")

            print()
            print("Service Date Entries: Next Oil Delivery")
            print("Enter date if requested or leave blank to auto generate a service call in 30 days")
            print()

            while True:  # Date Validation Loop
                try:
                    Next_Date = input("    Enter Next Oil Delivery as (YYYY-MM-DD): ")
                    if Next_Date == "":     #gives the user the option to input nothing a generate a automatic service call
                        Next_Date = datetime.datetime.now() + datetime.timedelta(days=30)
                        Next_Date = Func.Business_Day(Next_Date)
                    else:
                        Next_Date = Func.Time_Change(Next_Date)
                except:
                    print("Invalid Date Entry. Re-Enter using (YYYY-MM-DD)")
                else:
                    if Next_Date < datetime.datetime.now():
                        print("Invalid Date: Cannot be a Past Date")
                    else:
                        # This is to make sure all services are within buisness Days not the weekend
                        Next_Date = Func.Business_Day(Next_Date)
                        break

            print()
            print("Service Date Entries: Next Furnace Inspection")
            print("Enter date if requested or leave blank to auto generate a inspection in one Year")
            print()

            while True:  # Date Validation Loop
                try:
                    Insp_Date = input("    Enter Next Furnace Inspection as (YYYY-MM-DD): ")
                    if Insp_Date == "":     # Gives the user the option to input nothing a generate a automatic service call
                        Insp_Date = datetime.datetime.now() + datetime.timedelta(weeks=52)
                        Insp_Date = Func.Business_Day(Insp_Date)
                    else:
                        Insp_Date = Func.Time_Change(Insp_Date)
                except:
                    print("Invalid Date Entry. Re-Enter using (YYYY-MM-DD)")
                else:
                    if Insp_Date < datetime.datetime.now():
                        print("Invalid Date: Cannot be a Past Date")
                    else:
                        # This is to make sure all services are within buisness Days not the weekend
                        Insp_Date = Func.Business_Day(Insp_Date)
                        break

            print()
            anykey = input("Press any key to display inputs")
            #Func.Clear()
            print()

            # Will read Customer Balance
            Customer_Balance = 0

            # Confirmation Output

            print(f"{'Confirmation of Customer Entry'}")
            print()
            print("Customer Details")
            print()
            print(f"Account Number: {Account_Number}")
            print(f"Name: {Cus_First_Name} {Cus_Last_Name}")
            print(f"Address: {Street_Address}")
            print(f"{City} {Province:2}, {Postal_Code}")
            print(f"Phone Number: {Func.Format_Phone(Phone_Number)}")
            print(f"Email: {Cus_Email}")
            print()
            print("Service Dates")
            print()
            print(f"Next Oil Delivery is {Next_Date.strftime('%A: %b %d, %Y')}")
            print(f"Next Furnace Inspection is {Insp_Date.strftime('%A: %b %d, %Y')}")
            print()
            print(f"Customer Balance: {Func.As_Dollars(Customer_Balance)} ")
            print()
            print("*"*25)


            # Getting the User To verify the Input Information
            while True:
                Data_Check = input("Is this Entry Correct (Y)-yes or (N)-No: ").upper()
                if Data_Check =="":
                    print("Invalid Entry: Input Cannot be Blank")
                elif Data_Check == "Y":
                    # Writing File to Customer.dat on confirmation of Correct Data
                    with open('Customer.txt', 'a') as f:
                        Func.Write(Account_Number, f)
                        Func.Write(Cus_First_Name, f)
                        Func.Write(Cus_Last_Name, f)
                        Func.Write(Street_Address, f)
                        Func.Write(City, f)
                        Func.Write(Province, f)
                        Func.Write(Postal_Code, f)
                        Func.Write(Phone_Number, f)
                        Func.Write(Cus_Email, f)
                        Func.Write(Next_Date, f)
                        Func.Write(Insp_Date, f)
                        Func.Write_Space(Customer_Balance, f)
                    print()
                    print("********************")
                    print("Customer Entry Saved")
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
