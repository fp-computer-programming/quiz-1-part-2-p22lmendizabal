# author: LM (AMDG) 10/ 19/21
year = int(input("Enter the year of the date. "))
month = int(input("Enter the month of the date January = 1 and December = 12. "))
day_of_the_month = int(input("Enter the day of the month of the date. "))

century = (year // 100)
year_of_century = (year % 100)

if month == 1:
    month = 13
else:
    if month == 2:
        month = 14

day_of_the_week = (day_of_the_month + (26 * (month + 1) // 10) + year_of_century + (year_of_century // 4) + (century // 4) + (5 * century)) % 7 
if day_of_the_week == 0:
    print(str(month) + "/" + str(day_of_the_month) + "/" + str(year) + " was a Saturday.")
elif day_of_the_week == 1:
    print(str(month) + "/" + str(day_of_the_month) + "/" + str(year) + " was a Sunday.")
elif day_of_the_week == 2:
    print(str(month) + "/" + str(day_of_the_month) + "/" + str(year) + " was a Monday.")
elif day_of_the_week == 3:
    print(str(month) + "/" + str(day_of_the_month) + "/" + str(year) + " was a Tuesday.")
elif day_of_the_week == 4:
    print(str(month) + "/" + str(day_of_the_month) + "/" + str(year) + " was a Wednesday.")
elif day_of_the_week == 5:
    print(str(month) + "/" + str(day_of_the_month) + "/" + str(year) + " was a Thursday.")
elif day_of_the_week == 6:
    print(str(month) + "/" + str(day_of_the_month) + "/" + str(year) + " was a Friday.")
else:
    print("Data not available. ")
