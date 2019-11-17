import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import datetime
import Backup_cost
from matplotlib.dates import DateFormatter

# take user input for parameters needed
days = int(input("Days to visualize:"))
initial_work_rate = int(input("Initial work rate:"))
init_price_big = int(input("Initial price for a recovery try of full backups:"))
init_price_small = int(input("Initial price for a recovery try of incremental backups:"))
first_backup_date = '10/18/2019'


class Backup:
    def __init__(self, backup_date, backup_type):
        self.date = backup_date
        self.backup_type = backup_type


# setup backup dates arrays as diff from initial time point
backups_big = []
for i in range(days):
    if i % 7 == 2:
        date = datetime.datetime.strptime(first_backup_date, '%m/%d/%Y') + datetime.timedelta(days=i)
        backups_big.append(Backup(date, 'big'))

backups_small = []
for i in range(days):
    if i % 7 == 3 or i % 7 == 5:
        date = datetime.datetime.strptime(first_backup_date, '%m/%d/%Y') + datetime.timedelta(days=i)
        backups_small.append(Backup(date, 'small'))

backups = sorted(backups_big + backups_small, key=lambda backup: backup.date)
backups.reverse()

# Dates and backup dates int to datetime
dates_numbers = np.arange(0.0, days, 1)
dates_datetime = []
for i in dates_numbers:
    dates_datetime.append(datetime.datetime.strptime(first_backup_date, '%m/%d/%Y') + datetime.timedelta(days=i))


# y data functions for the two linear graphics
def y_data_high(single_try_big, single_try_small, w_rate):
    new_counter = 0
    new_fail_big = 0
    new_fail_small = 0
    prices_high = dates_numbers.copy()
    for new_time_iterator in dates_datetime:
        for new_backup_date_iterator in backups:
            if new_time_iterator == new_backup_date_iterator.date:
                if new_backup_date_iterator.backup_type == 'small':
                    new_fail_small += 1
                if new_backup_date_iterator.backup_type == 'big':
                    new_fail_big += 1
        prices_high[new_counter] = dates_numbers[new_counter] * w_rate + single_try_big * new_fail_big + single_try_small * new_fail_small
        new_counter += 1
    return prices_high


last_backup = datetime.datetime.strptime(first_backup_date, '%m/%d/%Y')


def y_data_low(w_rate):
    new_counter = 0
    prices_low = dates_numbers.copy()
    for time_iterator in dates_datetime:
        for backup_date_iterator in backups:
            if time_iterator == backup_date_iterator.date:
                global last_backup
                last_backup = backup_date_iterator.date
        if last_backup != 0:
            prices_low[new_counter] = (dates_datetime[new_counter] - last_backup).days * w_rate
        else:
            prices_low[new_counter] = dates_datetime[new_counter].day * w_rate
        new_counter += 1
    return prices_low


# backup dates to string
backup_dates_string = []
for i in backups:
    backup_dates_string.append(i.date.strftime('%m/%d/%Y'))
backup_dates_string = backup_dates_string[::-1]


# Generating random data
def data_random(point_generator, points_count):
    y_data_rand = []
    x_data_rand = []
    colors = []
    for n in range(points_count):
        point_generator.disaster_date += datetime.timedelta(days=1)
        for r in range(3):
            point = point_generator.point()
            x_data_rand.append(point[0])
            y_data_rand.append(point[1])
            colors.append(point[2])
    return [x_data_rand, y_data_rand, colors]


disaster_date = backups[-1].date.strftime('%m/%d/%Y')
a = Backup_cost.Backup_cost(initial_work_rate, init_price_small, init_price_big, disaster_date, backups, 4/5, 1/2)
random_data = data_random(a, days-4)

# Plotting the data
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.15, bottom=0.3)

prices = y_data_high(init_price_big, init_price_small, initial_work_rate)
l, = plt.plot(dates_datetime, prices, lw=1.2)
plt.xlabel("Disaster date")
plt.ylabel("Backup price")

prices_1 = y_data_low(initial_work_rate)
k, = plt.plot(dates_datetime, prices_1, color='red', lw=1.2)

m = plt.scatter(random_data[0], random_data[1], color=random_data[2], lw=1.2)
ax.margins(x=0)
date_form = DateFormatter("%m/%d")
ax.xaxis.set_major_formatter(date_form)


# Setting up the sliders
ax_color = 'lightgoldenrodyellow'
ax_work_rate = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=ax_color)
ax_price_big = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor=ax_color)
ax_price_small = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=ax_color)
s_work_rate = Slider(ax_work_rate, 'Work Rate', 0, 300.0, valinit=initial_work_rate)
s_price_big = Slider(ax_price_big, 'Big backup price', 0, 120.0, valinit=init_price_big, valstep=2)
s_price_small = Slider(ax_price_small, 'Small backup price', 0, 130.0, valinit=init_price_small, valstep=2, slidermax=s_price_big)


# The update function for the sliders
def update(val):
    price_big = s_price_big.val
    price_small = s_price_small.val
    work_rate = s_work_rate.val
    fig.canvas.draw_idle()
    l.set_ydata(y_data_high(price_big, price_small, work_rate))
    k.set_ydata(y_data_low(work_rate))


s_work_rate.on_changed(update)
s_price_big.on_changed(update)
s_price_small.on_changed(update)


# The reset function for the button
def reset(event):
    s_work_rate.reset()
    s_price_big.reset()
    s_price_small.reset()


reset_ax = plt.axes([0.8, 0.01, 0.1, 0.04])
button = Button(reset_ax, 'Reset', color=ax_color, hovercolor='0.975')
button.on_clicked(reset)

plt.show()
