import matplotlib.pyplot as plt
import csv

open_file= open("sitka_weather_07-2018_simple.csv")

header_row = next (csv_file)

#print(type(header_row))

for index,column_header in enumerate(header_row):
    print(index, column)

highs = []
dates = []
lows = []

for row in csv_file:
    highs.append(int(row[5]))
    dates.append(int(row[]))
    lows.append(int(row))


print(highs[:10])

plt.plot(dates, highs, color='red', alpha=0.5)
plt.plot(dates,lows,color='blue',alpha=0.5 )

plt.fill_between(dates,highs,lows, facecolor='blue', aplha=0.5)

plt.title("daily high temps, july 2018, fontsize=16")
plt.xlabel("",fontsize=16)
plt.ylabel("temperature (F)", fontsize=16)
plt.tick_params(axis='both', which="major", labelsize=16)


#The call to fig.auto_xdate() draws the date labels
#diagnollay to prevent them from overlapping 
fig.autofmt_xdate()
plt.show 