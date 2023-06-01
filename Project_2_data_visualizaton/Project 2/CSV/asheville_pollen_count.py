import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'CSV/ashville_pollen_count.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #GET DATA
    dates, weeds, grasses, trees = [], [], [], []
    for row in reader:
        current_date = (row[2])
        try:
            weed = float(row[3])
            grass = float(row[4])
            tree = float(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            weeds.append(weed)
            grasses.append(grass)
            trees.append(tree)

#PLOT Indexes
fig, ax = plt.subplots()
ax.plot(dates, weeds, c='red', alpha=0.5)
ax.plot(dates, grasses, c='blue', alpha=0.5)
ax.plot(dates, trees, c='green', alpha=0.5)

#FORMAT DATA
title = "Asheville Pollen Index - 2022"
plt.title(title, fontsize=20)
plt.text(6, 7, 'Tree Pollen = Green \n Weed Pollen = Red \n Grass Pollen = Blue', fontsize=12, bbox = dict(facecolor = 'gray', alpha = 0.3))
plt.xlabel('Date', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Pollen Index", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
