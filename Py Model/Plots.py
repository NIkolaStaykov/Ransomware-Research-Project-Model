import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


# Plotting the integral under ND
class NDist:

    def __init__(self, mean, sd, z_score):
        self.mean = mean
        self.sd = sd
        self.z_score = z_score

    def plot_integral(self):
        integral_price = self.mean + self.z_score*self.sd
        x = np.linspace(integral_price, self.mean + 3 * self.sd, 100)
        frame = plt.fill_between(x, stats.norm.pdf(x, self.mean, self.sd), color="#0698B0")
        frame.axes.get_yaxis().set_visible(False)
        x = np.linspace(0, self.mean + 3 * self.sd, 100)
        plt.plot(x, stats.norm.pdf(x, self.mean, self.sd), color="k")

    def plot_clean(self):
        fig, ax = plt.subplots(1)
        x = np.linspace(self.mean - 3 * self.sd, self.mean + 3 * self.sd, 100)
        ax.set_xlabel('X')
        ax.set_ylabel('Y', color="#0698B0")
        ax.plot(x, stats.norm.pdf(x, self.mean, self.sd), color="#0698B0")


def double_plot(left, right):
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(left[0], left[1], color="#097A5E")
    ax2.plot(left[0], right[1], color="#A02A2A", linestyle='--')

    ax1.set_xlabel('Price')
    ax1.set_ylabel('Demand', color="#097A5E")
    ax2.set_ylabel('Revenue', color="#A02A2A")
    ax2.tick_params(axis="y")
