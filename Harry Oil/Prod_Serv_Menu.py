# FileName: Prod_Serv_Menu
# Harry's Top Fuel Company: Looking to switching from Paper to electronic system.
# Author: Mike Wadden
# Date: November 11th, 2021


def Prod_Serv_Menu():
    """Product/Service Menu"""

    # Costants
    with open('Constant.txt', 'r') as f:
        COMPANY_NAME = f.readline()

    # Imports
    from Func import Clear
    import Products
    import Supplier

    while True:
        # Product/Services Menu
        print()
        print(f"{COMPANY_NAME}")
        print(f"{'Product/Services Menu':^20}")
        print()
        print("1. Add Product/Service.")
        print("2. Delete Product/Service.")
        print("4. Enter Service Request Sheet")
        print("5. Supplier.")
        print("6. Purchasing")
        print("7. Main Menu.")
        print()

        try:
            Choice = int(input(" Enter choice 1-7: "))
        except:
            print("Invalid Entry Please Enter a Number Between (1-7)")
        else:
            if Choice < 1 or Choice > 7:
                print("Invalid Entry Select a number Between 1-7")
            elif Choice == 1:  # Products
                #Clear()
                Products.Products()
            elif Choice == 5:  # Supplier
                #Clear()
                Supplier.Supplier()
            elif Choice == 7:
                #Clear()
                break
    return