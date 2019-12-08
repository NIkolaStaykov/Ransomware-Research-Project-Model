# import Model as md
# # import numpy as np
#
#
# sim = md.Simulation(200, 690, 130, 5, 0, 3)
# ransom_value = int(input("Price: "))
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
from mpl_toolkits.mplot3d import Axes3D
import Mathematical_function_backups as math
import numpy as np

# Plotting mathematical expectation

math.setting_the_constants()
"""
x_data = []
y_data = []
z_data = []
for k in range(100):
    # math.set_globals(30, 50 + 3*k)
    x_data.append(k)
    y_data.append(math.expected_price(k))
    z_data.append(math.only_full_price(k))
fig2, ax_1 = plt.subplots()
ax_1.set_xlabel("Time from first backup")
ax_1.set_ylabel("Expected price")
ax_1.plot(x_data, y_data, color="#097A5E", label='With Incremental')
ax_1.plot(x_data, z_data, color="#A02A2A", label='Full backups only')
fig2.legend()
"""

# plotting a histogram
"""
fig2, ax_2 = plt.subplots()
for i in range(10, 24, 1):
    ax_2.cla()
    ax_2.set_xlabel("Recovery price")
    ax_2.set_ylabel("Number of recoveries")
    name = "Histogram_" + str(i) + ".png"
    ax_2.hist(y_data, bins=i)
    plt.savefig(name)

"""
prices = []
means = {}
x = []
y = []
z = []
for j in range(1, 20):
    incremental_interval = {}
    math.full.interval = j+1
    for i in range(j):
        math.incremental.interval = i+1
        for k in range(500):
            prices.append(math.expected_price(k))
        incremental_interval[i+1] = np.mean(prices)
        x.append(j)
        y.append(i)
        z.append(np.mean(prices))
        print("Full interval: ", j + 1, "Incremental interval: ", i + 1, "Price: ", np.mean(prices))
    means[j+1] = incremental_interval

# 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='blue', marker='o')
ax.set_xlabel("Full interval")
ax.set_ylabel("Incremental interval")
ax.set_zlabel("Price")

plt.show()
