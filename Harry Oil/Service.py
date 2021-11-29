# FileName: Service
# Harry's Top Fuel Company: Looking to switching from Paper to electronic system.
# Author: Mike Wadden
# Date: November 12th, 2021

# imports
import csv
import datetime
from Func import Time_Change
from Func import As_Dollars
from Func import Number_Pad
from Func import Write_New
from Func import Write
from Func import Write_Space

with open('ServiceID.txt', 'r') as f:  # ServiceID Tracker
    ServiceID = f.readline()
with open('Constant.txt', 'r') as f:
    COMPANY_NAME = f.readline()

while True:

    Call_ID = input("Enter Service Request Sheet Number: ").strip()
    Data = []

    with open('Call.txt', 'r') as f:  # creates a list to be used to check for duplicate entries
        Reader = csv.reader(f)
        Header = next(Reader)
        for row in Reader:
            Data.append(row[0])

    if Call_ID not in Data:
        print(f"Invalid Entry:{Call_ID} is not a Valid Service Request ID")
    elif Call_ID.isdigit() == False:
        print("Invlaid Entry: Please Enter the Service Request Number")
    elif Call_ID == "":
        print("Invalid Entry: Account Number Cannot be Blank")
    else:
        # We use the Inputed Call ID to match with the account number
        with open('Call.txt', 'r') as f:
            Reader = csv.reader(f)
            Header = next(Reader)
            # Then use the Matched Account Number to look up all the Customer Details Automatically
            for Row in Reader:
                if Row[0] == Call_ID:
                    Account_Number = Row[1]
                    with open('Customer.txt', 'r') as r:
                        Read = csv.reader(r)
                        Header = next(Read)
                        for Acc in Read:
                            if Acc[0] == Account_Number:
                                # Creating Workable Variables from the sorted Customer info
                                First_Name = Acc[1]
                                Last_Name = Acc[2]
                                Street_Address = Acc[3]
                                City = Acc[4]
                                Province = Acc[5]
                                Postal_Code = Acc[6]
                                Phone_Number = Acc[7]
                                Email = Acc[8]
                                Next_Oil = Acc[9]
                                Next_Isp = Acc[10]
                                Customer_Balance = Acc[11]
        break

while True:  # Date Validation Loop
    try:
        Service_Date = input("Enter The Service Date as (YYYY-MM-DD): ")
        Service_Date = Time_Change(Service_Date)
    except:
        print("Invalid Date Entry. Re-Enter using (YYYY-MM-DD)")
    else:
        if Service_Date > datetime.datetime.now():
            print("Invalid Date: Cannot be a Future Date")
        else:
            break
Data = []
while True:

    print()
    print("Enter 0 to Display Technician Details")
    print()
    Tech_ID = input("Enter Tech ID (AA-1) ").upper()

    # creates a list to be used to make sure the supplier id is set up
    with open('Technician.txt', 'r') as r:
        Read = csv.reader(r)
        Header = next(Read)
        for Sup in Read:
            Data.append(Sup[0])
            if Sup[0] == str(Tech_ID):  # Links to the Supplier ID to use as needed in this module
                Tech_First = Sup[1]
                Tech_Last = Sup[2]
                print()
                print(f"      Technician Name: {Tech_First} {Tech_Last}")
                print()

    if Tech_ID == "0":
        # Displays Suppliers ID for Reference
        with open('Technician.txt', 'r') as f:
            Reader = csv.DictReader(f)
            for row in Reader:
                print(row['Tech_ID'], row['First_Name'], row['Last_Name'])

    # Checking List to make sure the Supplier ID is set up
    elif Tech_ID not in Data:
        print()
        print("Invalid Tech ID:")
    else:
        break

with open('Service_Details_Count.txt', 'r') as f:  # Service Details Tracker
    SD_Count = f.readline()

Total = 0
Products = ""
Qty = ""

# Loop that Controls The Services and Product Inputs so it can repeat until broken
print()
print("Enter 0 to Display Service/Product Details")
print()
print("Enter END into Product ID when finished with Service/Product Details")

while True:  # Loop to add in Products and Services

    Data = []
    with open('Product.txt', 'r') as r:
        Read = csv.reader(r)
        Header = next(Read)
        for Sup in Read:
            Data.append(Sup[0])

    print()
    ProductID = input("Enter Product ID: ").upper()

    if ProductID == "END":
        break
    elif ProductID == "0":
        # Displays Suppliers ID for Reference
        print()
        with open('Product.txt', 'r') as f:
            Reader = csv.DictReader(f)
            for row in Reader:
                print(row['ProductID'], row['Prod_Desc'])
            print("*************************************")
            print("END to Finish Adding Product/Services")
            print("*************************************")
        # Checking List to make sure the Supplier ID is set up
    elif ProductID not in Data:
        print()
        print("Invalid ProductID:")

    else:
        # creates a list to be used to make sure the supplier id is set up
        with open('Product.txt', 'r') as r:
            Read = csv.reader(r)
            Header = next(Read)

            for Sup in Read:
                Data.append(Sup[0])
                if Sup[0] == str(ProductID):  # Links to the ProductID to use as needed in this module
                    Prod_Or_Service = Sup[1]
                    Prod_Desc = Sup[2]
                    Sell_Price = float(Sup[4])
                    Qty_On_Hand = Sup[6]

                    # Sorts between Product and Services
                    if Prod_Or_Service == "P":
                        Message = "Product"
                        print(f"  {Message}: {Prod_Desc}, Cost: {As_Dollars(Sell_Price)}, Qty on Hand: {Qty_On_Hand}")
                        print()
                    elif Prod_Or_Service == "S":
                        Message = "Service"
                        print(f"  {Message}: {Prod_Desc}, Cost: {As_Dollars(Sell_Price)}")
                        print()

                    while True:  # Hanldes the Order Quantity Loop. Spilt between Service and Product. Dif Input Messages
                        try:
                            if Prod_Or_Service == "S":
                                if Sup[0] == "538768":  # code for Labour: Has unique input message.
                                    Order_Qty = int(input("Enter Labour in Hours: "))
                                else:
                                    Order_Qty = int(input("Enter 1 for the Service Completed: "))
                            if Prod_Or_Service == "P":
                                if Sup[0] == "538531":  # code for Oil: Has unique input Message
                                    Order_Qty = int(input("Number of Litres Delivered: "))
                                else:
                                    Order_Qty = int(input("Enter the Order Quantity : "))
                        except:
                            print("Invalid Entry: Order Qty Must be a number")
                        else:
                            if Order_Qty < 0:
                                print("Order Quantity Cannot be less than 0")
                            else:
                                Item_Total = Sell_Price * Order_Qty
                                Total += Item_Total
                                Prod_Dis = f"{Prod_Desc:25}"
                                Products += Prod_Dis + (" ") + Number_Pad(Order_Qty) + "\n"
                                print()
                                print("Service Details")
                                print()
                                print(f"{'Description':25} {'Order Qty'} ")
                                print("-" * 35)
                                print(f"{Products}")
                                print(f"Service Total: {As_Dollars(Total)}")
                                print()

                                # Writing File to Service_Details.txt
                                with open('Service_Details.txt', 'a') as f:
                                    Write(SD_Count, f)
                                    Write(ProductID, f)
                                    Write(Prod_Desc, f)
                                    Write(Sell_Price, f)
                                    Write(Order_Qty, f)
                                    Write(Total, f)
                                    Write_Space(ServiceID, f)

                                # Update Service Details ID
                                SD_Count = int(SD_Count)
                                SD_Count += 1

                                break

    Hst = Total * .15
    Invoice_Total = Total + Hst

    # Outputs

print(f"{COMPANY_NAME} Invoice")


ServiceID = int(ServiceID)
ServiceID += 1

with open('Service_Details_Count.txt', 'w') as f:  # Service ID
    Write_New(SD_Count, f)

with open('ServiceID.txt', 'w') as f:  # Service ID
    Write_New(ServiceID, f)