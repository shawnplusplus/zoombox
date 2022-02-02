import datetime

current_date_and_time = datetime.datetime.now()
current_date_and_time_string = str(current_date_and_time)
extension = ".txt"

file_name =  current_date_and_time_string + extension
file = open(file_name, 'w')
file.close()