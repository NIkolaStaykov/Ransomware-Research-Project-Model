# import Model as md
# # import numpy as np
#
#
# sim = md.Simulation(200, 690, 130, 5, 0, 3)
# str1 = input("Price: ")
# ransom_value = int(str1)
# str1 = input("Acceptable Error: ")
# error_boundary = float(str1)
# error_boundary = error_boundary/1000
#
# b = 1
# while b:
#     error_percentage = md.error_percent(sim, ransom_value)
#     if error_percentage < error_boundary:
#         b = 0
#         print("Minimal sample size: ", sim.ppl_sample_size)
#     sim.ppl_sample_size += 20

import matplotlib.pyplot as plt
import Mathematical_function_backups as math

math.setting_the_constants()
x_data = []
y_data = []
for k in range(100):
    x_data.append(k)
    y_data.append(math.expected_price(k))
print(x_data)
print(y_data)
plt.plot(x_data, y_data)
name = 'Math_plot_' + str(k) + '.png'
plt.savefig(name, bbox_inches='tight')

