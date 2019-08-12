import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


# Plotting the integral under ND
class Normal_distribution:

    def __init__(self, mean, sd, z_score):
        self.mean = mean
        self.sd = sd
        self.z_score = z_score

    def plot_integral(self):
        integral_price = self.mean + self.z_score*self.sd
        x = np.linspace(integral_price, self.mean + 3 * self.sd, 100)
        frame = plt.fill_between(x, stats.norm.pdf(x, self.mean, self.sd), color="#0698B0")
        frame.axes.get_yaxis().set_visible(False)
        x = np.linspace(0, self.mean + 3 * self.sd,100)
        plt.plot(x, stats.norm.pdf(x, self.mean, self.sd), color="k")
