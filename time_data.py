def time_data(tm, time_need=False):
    year = tm[-4:]
    month = tm[4:7]
    if month == "Jan":
        month = "01"
    elif month == "Feb":
        month = "02"
    elif month == "Mar":
        month = "03"
    elif month == "Apr":
        month = "04"
    elif month == "May":
        month = "05"
    elif month == "Jun":
        month = "06"
    elif month == "Jul":
        month = "07"
    elif month == "Aug":
        month = "08"
    elif month == "Sep":
        month = "09"
    elif month == "Oct":
        month = "10"
    elif month == "Nov":
        month = "11"
    elif month == "Dec":
        month = "12"
    date = tm[8:10].split(" ")[-1]
    if len(date) == 1:
        date = "0" + date

    if time_need == True:
        time_list = tm[11:19].split(":")
        my_time = time_list[0] + "-" + time_list[1] + "-" + time_list[2]
        dt = year + "-" + month + "-" + date + "-" + my_time
    else:
        dt = year + "-" + month + "-" + date
    return dt
