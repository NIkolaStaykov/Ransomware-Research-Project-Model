import Model as md
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import Mathematical_function_backups as math
import numpy as np

# Plotting mathematical expectation
#
output = open("Paper_stuff_1.txt", "w")
output.write("\hline" + '\n' + "Constant & Full Interval & Incremental interval \hline" + '\n')
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
best_incremental = {}
for l in range(1):
    math.storage_price = math.work_rate / (1000 + 500*l)
    for j in range(1, 29):
        incremental_interval = {}
        math.full.interval = j+1
        for i in range(1, j+1):
            math.incremental.interval = i
            prices = []
            for k in range(30, 90):
                prices.append(math.expected_recovery_price(k) + math.storage_cost(k))
            incremental_interval[i] = np.mean(prices)  # np.sum(prices)
            x.append(j+1)
            y.append(i+1)
            z.append(incremental_interval[i])
        means[j+1] = incremental_interval
        best_incremental[j+1] = min(incremental_interval.items(), key=lambda x: x[1])
    best_overall = min(best_incremental.items(), key=lambda x: x[1][1])
    print("c=", math.work_rate/math.storage_price, best_overall)
    output.write(str(1000 + 500*l) + " & " + str(best_overall[0]) + " & " + str(best_overall[1][0]) + chr(92)*2 + " " + chr(92) + "hline" '\n')

# 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='blue', marker='o')
ax.set_xlabel("Full interval")
ax.set_ylabel("Incremental interval")
ax.set_zlabel("Price")

plt.show()
