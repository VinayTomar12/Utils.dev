def get_datetime_before_given_minutes(minutes):
    """
        returns datetime object of datetime given minutes before current one.
    """
    from datetime import datetime
    import datetime as dt
    date_obj_before_3min = datetime.now()- dt.timedelta(minutes=minutes)
    return date_obj_before_3min
