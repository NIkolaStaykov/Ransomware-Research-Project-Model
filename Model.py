import numpy as np
import matplotlib.pyplot as plt
import math
import statistics as st
from Backup_function import backup_function
# from Plots import NDist


# Takes out a random WTP value from the distribution
def sample_point(mean, st_div):
    sample = np.random.normal(mean, st_div, 1)
    return sample[0]


class Simulation:

    def __init__(self, ppl_sample_size, mean, st_div, number_of_points, backup_prob, backup_price):
        self.ppl_sample_size = ppl_sample_size
        self.number_of_points = number_of_points
        # Distribution that follows people's WTP values
        self.mean = mean
        self.st_div = st_div
        self.backup_prob = backup_prob
        self.backup_price = backup_price

    # Approximates the point in the demand curve of a given price
    def fit(self, price_to_fit):

        ppl = 0

        ###########
        for i in range(0, self.ppl_sample_size):
            sam_point = sample_point(self.mean, self.st_div)
            sam_value = backup_function(sam_point, self.backup_price, self.backup_prob)
            if sam_value > price_to_fit:
                ppl += 1
        ############

        return ppl / self.ppl_sample_size

    # Plotting the experimental data
    def demand_exp_data(self):
        demand = []
        price = []
        price_step = math.floor((self.mean + 3 * self.st_div) / self.number_of_points)
        for i in range(self.number_of_points):
            demand.append(self.fit(price_step * i))
            price.append(price_step * i)
        # plt.scatter(price, demand, color="#86E9D1")
        data = [price, demand]
        return data

    # Error function to compare data with the actual plot
    def error_f(self):
        error = 0
        price_step = math.floor((self.mean + 3 * self.st_div) / self.number_of_points)
        for i in range(self.number_of_points):
            error += (self.fit(price_step * i) - self.demand_function(price_step * i)) ** 2
        error = error / self.number_of_points
        return error

    # Computes the demand function for the given parameters
    def demand_function(self, price):
        z_score = np.sign(price - self.mean) * (price - self.mean) / self.st_div
        if price > self.mean:
            demand = 1 / 2 - 1 / 2 * np.math.erf(z_score / np.sqrt(2))
        else:
            demand = 1 / 2 + 1 / 2 * np.math.erf(z_score / np.sqrt(2))
        return demand

    # Plotting the actual mathematical function
    # Returns prices and demand in two arrays
    def plot_demand_math(self):
        price_math = []
        demand_math = []
        max_price = math.floor(self.mean + 3 * self.st_div)
        for i in range(10 * max_price):
            price_math.append(i / 10)
            demand_math.append(self.demand_function(i / 10))
        plt.xlabel("Price")
        plt.ylabel("Demand")
        plt.plot(price_math, demand_math, color="#097A5E")
        plt_left = [price_math, demand_math]
        return plt_left

    # Calculating the revenue
    def revenue_function(self, price):
        revenue = price * self.demand_function(price)
        return revenue

    def plot_revenue(self):
        price = []
        revenue = []
        max_price = math.floor(self.mean + 3 * self.st_div)
        for i in range(10 * max_price):
            price.append(i / 10)
            revenue.append(self.revenue_function(i / 10))
        plt.xlabel("Price")
        plt.ylabel("Revenue")
        plt.plot(price, revenue, color="#A02A2A", linestyle='--')
        plt_right = [price, revenue]
        return plt_right


# Calculating errors
def error_percent(simulation, price):
    error = abs((simulation.fit(price)-simulation.demand_function(price))/simulation.fit(price))
    return error


def plotting_errors(simulation, sample_step, points_count):
    error_array = []
    error_mean = []
    sample_sizes = []
    for i in range(points_count):
        sim_it = Simulation(simulation.ppl_sample_size + sample_step * i, simulation.mean, simulation.st_div,
                            simulation.number_of_points, simulation.backup_prob, simulation.backup_price)
        for n in range(20):
            error = sim_it.error_f()
            error_array.append(error)
        mean = st.mean(error_array)
        error_array = []
        error_mean.append(mean)
        sample_sizes.append(simulation.ppl_sample_size + sample_step * i)
    plt.xlabel("Sample size")
    plt.ylabel("Error")
    plt.plot(sample_sizes, error_mean)


# Plotting error vs backup percentage
def backup_vs_profit(simulation, percent_step):
    profit_means = []
    backup_percentage = []
    steps = math.floor((1-simulation.backup_prob)/percent_step)
    for i in range(steps):
        sim_it = Simulation(simulation.ppl_sample_size, simulation.mean, simulation.st_div,
                            simulation.number_of_points, simulation.backup_prob + i*percent_step,
                            simulation.backup_price)
        sth = sim_it.demand_exp_data()
        expected_profit = math.floor(sim_it.ppl_sample_size * np.mean(np.multiply(sth[0], sth[1])))
        profit_means.append(expected_profit)
        backup_percentage.append(100*percent_step*i + 100*simulation.backup_prob)
    data = [backup_percentage, profit_means]
    return data
