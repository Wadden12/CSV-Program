# This function Automatically updates the Service Dates

def Auto_Service():
    """Automatic Service Updated"""
    import csv
    import datetime
    import Func

    Today = datetime.datetime.now().date()
    Data = []
    with open('Customer.txt', 'r') as f:
        Reader = csv.reader(f)
        Header = next(Reader)
        for row in Reader:
            Data.append(row)
        NewData = []
        for DateRow in Data:
            Date = datetime.datetime.strptime(DateRow[9].split(" ")[0], "%Y-%m-%d").date()
            if Today == Date:
                Date = datetime.datetime.now() + datetime.timedelta(days=30)
                Date = Func.Business_Day(Date)
                NewDateRow = DateRow.copy()
                NewDateRow[9] = str(Date).split(" ")[0]
                NewData.append(NewDateRow)
            else:
                NewData.append(DateRow.copy())
                continue
        Data = NewData

    with open('Customer.txt', 'w', newline="") as f:
        Writer = csv.writer(f)
        Writer.writerow(Header)
        Writer.writerows(Data)
    Data = []
    with open('Customer.txt', 'r') as f:
        Reader = csv.reader(f)
        Header = next(Reader)
        for row in Reader:
            Data.append(row)
        NewData = []
        for DateRow in Data:
            Date = datetime.datetime.strptime(DateRow[10].split(" ")[0], "%Y-%m-%d").date()
            if Today == Date:
                Date = datetime.datetime.now() + datetime.timedelta(weeks=52)
                Date = Func.Business_Day(Date)
                NewDateRow = DateRow.copy()
                NewDateRow[10] = str(Date).split(" ")[0]
                NewData.append(NewDateRow)
            else:
                NewData.append(DateRow.copy())
                continue
        Data = NewData

    with open('Customer.txt', 'w', newline="") as f:
        Writer = csv.writer(f)
        Writer.writerow(Header)
        Writer.writerows(Data)

    return
