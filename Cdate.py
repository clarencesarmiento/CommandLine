def month_today(month):                         # Getting Months
    if month == 1:
        month = "January"
    elif month == 2:
        month = "February"
    elif month == 3:
        month = "March"
    elif month == 4:
        month = "April"
    elif month == 5:
        month = "May"
    elif month == 6:
        month = "June"
    elif month == 7:
        month = "July"
    elif month == 8:
        month = "August"
    elif month == 9:
        month = "September"
    elif month == 10:
        month = "October"
    elif month == 11:
        month = "November"
    elif month == 12:
        month = "December"
    else:
        pass
    return month

def day_of_week(day):                           # Getting the day of the week
    if day == 0:
        day = "Monday"
    elif day == 1:
        day = "Tuesday"
    elif day == 2:
        day = "Wednesday"
    elif day == 3:
        day = "Thursday"
    elif day == 4:
        day = "Friday"
    elif day == 5:
        day = "Saturday"
    elif day == 6:
        day = "Sunday"
    else:
        pass
    return day