import time
import csv
from datetime import datetime
data_time = time.strftime("%Y-%m-%d %X")

print(data_time)
print(time.strftime("%Y-%m-%d %X"))
print(type(data_time))

time_str = datetime.now().strftime("%Y-%m-%d %X")
print(time_str)
print(type(time_str))