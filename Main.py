import Model as md
import numpy as np


sim = md.Simulation(200, 690, 130, 5, 0.5, 3)
str1 = input("Price: ")
example_price = int(str1)
print(sim.fit(example_price))
