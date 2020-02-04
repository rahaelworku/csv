import matplotlib.pyplot as plt
import csv
from datetime import datetime


open_file1= open("p:\\CSV_Project\\matplotlib_csv\\death_valley_2018_simple.csv","r")
open_file2= open("p:\\CSV_Project\\matplotlib_csv\\sitka_weather_2018_simple.csv","r")

csv_file1 = csv.reader(open_file1, delimiter=",")
csv_file2=csv.reader(open_file2, delimiter=",")

header_row1 = next(csv_file1)
header_row2= next(csv_file2)

for highindex1,column_header1 in enumerate(header_row1):
    if column_header1 == "TMAX":
        print(highindex1)
        break;

for lowindex1,column_header1 in enumerate(header_row1):
    if column_header1 == "TMIN":
        print(lowindex1)
        break;

for index,title1 in enumerate(header_row1):
    if column_header1 == "NAME":
        print(title1)
        break;

for highindex2,column_header2 in enumerate(header_row2):
    if column_header2 == "TMAX":
        print(highindex1)
        break;

for lowindex2,column_header2 in enumerate(header_row2):
    if column_header2 == "TMIN":
        print(lowindex2)
        break;

highs1 = []
dates1 = []
lows1 = []
dates1 = []

highs2 = []
dates2 = []
lows2 = []
dates2 = []

for row1 in csv_file1:
    #going to try and do this block
    try:
        high1=int(row1[highindex1])
        low1=int(row1[lowindex1])
        current_date1 = datetime.strptime(row1[2], '%Y-%m-%d')
    #if error will tell where (date) and will not go to else
    except ValueError:
        print(f"missing data for{current_date1}")
    else:
        highs1.append(high1)
        lows1.append(low1)
        dates1.append(current_date1)

for row2 in csv_file2:
    #going to try and do this block
    try:
        high2=int(row2[highindex2])
        low2=int(row2[lowindex2])
        current_date2 = datetime.strptime(row2[2], '%Y-%m-%d')
    #if error will tell where (date) and will not go to else
    except ValueError:
        print(f"missing data for{current_date1}")
    else:
        highs2.append(high2)
        lows2.append(low2)
        dates2.append(current_date2)







fig, (ax1,ax2) = plt.subplots(2)

ax2.plot(dates1, highs1, color='red', alpha=0.5)
ax2.plot(dates1,lows1,color='blue',alpha=0.5 )
ax1.title.set_text(title1)

ax1.plot(dates2, highs2, color='red', alpha=0.5)
ax1.plot(dates2,lows2,color='blue',alpha=0.5 )

ax1.fill_between(dates2,highs2,lows2, facecolor='blue', alpha=0.1)
ax2.fill_between(dates1,highs1,lows1, facecolor='blue', alpha=0.1)


plt.show()