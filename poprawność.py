import re
date_pattern = r'\d{4}-\d{2}-\d{2}'
time_pattern = r'\d{2}:\d{2}'

#sprawdzanie poprawnego formatu czasu
def check_time(str_time, pattern=time_pattern):
    return re.match(pattern, str_time)

#sprawdzanie poprawnego formatu daty
def check_date(str_date, pattern=date_pattern):
    return re.match(pattern, str_date)



