import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Simulation:

    sample_prices = {}

    def __init__(self, ppl_sample_size, mean, sd):
        self.ppl_sample_size = ppl_sample_size
        # Distribution that follows people's WTP values
        self.mean = mean
        self.sd = sd

    def sample_point(self, mean, sd):
        sample = np.random.normal(mean, sd, 1)
        return sample[0]

    def fit(self, price_to_fit):
        ppl = 0
        self.sample_prices[str(price_to_fit)] = []

        ###########
        for i in range(0, self.ppl_sample_size):
            sample_point = self.sample_point(self.mean, self.sd)

            if  sample_point > price_to_fit:
                ppl += 1

            self.sample_prices[str(price_to_fit)].append(sample_point)
        ############

        return ppl/self.ppl_sample_size

sim = Simulation(3000, 500, 150)
print(sim.sample_prices)

demand = []
price = []

for i in range(400):
    demand.append(sim.fit(2*i))
    price.append(2*i)

plt.scatter(price, demand, color="green")
plt.show()
print("(",price[0],demand[0])

