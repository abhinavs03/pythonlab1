months = {
    "January": 31,
    "February": 28, 
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

def leap_yr(yr):
    if (yr % 4 == 0 and yr % 100 != 0) or (yr % 400 == 0):
        return True
    return False

month_name = input("Enter the month name: ")

if month_name == "February":
    yr = int(input("Enter the year: "))
    if leap_yr(yr):
        days = 29
    else:
        days = 28
else:
    days = months.get(month_name, "Invalid month....")

if days != "Invalid month....":
    print("The number of days in", month_name," is:",days)
else:
    print(days)


'''
Enter the month name: July
The number of days in July  is: 31
'''
