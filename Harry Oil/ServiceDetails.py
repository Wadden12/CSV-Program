# FileName: ServiceDetails
# Harry's Top Fuel Company: Looking to switching from Paper to electronic system.
# Author: Mike Wadden
# Date: November 18th, 2021
ServiceID = 1
# imports
import csv
from Func import As_Dollars
from Func import Number_Pad
from Func import Write_New
from Func import Write
from Func import Write_Space

with open('Service_Details_Count.txt', 'r') as f:  # Service Details Tracker
    SD_Count = f.readline()
with open('Constant.txt', 'r') as f:
    COMPANY_NAME = f.readline()
Total = 0
Products = ""
Qty = ""
# Loop that Controls The Services and Product Inputs so it can repeat until broken
print()
print("Enter 0 to Display Service/Product Details")
print()
print("Enter END into Product ID when finished with Service/Product Details")

while True:

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



with open('Service_Details_Count.txt', 'w') as f:  # Service ID
    Write_New(SD_Count, f)



