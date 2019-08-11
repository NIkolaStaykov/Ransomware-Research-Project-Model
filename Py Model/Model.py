import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

class Simulation:

    #Library for the prices, corresponding to a given ransom
    #sample_prices = {}

    def __init__(self, ppl_sample_size, mean, st_div):
        self.ppl_sample_size = ppl_sample_size
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
    def plot_demand_exp(self, number_of_points):
        demand = []
        price = []
        for i in range(number_of_points):
            c = math.floor((self.mean + 2*self.st_div)/number_of_points)
            demand.append(self.fit(c*i))
            price.append(8 * i)
        plt.scatter(price, demand, color="green")

    #Computes the demand function for the given parameters
    def demand_function(self, x):
        z_score = np.sign(x-self.mean)*(x-self.mean)/self.st_div
        if x > self.mean:
            y = 1/2-1/2*np.math.erf(z_score/np.sqrt(2))
        else:
            y = 1/2+1/2*np.math.erf(z_score/np.sqrt(2))
        return y

    # Plotting the actual mathematical function
    def plot_demand_math(self):
        price_math = []
        demand_math = []
        for i in range(8000):
            price_math.append(i / 10)
            demand_math.append(self.demand_function(i / 10))
        plt.plot(price_math, demand_math, color="red")

    #Time costs money
    #def time_price(self):

sim = Simulation(400, 500, 150)

plt.show()