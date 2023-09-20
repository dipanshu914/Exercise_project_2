import csv

import matplotlib.pyplot as plt

from datetime import datetime

filename = "sitka_weather_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # print(header_row)

    """ for index, column_header in enumerate(header_row):
        print(index, column_header) """

    dates, high_humidity, low_humidity = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[7])
            low = int(row[9])
        except ValueError:
            print(current_date, "data not found")
        else:
            dates.append(current_date)
            high_humidity.append(high)
            low_humidity.append(low)


# plot graph
fig = plt.figure(dpi=128, figsize=(10, 5))
plt.plot(dates, high_humidity, c="red", alpha=0.8)
plt.plot(dates, low_humidity, c="green", alpha=0.8)
plt.fill_between(dates, high_humidity, low_humidity, facecolor="blue", alpha=0.5)

# label a graph
plt.title("sitka high-low humidity - 2014")
plt.xlabel("", fontsize=14)
fig.autofmt_xdate()
plt.ylabel("Temperature in {f}", fontsize=14)
plt.tick_params(axis="both", which="major", labelsize="12")

plt.show()

