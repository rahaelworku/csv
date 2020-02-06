import matplotlib.pyplot as plt
import csv
from datetime import datetime


open_file1= open("p:\\CSV_Project\\matplotlib_csv\\death_valley_2018_simple.csv","r")
open_file2= open("p:\\CSV_Project\\matplotlib_csv\\sitka_weather_2018_simple.csv","r")

csv_death_valley = csv.reader(open_file1, delimiter=",")
csv_sitka=csv.reader(open_file2, delimiter=",")

#get first row of each file
header_row_death_valley = next(csv_death_valley)
header_row_sitka= next(csv_sitka)

#get index of where TMAX is in the header row of the death valley csv
for highindex1,column_header1 in enumerate(header_row_death_valley):
    if column_header1 == "TMAX":
        print(highindex1)
        break;
#get index of where TMIN is in the header row of the death valley csv
for lowindex1,column_header1 in enumerate(header_row_death_valley):
    if column_header1 == "TMIN":
        print(lowindex1)
        break;

#get index of where NAME is in the header row of the death valley csv for the title
for title_index_1, column_header1 in enumerate(header_row_death_valley):
    if column_header1 == "NAME":
        print(title_index_1)
        break;

#get index of where TMAX is in the header row of sitka csv
for highindex2,column_header2 in enumerate(header_row_sitka):
    if column_header2 == "TMAX":
        print(highindex1)
        break;

#get index of where TMIN is in the header row of sitka csv
for lowindex2,column_header2 in enumerate(header_row_sitka):
    if column_header2 == "TMIN":
        print(lowindex2)
        break;

#get index of where NAME is in the header row of sitka csv for title
for title_index_2, column_header2 in enumerate(header_row_sitka):
    if column_header2 == "NAME":
        print(title_index_2)
        break;

#create empty lists for each variable we need to find 
highs_death_valley = []
dates_death_valley = []
lows_death_valley = []
name_death_valley = []

highs_sitka = []
dates_sitka = []
lows_sitka = []
name_sitka=[]

#for each row in csv
for row1 in csv_death_valley:
    #try to get the high, low, date, and tite from the particular indexes 
    try:
        high1=int(row1[highindex1])
        low1=int(row1[lowindex1])
        current_date1 = datetime.strptime(row1[2], '%Y-%m-%d')
        title_1=str(row1[title_index_1])
    
    #exept if there is any missing values 
    except ValueError:
        print(f"missing data for{current_date1}")

    #else append each value (high, low, etc.) to their appropriate lists 
    else:
        highs_death_valley.append(high1)
        lows_death_valley.append(low1)
        dates_death_valley.append(current_date1)
        name_death_valley.append(title_1)


for row2 in csv_sitka: 
    try:
        high2=int(row2[highindex2])
        low2=int(row2[lowindex2])
        current_date2 = datetime.strptime(row2[2], '%Y-%m-%d')
        title_2=str(row2[title_index_2])
    except ValueError:
        print(f"missing data for{current_date1}")
    else:
        highs_sitka.append(high2)
        lows_sitka.append(low2)
        dates_sitka.append(current_date2)
        name_sitka.append(title_2)



#create subplots 
fig, (sitka, death_valley) = plt.subplots(2)
#main title
fig.suptitle('Temperature comparison between '+name_death_valley[0]+' and '+name_sitka[0] )
#spacing between plots
fig.subplots_adjust(hspace=0.4)

death_valley.title.set_text(name_death_valley[0])
death_valley.plot(dates_death_valley, highs_death_valley, color='red', alpha=0.5)
death_valley.plot(dates_death_valley,lows_death_valley,color='blue',alpha=0.5 )
death_valley.fill_between(dates_death_valley,highs_death_valley,lows_death_valley, facecolor='blue', alpha=0.1)

sitka.title.set_text(name_sitka[0])
sitka.plot(dates_sitka, highs_sitka, color='red', alpha=0.5)
sitka.plot(dates_sitka,lows_sitka,color='blue',alpha=0.5 )
sitka.set_xticklabels([])
sitka.fill_between(dates_sitka,highs_sitka,lows_sitka, facecolor='blue', alpha=0.1)

plt.show()