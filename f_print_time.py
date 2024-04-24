from datetime import datetime

def f_print_time():
    """current date string with time

    :return: current time format "%Y-%m-%d %H:%M:%S"
    """
    dt_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return dt_string
