import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button


class Visualisation:

    def __init__(self, probability, big_dates, small_dates):
        self.probability = probability
        self.big_dates = big_dates
        self.small_dates = small_dates
        self.days = int(input("Number of days to visualize: "))
        self.x_data = np.arange(0.0, self.days, 1)

        self.initial_work_rate = int(input("Initial work rate: "))
        self.init_price_big = int(input("Initial price for a recovery try of full backups: "))
        self.init_price_small = int(input("Initial price for a recovery try of incremental backups: "))

        self.ax_color = 'lightgoldenrodyellow'
        self.s_work_rate = Slider
        self.s_price_big = Slider
        self.s_price_small = Slider

    def y_data(self, price_big, price_small, work_r):
        fail_big = 0
        fail_small = 0
        counter = 0
        prices = self.x_data.copy()
        for time_iterator in self.x_data:
            for date_iterator in self.big_dates:
                if time_iterator == date_iterator:
                    fail_big += 1
            for date_iterator in self.small_dates:
                if time_iterator == date_iterator:
                    fail_small += 1
            prices[counter] = self.x_data[counter] * work_r + price_big * fail_big + price_small * fail_small
            counter += 1
        return prices

    def slider_setup(self):
        ax_work_rate = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=self.ax_color)
        ax_price_big = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor=self.ax_color)
        ax_price_small = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=self.ax_color)
        self.s_work_rate = Slider(ax_work_rate, 'Work Rate', 0.1, 300.0, valinit=self.initial_work_rate)
        self.s_price_big = Slider(ax_price_big, 'Big backup price', 0.1, 250.0, valinit=self.init_price_big)
        self.s_price_small = Slider(ax_price_small, 'Small backup price', 0.1, 250.0, valinit=self.init_price_small)

    def button_setup(self):
        reset_ax = plt.axes([0.8, 0.01, 0.1, 0.04])
        button = Button(reset_ax, 'Reset', color=self.ax_color, hovercolor='0.975')
        return button

    def defining_plots(self):
        fig, ax = plt.subplots()
        plt.subplots_adjust(left=0.25, bottom=0.25)
        l, = plt.plot(self.x_data, self.y_data(self.init_price_big, self.init_price_small, self.initial_work_rate),
                      lw=1.2)
        ax.margins(x=0)
        return [fig, l]

    def actual_plot(self):
        self.defining_plots()
        self.s_work_rate.on_changed(self.update)
        self.s_price_big.on_changed(self.update)
        self.s_price_small.on_changed(self.update)
        self.button_setup()
        button = self.button_setup()
        button.on_clicked(self.reset)
        plt.show()

    def reset(self, event):
        self.s_work_rate.reset()
        self.s_price_big.reset()
        self.s_price_small.reset()
        self.button_setup.on_clicked(self.reset)

    def update(self, val):
        plots = self.defining_plots()
        work_rate = self.s_work_rate.val
        price_big = self.s_price_big.val
        price_small = self.s_price_small.val
        plots[0].canvas.draw_idle()
        plots[1].set_ydata(self.y_data(price_big, price_small, work_rate))


# initial_work_rate = int(input("Initial work rate:"))
# init_price_big = int(input("Initial price for a recovery try of full backups:"))
# init_price_small = int(input("Initial price for a recovery try of incremental backups:"))
# days = int(input("Number of days to visualize:"))
#
# fig, ax = plt.subplots()
# plt.subplots_adjust(left=0.25, bottom=0.25)
#
# dates = np.arange(0.0, days, 1)
# prices = dates.copy()

backup_dates_big = []
for i in range(60):
    if i % 7 == 2:
        backup_dates_big.append(i)

backup_dates_small = []
for i in range(60):
    if i % 7 == 3 or i % 7 == 5:
        backup_dates_small.append(i)


vis = Visualisation(1, backup_dates_big, backup_dates_small)

vis.actual_plot()
#
# counter = 0
# fail_big = 0
# fail_small = 0
#
# for time_iterator in dates:
#     for backup_date_iterator in backup_dates_big:
#         if time_iterator == backup_date_iterator:
#             fail_big += 1
#     for backup_date_iterator in backup_dates_small:
#         if time_iterator == backup_date_iterator:
#             fail_small += 1
#     prices[counter] = dates[counter] * initial_work_rate + init_price_big * fail_big + init_price_small * fail_small
#     counter += 1
#
# l, = plt.plot(dates, prices, lw=1.2)
# ax.margins(x=0)
#
# ax_color = 'lightgoldenrodyellow'
# ax_work_rate = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=ax_color)
# ax_price_big = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor=ax_color)
# ax_price_small = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=ax_color)
# s_work_rate = Slider(ax_work_rate, 'Work Rate', 0.1, 300.0, valinit=initial_work_rate)
# s_price_big = Slider(ax_price_big, 'Big backup price', 10, 120.0, valinit=init_price_big, valstep=2.5)
# s_price_small = Slider(ax_price_small, 'Small backup price', 5, 130.0, valinit=init_price_small, valstep=2.5)
#
#
# def new_prices(single_try_big, single_try_small,  w_rate):
#     new_counter = 0
#     new_fail_big = 0
#     new_fail_small = 0
#     prices_new = dates.copy()
#     for new_time_iterator in dates:
#         for new_backup_date_iterator in backup_dates_big:
#             if new_time_iterator == new_backup_date_iterator:
#                 new_fail_big += 1
#         for new_backup_date_iterator in backup_dates_small:
#             if new_time_iterator == new_backup_date_iterator:
#                 new_fail_small += 1
#         prices_new[new_counter] = dates[new_counter] * w_rate + single_try_big * new_fail_big + single_try_small * new_fail_small
#         new_counter += 1
#     return prices_new
#
#
# def update(val):
#     price_big = s_price_big.val
#     price_small = s_price_small.val
#     work_rate = s_work_rate.val
#     fig.canvas.draw_idle()
#     l.set_ydata(new_prices(price_big, price_small, work_rate))
#
#
# s_work_rate.on_changed(update)
# s_price_big.on_changed(update)
# s_price_small.on_changed(update)
#
#
# def reset(event):
#     s_work_rate.reset()
#     s_price_big.reset()
#     s_price_small.reset()
#
#
# reset_ax = plt.axes([0.8, 0.01, 0.1, 0.04])
# button = Button(reset_ax, 'Reset', color=ax_color, hovercolor='0.975')
# button.on_clicked(reset)
# plt.show()
