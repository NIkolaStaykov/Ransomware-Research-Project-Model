import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.stats as stats
import statistics as st

class Simulation:

    #Library for the prices, corresponding to a given ransom
    #sample_prices = {}

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
        #self.sample_prices[str(price_to_fit)] = []

        ###########
        for i in range(0, self.ppl_sample_size):
            sample_point = self.sample_point(self.mean, self.st_div)

            if sample_point > price_to_fit:
                ppl += 1

            #self.sample_prices[str(price_to_fit)].append(sample_point)
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
        plt.scatter(price, demand, color="green")
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
        max_price = self.mean + 3*self.st_div
        for i in range(10*max_price):
            price_math.append(i / 10)
            demand_math.append(self.demand_function(i / 10))
        plt.plot(price_math, demand_math, color="red")

    #Calculating costs
class Costs:
    def __init__(self, ppl_sample_size, number_of_points):
        self.ppl_sample_size = ppl_sample_size
        self.number_of_points = number_of_points
    def spam_costs(self, spam_price):
        return(self.ppl_sample_size * spam_price)
    def time_costs(self, price_function):
        price = price_function(self.number_of_points)
        return(price)


#Calculating errors
error_array = []
error_mean = []
sample_sizes = []
# for i in range(12):
#
#     sim = Simulation(400 + 50*i, 500, 150, 200)
#     for n in range(10):
#         error = 10000 * sim.error_f()
#         error_array.append(error)
#     mean = st.mean(error_array)
#     error_array = []
#     error_mean.append(mean)
#     sample_sizes.append(400 + 50*i)
#
# plt.plot(sample_sizes, error_mean)
#
# sim = Simulation(200, 500, 200, 100)
# sim.plot_demand_exp()
# sim.plot_demand_math()
#
# plt.show()

def normal_distribution(mean, sd):
    x = np.linspace(mean - 2/3*sd, mean + 3*sd, 100)
    frame = plt.fill_between(x, stats.norm.pdf(x, mean, sd), color="#0698B0")
    frame.axes.get_yaxis().set_visible(False)
    x = np.linspace(0, mean + 3*sd,100)
    plt.plot(x, stats.norm.pdf(x, mean, sd), color="k")
    const = mean - 2/3*sd
    plt.xlabel("Price")

normal_distribution(500, 150)
plt.show()