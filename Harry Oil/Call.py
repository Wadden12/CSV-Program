# FileName: Call
# Harry's Top Fuel Company: Looking to switching from Paper to electronic system.
# Author: Mike Wadden
# Date: November 9th, 2021

def Call():
    """ Call Module"""
    # imports
    import csv
    import Func
    import datetime
    import sys
    import Customer

    # Constants

    with open('Constant.txt', 'r') as f:
        COMPANY_NAME = f.readline()

    while True:
        with open('Call_ID.txt', 'r') as f:    #Call ID Tracker
            Call_Id = f.readline()

        while True:
            print()
            print(f"{COMPANY_NAME.center(75)}")
            print(f"{'Call Menu':^75}")

            while True:
                New_Customer = input("New or Existing Customer? (N)ew or (E)xisting: ").upper().strip()
                if New_Customer == "E":
                    break
                elif New_Customer == "N":
                    Customer.Customer()
                    break
                else:
                    print("Invalid Input: Please Enter (N) for New or (E) for Existing: ")

            while True:

                while True:

                    Account_Number = input("Customer Account Number: (7 Digit Phone Number): ").strip()
                    Data = []

                    with open('Customer.txt', 'r') as f:  # creates a list to be used to check for duplicate entries
                        Reader = csv.reader(f)
                        Header = next(Reader)
                        for row in Reader:
                            Data.append(row[0])

                    if Account_Number not in Data:
                        print(f"Invalid Entry:{Account_Number} is not a Valid Account Number")
                    elif Account_Number.isdigit() == False:
                        print("Invlaid Entry: Please Enter the Account Number: (7 Digit Phone Number")
                    elif Account_Number == "":
                        print("Invalid Entry: Account Number Cannot be Blank")
                    else:
                        with open('Customer.txt', 'r') as f:  # creates a list to be used to check for duplicate entries
                            Reader = csv.reader(f)
                            Header = next(Reader)
                            for Row in Reader:
                                if Row[0] == Account_Number:  # Searches for Account Number and Matches Customer Details
                                    print()
                                    print(f"Account Number: {Row[0]}")
                                    print(f"Customer Name: {Row[1]} {Row[2]}")
                                    print(f"Address: {Row[3]}")
                                    print(f"{Row[4]} {Row[5]}, {Row[6]}")
                                    print(f"Phone Number: {Func.Format_Phone(Row[7])}")
                                    print(f"Email: {Row[8]}")
                                    print()
                                    Customer_Name = Row[1] + " " + Row[2]  # Creating Variables for Call Forum Output
                                    Street_Address = Row[3]
                                    City = Row[4]
                                    Province = Row[5]
                                    Postal_Code = Row[6]
                                    Phone_Number = Func.Format_Phone(Row[7])
                        break
                while True:
                    Data_Check = input("Is this Customer Correct (Y)-yes or (N)-No: ").upper()
                    print()

                    if Data_Check == "":
                        print("Invalid Entry Customer Check Cannot Be Blank")
                    elif Data_Check == "Y":
                        break
                    elif Data_Check == "N":
                        print()
                        break
                    else:
                        print("Incorrect Value entered, Please Enter Y or N")
                if Data_Check == "Y":
                    break

            print("Servicing Options")
            print("Blank Entries will Default to No")
            print()

            while True:
                Message = ""
                Repair_Service = input("Repair Service:     (Y)es or (N)o: ").upper().strip()
                if Repair_Service == "" or Repair_Service == "N":
                    Repair_Service = "N"
                    break
                elif Repair_Service == "Y":
                    Message += "Repair Service" + "\n"
                    break
                else:
                    print("Invalid Entry: Please Enter Y-Yes or N-No")

            while True:
                Oil_Deliv = input("Oil_Delivery:       (Y)es or (N)o: ").upper().strip()
                if Oil_Deliv == "" or Oil_Deliv == "N":
                    Oil_Deliv = "N"
                    break
                elif Oil_Deliv == "Y":
                    Message += "Oil Delivery" + "\n"
                    break
                else:
                    print("Invalid Entry: Please Enter Y-Yes or N-No")

            while True:
                Furnace_Insp = input("Furnace Inspection: (Y)es or (N)o: ").upper().strip()
                if Furnace_Insp == "" or Furnace_Insp == "N":
                    Furnace_Insp = "N"
                    break
                elif Furnace_Insp == "Y":
                    Message += "Furnace Inspection" + "\n"
                    break
                else:
                    print("Invalid Entry: Please Enter Y-Yes or N-No")

            Call_Details = datetime.datetime.now()

            no_of_lines = 5
            Lines = ""

            print()
            print("Enter a brief description of problem/services")
            print()
            print("You can Enter Up to 5 Notes: Enter ^ to skip and Continue")
            print()

            for i in range(no_of_lines):  # Multi Line String Input with "^" as a break
                Lines += input(f"Note: {i + 1} ") + "\n"
                if "^" in Lines:
                    Lines = Lines.replace("^", "")
                    break
                elif len(Lines) > 500:
                    print("Maximum Character Input of 500 Reached")
                    break

            print()
            anykey = input("Press any key to display inputs")
            #Func.Clear()
            print()
            #Output for User Call Forum
            print()
            print(f"       {COMPANY_NAME}")
            print(f"        Call Forum ID: {Call_Id}")
            print()
            print(f"   Account Number  {Account_Number:>15}")
            print(f"   Customer Name:  {Customer_Name:>15}")
            print(f"   Phone Number:   {Phone_Number:>15}")
            print("-------------Address--------------")
            print(f"   {Street_Address}")
            print(f"   {City} {Province}, {Postal_Code}")
            print("-------------Call Info------------")
            print(f"      {Call_Details.ctime()}")
            print("----------------------------------")
            print("Service Request")
            print("**********************")
            print(f"{Message.strip()}")
            print("**********************")
            print("       Brief Notes of Problem/Services")
            print("-----------------------------------------------------")
            print(Lines.strip())
            print("-----------------------------------------------------")
            print()

        # Getting the User To verify the Input Information

            while True:
                Data_Check = input("Is this Entry Correct (Y)-yes or (N)-No: ").upper()
                if Data_Check == "":
                    print("Invalid Entry: Input Cannot be blank")
                elif Data_Check == "Y":

                    # Writing File to Customer.dat on confirmation of Correct Data
                    with open('Call.txt', 'a') as f:
                        Func.Write(Call_Id, f)
                        Func.Write(Account_Number, f)
                        Func.Write(Call_Details, f)
                        Func.Write(Repair_Service, f)
                        Func.Write(Oil_Deliv, f)
                        Func.Write(Furnace_Insp, f)
                        Data_Lines = Lines.replace("\n", "-")   # Formating the Multi String so it can be entered on the text file
                        Func.Write_Space(Data_Lines, f)

                    print()
                    print("********************")
                    print("Call Entry Saved")
                    print("********************")
                    print()

                    # Writing the Call Forum to a full display output
                    original_stdout = sys.stdout
                    with open('Call_Forum.txt', 'a') as f:
                        sys.stdout = f
                        print()
                        print(f"       {COMPANY_NAME}")
                        print(f"        Call Forum ID: {Call_Id}")
                        print()
                        print(f"   Account Number  {Account_Number:>15}")
                        print(f"   Customer Name:  {Customer_Name:>15}")
                        print(f"   Phone Number:   {Phone_Number:>15}")
                        print("-------------Address--------------")
                        print(f"   {Street_Address}")
                        print(f"   {City} {Province}, {Postal_Code}")
                        print("-------------Call Info------------")
                        print(f"      {Call_Details.ctime()}")
                        print("----------------------------------")
                        print("Service Request")
                        print("**********************")
                        print(f"{Message.strip()}")
                        print("**********************")
                        print("       Brief Notes of Problem/Services")
                        print("-----------------------------------------------------")
                        print(Lines.strip())
                        print("-----------------------------------------------------")
                        print()
                        sys.stdout = original_stdout

                    # Update Callid
                    Call_Id = int(Call_Id)
                    Call_Id += 1
                    with open('Call_ID.txt', 'w') as f:  # Call ID Tracker
                        Func.Write_New(Call_Id, f)
                        break
                elif Data_Check == "N":
                    print()
                    break
                else:
                    print("Incorrect Value entered, Please Enter Y or N")


            if Data_Check == "Y":
                break

        while True:
            Continue = input("Enter (Y) to make another entry or (N)  to return to Call Menu: ").upper()
            if Continue == "":
                print("Invalid Entry: Cannot be Blank")
            elif Continue == "Y":
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