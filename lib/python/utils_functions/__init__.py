def correct_date(date_column):

    dates_list = date_column.to_list()
    new_dates_list = []

    for date in dates_list:
        if date > 2021:
            new_date = 2021
        elif date < 2014:
            new_date = 2014
        else:
            new_date = date

        new_dates_list.append(new_date)

    return new_dates_list