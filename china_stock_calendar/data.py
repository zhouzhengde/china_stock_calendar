import csv
import os
from pandas.tseries.holiday import Holiday

# parse holiday.csv
HOLIDAY_FILE = 'holiday.csv'
datafilepath = os.path.join(os.path.dirname(__file__), HOLIDAY_FILE)
reader = csv.reader(open(datafilepath, 'r'))

# take holiday info and set result set.
holiday_set = []
i = 0
for item in reader:
    dayStr = str(item[0])
    day = Holiday("Holiday_" + dayStr, year= int(dayStr[:4]), month= int(dayStr[4:6]), day= int(dayStr[6:]))
    holiday_set.insert(i, day)
    i += 1