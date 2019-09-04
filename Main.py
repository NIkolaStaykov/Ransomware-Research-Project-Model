import Model as md
# import numpy as np


sim = md.Simulation(200, 690, 130, 5, 0, 3)
str1 = input("Price: ")
price_to_estimate = int(str1)
# str1 = input("Acceptable Error: ")
# error = int(str1)

plot_data = sim.plot_demand_exp()

error_percentage = md.error_percent(sim, price_to_estimate)
print("Error: ", error_percentage, "%")
