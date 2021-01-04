def get_datetime_before_given_minutes(minutes):
    """
        returns datetime object of datetime given minutes before current one.
    """
    from datetime import datetime
    import datetime as dt
    date_obj_before_3min = datetime.now()- dt.timedelta(minutes=minutes)
    return date_obj_before_3min


def date_range_validator(input_date_str, from_date_str, to_date_str, pattern="%d-%m-%Y"):
    """
        This functions checks whether input date string is between input start date string and to end date string
    """
    import sys
    from datetime import datetime
    try:
        input_date = datetime.strptime(input_date_str, pattern).date()
        from_date = datetime.strptime(from_date_str, pattern).date()
        to_date = datetime.strptime(to_date_str, pattern).date()
        if from_date <= input_date and input_date <= to_date:
            return True
        else:
            return False
    except Exception as E:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(f"date_range_validator Error: {E} at {exc_tb.tb_lineno}, Exception Type: {exc_type}")
        return False

print(date_range_validator("01-01-2020", "01-01-2019", "01-01-2021", pattern="%d-%m-%Y"))
