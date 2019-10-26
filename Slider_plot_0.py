import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import datetime
import Backup_cost

# take user input for parameters needed
days = int(input("Days to visualize:"))
initial_work_rate = int(input("Initial work rate:"))
init_price_big = int(input("Initial price for a recovery try of full backups:"))
init_price_small = int(input("Initial price for a recovery try of incremental backups:"))


# setup backup dates arrays as diff from initial time point

backup_dates_big = []
for i in range(days):
    if i % 7 == 2:
        backup_dates_big.append(i)

backup_dates_small = []
for i in range(days):
    if i % 7 == 3 or i % 7 == 5:
        backup_dates_small.append(i)

backup_dates = backup_dates_big + backup_dates_small

# Dates int to dates datetime
dates_numbers = np.arange(0.0, days, 1)
dates_datetime = []
first_backup_date = '10/18/2019'
for i in dates_numbers:
    dates_datetime.append(datetime.datetime.strptime(first_backup_date, '%m/%d/%Y') + datetime.timedelta(days=i))


# y data functions for the two linear graphics
def y_data(single_try_big, single_try_small,  w_rate):
    new_counter = 0
    new_fail_big = 0
    new_fail_small = 0
    prices_high = dates_numbers.copy()
    for new_time_iterator in dates_numbers:
        for new_backup_date_iterator in backup_dates_big:
            if new_time_iterator == new_backup_date_iterator:
                new_fail_big += 1
        for new_backup_date_iterator in backup_dates_small:
            if new_time_iterator == new_backup_date_iterator:
                new_fail_small += 1
        prices_high[new_counter] = dates_numbers[new_counter] * w_rate + single_try_big * new_fail_big + single_try_small * new_fail_small
        new_counter += 1
    return prices_high


def y_data_1(w_rate):
    new_counter = 0
    prices_low = dates_numbers.copy()
    last_backup = 0
    for time_iterator in dates_numbers:
        for backup_date_iterator in backup_dates:
            if time_iterator == backup_date_iterator:
                last_backup = backup_date_iterator
        prices_low[new_counter] = (dates_numbers[new_counter] - last_backup) * w_rate
        new_counter += 1
    return prices_low


# backup dates to datetime
backup_dates_string = []
for i in backup_dates:
    datetime_iterator = datetime.datetime.strptime(first_backup_date, '%m/%d/%Y') + datetime.timedelta(days=i)
    backup_dates_string.append(datetime_iterator.strftime('%m/%d/%Y'))
backup_dates_string = backup_dates_string[::-1]
print(backup_dates_string)


# Generating random data
def data_random(point_generator, points_count):
    y_data_rand = []
    x_data_rand = []
    for n in range(points_count):
        point_generator.disaster_date += datetime.timedelta(days=n)
        point = point_generator.point()
        y_data_rand.append(point[1])
        x_data_rand.append(point[0])
    return [x_data_rand, y_data_rand]


disaster_date = backup_dates_string[-2]
a = Backup_cost.Backup_cost(initial_work_rate, init_price_small, disaster_date, backup_dates_string, 1/2)
random_data = data_random(a, 10)
print(random_data[0])
print(random_data[1])

# Plotting the data
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.15, bottom=0.5)

prices = y_data(init_price_big, init_price_small, initial_work_rate)
l, = plt.plot(dates_datetime, prices, lw=1.2)
plt.xlabel("Days from disaster to recovery")
plt.ylabel("Backup price")
plt.gcf().autofmt_xdate()

prices_1 = y_data_1(initial_work_rate)
k, = plt.plot(dates_datetime, prices_1, color='red', lw=1.2)

m = plt.scatter(random_data[0], random_data[1], color='green', lw=1.2)
ax.margins(x=0)


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
    l.set_ydata(y_data(price_big, price_small, work_rate))
    k.set_ydata(y_data_1(work_rate))


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
