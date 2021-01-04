# Function: Date String Formatter
def date_str_formatter(input_date_str, current_format, target_format):
    """
    Input:
        input_date_str: Input Date in string format e.g "01-Jan-2000"
        current_format: Corresponding date format i.e "%d-%b-%Y"
        target_format: Target date format e.g: "%d-%m-%Y"
    Output:
        01-01-2000 
    """
    import sys
    from datetime import datetime
    new_date_str = input_date_str
    try:
        input_date = datetime.strptime(input_date_str, current_format).date()
        new_date_str = input_date.strftime(target_format)
    except Exception as E:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(f"date_str_formatter Error: {E} at {exc_tb.tb_lineno}, Exception Type: {exc_type}")
    return new_date_str

print(date_str_formatter("2020-01-12", "%Y-%m-%d", "%d-%m-%Y"))


