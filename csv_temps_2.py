open_file= open("sitka_weather_07-2018_simple.csv")

header_row = next (CSV_file)

#print(type(header_row))

for index,column_header in enumerate(header_row):
    print(index, column)

high = []
low = []

for row in CSV_file:
    highs.append(int(row[5]))
    dates.append(row[2])

#print(highs[:10])

fig = plt.figure()

plt.plot(dates, highs, color='red')
plt.title("daily high temps, july 2018", fontsize=16)
plt.xlabel("",fontsize=12)
plt.ylabel("temperature (F)", fontsize=12)
plt.tick_params(axis='both', which="major", labelsize=12)

#The call to fig.auto_xdate() draws the date labels
#diagnollay to prevent them from overlapping 
fig.autofmt_xdate()
plt.show 