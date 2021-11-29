# FileName: Technician
# Harry's Top Fuel Company: Looking to switching from Paper to electronic system.
# Author: Mike Wadden
# Date: November 1th, 2021

def Technician():
    """Technician Module"""

    # Constants
    with open('Constant.txt', 'r') as f:
        COMPANY_NAME = f.readline()

    print()
    print(f"{COMPANY_NAME.center(75)}")
    print(f"{'Technician Menu':^75}")

    # Imports
    import Func
    import csv

    # Province Information
    P = {"Newfoundland Labrador: NL", "Prince Edward Island: PE", "Nova Scotia: NS", "New Brunswick: NB",
         "Quebec: QC", "Ontario: ON", "Manitoba: MB", "Saskatchewan: SK", "Alberta: AB",
         "British Columbia: BC", "Yukon: YT", "Northwest Territories: NT", "Nunavut: NU"}

    Province_List = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]

    while True:  # Loop to Make Another Entry

        while True:  # Loop To Validate Entry

            with open('Tech_ID.txt', 'r') as f:  # Tech ID Tracker
                Tech_Count = f.readline()

            # Inputs and Validation'
            print()
            print("Enter Technician Information")
            print()

            while True:
                Mobile_Number = input("    Enter 10 Digit Phone Number: ").strip().replace("-", "")
                Data = []

                with open('Technician.txt', 'r') as f:  # creates a list to be used to check for duplicate entries
                    Reader = csv.reader(f)
                    Header = next(Reader)
                    for row in Reader:
                        Data.append(row[7])

                if Mobile_Number in Data:
                    print(f"Invalid Entry: This Phone Number: {Mobile_Number} is already linked to a account")
                elif Mobile_Number.isdigit() == False:
                    print("Invalid Entry!: Enter 10 Digit Phone Number no '-' needed")
                elif len(Mobile_Number) != 10:
                    print("Invalid Entry!: Enter 10 Digit Phone Number no '-' needed")
                else:
                    break

            while True:
                Tec_First_Name = input("    First Name: ").title().lstrip().rstrip()
                if Tec_First_Name == "":
                    print("First Name cannot be blank: Please Re-Enter")
                elif len(Tec_First_Name) > 25:
                    print("Invalid First Name Length: Cannot be longer than 25 letters ")
                elif Func.Name_Validation(Tec_First_Name) == False:  # Function to Validate Name Input
                    print("Invalid Name Entered: Please use letters between (a-z), (-) and (') ")
                else:
                    break

            while True:
                Tec_Last_Name = input("    Last Name: ").title().lstrip().rstrip()
                if Tec_Last_Name == "":
                    print("Last Name cannot be blank: Please Re-Enter")
                elif len(Tec_Last_Name) > 30:
                    print("Invalid Last Name Length: Cannot be longer than 30 letters ")
                elif Func.Name_Validation(Tec_Last_Name) == False:  # Function to Validate Name Input
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
                      and Postal_Code[2].isalpha() == True and Postal_Code[3].isdigit() == True and Postal_Code[
                          4].isalpha()
                      and Postal_Code[5].isdigit() == True):
                    break
                else:
                    print("Invalid Postal Code: Please Re-Enter (A1A1A1)")

            while True:
                Tec_Email = input("   Technician Email: ").lstrip().rstrip()
                if Func.Check_Email(Tec_Email) == True:
                    break
                else:
                    print("Invalid Email Entry: Please Enter a Valid Email")

            Tech_Id = f"{Tec_First_Name[0]}{Tec_Last_Name[0]}-{Tech_Count}"

            print()
            anykey = input("Press any key to display inputs")
            # Func.Clear()
            print()

            # Confirmation Output

            print(f"{'Confirmation of Technician Entry'}")
            print()
            print("Technician Details")
            print()
            print(f"Technician ID: {Tech_Id}")
            print(f"Name: {Tec_First_Name} {Tec_Last_Name}")
            print(f"Address: {Street_Address}")
            print(f"{City} {Province:2}, {Postal_Code}")
            print(f"Mobile Number: {Func.Format_Phone(Mobile_Number)}")
            print(f"Email: {Tec_Email}")
            print("*" * 25)

            # Getting the User To verify the Input Information
            while True:
                Data_Check = input("Is this Entry Correct (Y)-yes or (N)-No: ").upper()

                if Data_Check == "":
                    print("Invalid Entry: Input Cannot be Blank")
                elif Data_Check == "Y":

                    # Writing File to Customer.dat on confirmation of Correct Data
                    with open('Technician.txt', 'a') as f:
                        Func.Write(Tech_Id, f)
                        Func.Write(Tec_First_Name, f)
                        Func.Write(Tec_Last_Name, f)
                        Func.Write(Street_Address, f)
                        Func.Write(City, f)
                        Func.Write(Province, f)
                        Func.Write(Postal_Code, f)
                        Func.Write(Mobile_Number, f)
                        Func.Write_Space(Tec_Email, f)

                    print()
                    print("********************")
                    print("Technician Entry Saved")
                    print("********************")
                    print()

                    # Update Techid
                    Tech_Count = int(Tech_Count)
                    Tech_Count += 1

                    with open('Tech_ID.txt', 'w') as f:  # Call ID Tracker
                        Func.Write_New(Tech_Count, f)
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



