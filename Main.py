import Model as md
# import numpy as np


sim = md.Simulation(200, 690, 130, 5, 0, 3)
str1 = input("Price: ")
ransom_value = int(str1)
str1 = input("Acceptable Error: ")
error_boundary = float(str1)
error_boundary = error_boundary/1000

b = 1
while b:
    error_percentage = md.error_percent(sim, ransom_value)
    if error_percentage < error_boundary:
        b = 0
        print("Minimal sample size: ", sim.ppl_sample_size)
    sim.ppl_sample_size += 20


