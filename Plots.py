import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import Model as md


# Plotting the integral under ND
class NormDist:

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
        plt.yticks([])
        ax.set_xlabel('Price')
        ax.plot(x, stats.norm.pdf(x, self.mean, self.sd), color="#0698B0")


def double_plot(left_data, right_data):
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(left_data[0], left_data[1], color="#097A5E")
    ax2.plot(left_data[0], right_data[1], color="#A02A2A", linestyle='--')

    ax1.set_xlabel('Price')
    ax1.set_ylabel('Demand', color="#097A5E")
    ax2.set_ylabel('Revenue', color="#A02A2A")
    ax2.tick_params(axis="y")


class PaperPlots:
    def __init__(self, prob_1, prob_2, mean, something):
        self.prob_1 = prob_1
        self.prob_2 = prob_2
        self.mean = mean
        self.something = something

    def two_armed_bandit(self):
        x = np.linspace(0, 1, 100)
        y = self.prob_1
        plt.plot(x, y)
