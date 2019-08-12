import numpy as np
import matplotlib.pyplot as plt
import math
from Plots import normal_distribution
import statistics as st

class Simulation:

    def __init__(self, ppl_sample_size, mean, st_div, number_of_points):
        self.ppl_sample_size = ppl_sample_size
        self.number_of_points = number_of_points
        # Distribution that follows people's WTP values
        self.mean = mean
        self.st_div = st_div

    #Takes out a random WTP value from the distribution
    def sample_point(self, mean, st_div):
        sample = np.random.normal(mean, st_div, 1)
        return sample[0]

    #Aproximates the point in the demand curve of a given price
    def fit(self, price_to_fit):
        ppl = 0

        ###########
        for i in range(0, self.ppl_sample_size):
            sample_point = self.sample_point(self.mean, self.st_div)

            if sample_point > price_to_fit:
                ppl += 1
        ############

        return ppl/self.ppl_sample_size

    #Plotting the experimental data
    def plot_demand_exp(self):
        demand = []
        price = []
        price_step = math.floor((self.mean + 3 * self.st_div) / self.number_of_points)
        for i in range(self.number_of_points):
            demand.append(self.fit(price_step*i))
            price.append(price_step * i)
        plt.scatter(price, demand, color="#86E9D1")

    #Error function to compare data with the actual plot
    def error_f(self):
        error = 0
        price_step = math.floor((self.mean + 3 * self.st_div) / self.number_of_points)
        for i in range(self.number_of_points):
            error += (self.fit(price_step * i) - self.demand_function(price_step*i))**2
        error = error/self.number_of_points
        return(error)

    #Computes the demand function for the given parameters
    def demand_function(self, price):
        z_score = np.sign(price-self.mean)*(price-self.mean)/self.st_div
        if price > self.mean:
            demand = 1/2-1/2*np.math.erf(z_score/np.sqrt(2))
        else:
            demand = 1/2+1/2*np.math.erf(z_score/np.sqrt(2))
        return demand

    # Plotting the actual mathematical function
    def plot_demand_math(self):
        price_math = []
        demand_math = []
        max_price = math.floor(self.mean + 3*self.st_div)
        for i in range(10*max_price):
            price_math.append(i / 10)
            demand_math.append(self.demand_function(i / 10))
        plt.xlabel("Price")
        plt.ylabel("Demand")
        plt.plot(price_math, demand_math, color="#097A5E")

# Calculating errors
def plotting_errors(sim, sample_step, points_count):
    global mean
    error_array = []
    error_mean = []
    sample_sizes = []
    for i in range(points_count):
        sim_it = Simulation(sim.ppl_sample_size + sample_step*i, sim.mean, sim.st_div, sim.number_of_points)
        for n in range(10):
            error = sim_it.error_f()
            error_array.append(error)
        mean = st.mean(error_array)
        error_array = []
        error_mean.append(mean)
        sample_sizes.append(sim.ppl_sample_size + sample_step*i)
    plt.xlabel("Sample size")
    plt.ylabel("Error")
    plt.plot(sample_sizes, error_mean)

sim = Simulation(100, 500, 150, 200)
#plotting_errors(sim, 30, 30)

norm = normal_distribution(500, 150, -2/3)
norm.plot_integral()
# sim.plot_demand_math()
# price = sim.mean + sim.st_div * norm.z_score
# point_demand = sim.demand_function(price)
# plt.plot(price, point_demand, color = "#BB0D0D", marker = "o")

plt.show()