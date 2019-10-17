import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

days = int(input("Number of days to visualize:"))

backup_dates_big = []
for i in range(days):
    if i % 7 == 2:
        backup_dates_big.append(i)

backup_dates_small = []
for i in range(days):
    if i % 7 == 3 or i % 7 == 5:
        backup_dates_small.append(i)

backup_dates = backup_dates_big + backup_dates_small

initial_work_rate = int(input("Initial work rate:"))
init_price_big = int(input("Initial price for a recovery try of full backups:"))
init_price_small = int(input("Initial price for a recovery try of incremental backups:"))

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)

dates = np.arange(0.0, days, 1)
counter = 0
fail_big = 0
fail_small = 0


def y_data(single_try_big, single_try_small,  w_rate):
    new_counter = 0
    new_fail_big = 0
    new_fail_small = 0
    prices_new = dates.copy()
    for new_time_iterator in dates:
        for new_backup_date_iterator in backup_dates_big:
            if new_time_iterator == new_backup_date_iterator:
                new_fail_big += 1
        for new_backup_date_iterator in backup_dates_small:
            if new_time_iterator == new_backup_date_iterator:
                new_fail_small += 1
        prices_new[new_counter] = dates[new_counter] * w_rate + single_try_big * new_fail_big + single_try_small * new_fail_small
        new_counter += 1
    return prices_new


def y_data_1(w_rate):
    new_counter = 0
    prices_new = dates.copy()
    last_backup = 0
    for time_iterator in dates:
        for backup_date_iterator in backup_dates:
            if time_iterator == backup_date_iterator:
                last_backup = backup_date_iterator
        prices_new[new_counter] = (dates[new_counter] - last_backup) * w_rate
        new_counter += 1
    return prices_new


prices_1 = y_data_1(initial_work_rate)

k, = plt.plot(dates, prices_1, color='red', lw=1.2)

prices = y_data(init_price_big, init_price_small, initial_work_rate)

l, = plt.plot(dates, prices, lw=1.2)
ax.margins(x=0)

ax_color = 'lightgoldenrodyellow'
ax_work_rate = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=ax_color)
ax_price_big = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor=ax_color)
ax_price_small = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=ax_color)
s_work_rate = Slider(ax_work_rate, 'Work Rate', 0.1, 300.0, valinit=initial_work_rate)
s_price_big = Slider(ax_price_big, 'Big backup price', 10, 120.0, valinit=init_price_big, valstep=2.5)
s_price_small = Slider(ax_price_small, 'Small backup price', 5, 130.0, valinit=init_price_small, valstep=2.5, slidermax=s_price_big)


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


def reset(event):
    s_work_rate.reset()
    s_price_big.reset()
    s_price_small.reset()


reset_ax = plt.axes([0.8, 0.01, 0.1, 0.04])
button = Button(reset_ax, 'Reset', color=ax_color, hovercolor='0.975')
button.on_clicked(reset)
plt.show()