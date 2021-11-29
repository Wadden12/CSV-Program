# FileName: Function
# Harry's Top Fuel Company: Looking to switching from Paper to electronic system.
# Author: Mike Wadden
# Date: November 9th, 2021


def Name_Validation(Name):
    """ Function to Validate a Name for Input: Allowing Spaces, - and '"""
    for Char in Name:
        if ("A" <= Char <= "Z" or "a" <= Char <= "z" or Char == " "
                or Char == "-" or Char == "'"):
            continue
        else:
            return False
    return True


def Time_Change(Date):
    """Convert Date input (YYYY-MM_DD) into a datetime object"""
    from datetime import datetime
    Date = datetime.strptime(Date, "%Y-%m-%d")
    return Date


def Business_Day(Date):
    """Function to Work Within Business Days Only Mon-Fri"""
    from datetime import timedelta
    Weekday = Date.weekday()
    if Weekday == 5:
        Date += timedelta(days=2)
    elif Weekday == 6:
        Date += timedelta(days=1)
    return Date


def Format_Phone(Phone):
    """Function to Format a Phone Number into (999)-999 9999)"""
    Phone = str(Phone)
    return f"({Phone[0:3]}) {Phone[3:6]}-{Phone[6:10]}"


def As_Dollars(Number):
    """Format Dollars amounts to strings"""
    Number_Display = f"${Number:,.2f}"
    return Number_Display


def Write(Variable, f):
    """Function to Convert None Strings to Strings and Format to write to file with ,"""
    import datetime
    if isinstance(Variable, str) == False:
        if isinstance(Variable, datetime.datetime) == True:
            return f.write(f"{Variable.strftime('%Y-%m-%d')},")
        else:
            return f.write(f"{str(Variable)},")
    elif isinstance(Variable, str) == True:
        return f.write(f"{(Variable)},")


def Write_Space(Variable, f):
    """Function to Convert None Strings to Strings and Format to write to file with Space"""
    import datetime
    if isinstance(Variable, str) == False:
        if isinstance(Variable, datetime.datetime) == True:
            return f.write(f"{Variable.strftime('%Y-%m-%d')}\n")
        else:
            return f.write(f"{str(Variable)}\n")
    elif isinstance(Variable, str) == True:
        return f.write(f"{(Variable)}\n")


def Clear():
    """Function to Clear Terminal Output"""
    from os import system
    from sys import platform

    if platform == "linux" or platform == "linux2":  #Linux2
        return system('clear')
    elif platform == "darwin":  #OS X
        return system('clear')
    elif platform == "win32":     #Windows
        return system('cls')


def Check_Email(Email):
    """Validates a Email Input"""
    from re import fullmatch
    Check = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if fullmatch(Check, Email):
        return True
    else:
        return False


def Write_New(Variable, f):
    """Function to Convert None Strings to Strings and Format to write to file with ,"""
    import datetime
    if isinstance(Variable, str) == False:
        if isinstance(Variable, datetime.datetime) == True:
            return f.write(f"{Variable.strftime('%Y-%m-%d')}")
        else:
            return f.write(f"{str(Variable)}")
    elif isinstance(Variable, str) == True:
        return f.write(f"{(Variable)}")


def Number_Pad(Number):
    """Format Dollars amounts to strings & Pad Right 10 Spaces"""
    Number_Display = f"{Number:,}"
    Number_Display = f"{Number_Display:>5}"
    return Number_Display