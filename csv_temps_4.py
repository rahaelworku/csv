import matplotlib.pyplot as plt
import csv
from datetime import datetime

open_file= open("death_valley_2018_simple.csv","r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

print(type(header_row))

for index,column_header in enumerate(header_row):
    print(index, column_header)

highs = []
dates = []
lows = []

for row in csv_file:
    #going to try and do this block
    try:
        high=int(row[4])
        low=int(row[5])
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
    #if error will tell where (date) and will not go to else
    except ValueError:
        print(f"missing data for{current_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)


#print(highs[:10])

fig= plt.figure()

plt.plot(dates, highs, color='red', alpha=0.5)
plt.plot(dates,lows,color='blue',alpha=0.5 )

plt.fill_between(dates,highs,lows, facecolor='blue', alpha=0.1)

plt.title("daily high temps for death valley 2018", fontsize=16)
plt.xlabel("",fontsize=10)
plt.ylabel("temperature (F)", fontsize=12)
plt.tick_params(axis='both', which="major", labelsize=12)


#The call to fig.auto_xdate() draws the date labels
#diagnollay to prevent them from overlapping 
fig.autofmt_xdate()
plt.show()