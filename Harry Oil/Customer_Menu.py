# FileName: Customer Menu
# Harry's Top Fuel Company: Looking to switching from Paper to electronic system.
# Author: Mike Wadden
# Date: November 11th, 2021

def Customer_Menu():
    # Constant
    with open('Constant.txt', 'r') as f:
        COMPANY_NAME = f.readline()

    # Imports
    from Func import Clear
    import Customer

    while True:
        # Customer Menu
        print()
        print(f"{COMPANY_NAME}")
        print(f"{'Customer Menu':^20}")
        print()
        print("1. Add Customer.")
        print("2. Delete Customer.")
        print("3. Main Menu.")
        print()
        try:
            Choice = int(input(" Enter choice 1-3: "))
        except:
            print("Invalid Entry Please Enter a Number Between (1-3)")
        else:
            if Choice < 1 or Choice > 3:
                print("Invalid Entry Select a number Between 1-3")
            elif Choice == 1:  # Execute Customer Program
                #Clear()
                Customer.Customer()
            elif Choice == 3:
                #Clear()
                break
    return
