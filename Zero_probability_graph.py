import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

# define variables and initial values

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
dates = np.arange(0.0, 60, 1)
initial_work_rate = 50
initial_single_try_price = 30
backup_dates = []
prices = dates.copy()
for i in range(60):
    if i % 7 == 2:
        backup_dates.append(i)

counter = 0
failed_backups = 0

for time_iterator in dates:
    for backup_date_iterator in backup_dates:
        if time_iterator == backup_date_iterator:
            failed_backups += 1
    prices[counter] = dates[counter]*initial_work_rate + initial_single_try_price*failed_backups
    counter += 1

l, = plt.plot(dates, prices, lw=1.2)
ax.margins(x=0)

ax_color = 'lightgoldenrodyellow'
ax_work_rate = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=ax_color)
ax_single_try_price = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor=ax_color)
s_work_rate = Slider(ax_work_rate, 'Work Rate', 0.1, 300.0, valinit=initial_work_rate)
s_single_try_price = Slider(ax_single_try_price, 'Backup price', 0.1, 250.0, valinit=initial_single_try_price)


def new_prices(single_try, w_rate):
    new_counter = 0
    new_failed_backups = 0
    prices_new = dates.copy()
    for new_time_iterator in dates:
        for new_backup_date_iterator in backup_dates:
            if new_time_iterator == new_backup_date_iterator:
                new_failed_backups += 1
        prices_new[new_counter] = dates[new_counter] * w_rate + single_try * new_failed_backups
        new_counter += 1
    return prices_new


def update(val):
    single_try_price = s_single_try_price.val
    work_rate = s_work_rate.val
    fig.canvas.draw_idle()
    l.set_ydata(new_prices(single_try_price, work_rate))


s_work_rate.on_changed(update)
s_single_try_price.on_changed(update)

reset_ax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(reset_ax, 'Reset', color=ax_color, hovercolor='0.975')


def reset(event):
    s_work_rate.reset()
    s_single_try_price.reset()


button.on_clicked(reset)

rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=ax_color)
radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)


def color_func(label):
    l.set_color(label)
    fig.canvas.draw_idle()


radio.on_clicked(color_func)

plt.show()
