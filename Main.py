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
z_data = []
for k in range(100):
    # math.set_globals(30, 50 + 3*k)
    print('\n', "Days from beginning", k)
    x_data.append(k)
    y_data.append(math.expected_price(k))
    z_data.append(math.only_full_price(k))
# fig = plt.figure()
# ax = fig.add_subplot(11)
plt.xlabel("Time from first backup")
plt.ylabel("Expected price")
# plt.zlabel("Work rate")
# ax.plot_wireframe(x_data, y_data, z_data)
for i in range(len(y_data)-1):
    print("x=", x_data[i], '\t', "y=", y_data[i], "only full:", z_data[i])
plt.plot(x_data, y_data)
plt.show()

