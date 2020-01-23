import Model as md
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import Mathematical_function_backups as math
import numpy as np

#
# sim = md.Simulation(200, 690, 130, 100, 0, 3)
# exp_data = sim.demand_exp_data()
# math_data = sim.plot_demand_math()
# fig, ax = plt.subplots()
# ax.plot(math_data[0], math_data[1])
# ax.scatter(exp_data[0], exp_data[1])
# plt.show()
# ransom_value = int(input("Price: "))
# str1 = input("Acceptable Error: ")
# error_boundary = float(str1)
# error_boundary = error_boundary/1000

# b = 1
# while b:
#     error_percentage = md.error_percent(sim, ransom_value)
#     if error_percentage < error_boundary:
#         b = 0
#         print("Minimal sample size: ", sim.ppl_sample_size)
#     sim.ppl_sample_size += 20


# Plotting mathematical expectation
#
math.setting_the_constants()
x_data = []
y_data = []
z_data = []
# for k in range(300):
#     # math.set_globals(30, 50 + 3*k)
#     x_data.append(k)
#     y_data.append(math.expected_price(k))
#     z_data.append(math.only_full_price(k))
# fig2, ax_1 = plt.subplots()
# ax_1.set_xlabel("Time from first backup")
# ax_1.set_ylabel("Expected price")
# ax_1.plot(x_data, y_data, color="#384986", label='With Incremental')
# ax_1.plot(x_data, z_data, color="#A02A2A", label='Full backups only')
# fig2.legend()
#
# # plotting a histogram
# fig2, ax_2 = plt.subplots()
# for i in range(10, 16, 1):
#     ax_2.cla()
#     ax_2.set_xlabel("Recovery price")
#     ax_2.set_ylabel("Number of recoveries")
#     name = "Histogram_" + str(i) + ".png"
#     ax_2.hist(y_data, bins=i, color="#384986")
#     plt.savefig(name)

# Data for the 3D plot
means = {}
x = []
y = []
z = []
for j in range(1, 18):
    incremental_interval = {}
    math.full.interval = j+1
    for i in range(j):
        math.incremental.interval = i+1
        prices = []
        for k in range(200):
            prices.append(math.expected_recovery_price(k)+math.storage_cost(k))
        incremental_interval[i+1] = np.mean(prices)
        x.append(j)
        y.append(i)
        z.append(np.mean(prices))
    means[j+1] = incremental_interval
    print(incremental_interval)
    print()

# 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='blue', marker='o')
ax.set_xlabel("Full interval")
ax.set_ylabel("Incremental interval")
ax.set_zlabel("Price")

plt.show()
