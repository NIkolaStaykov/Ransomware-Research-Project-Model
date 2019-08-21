import numpy as np
import scipy.stats as st


# class backup_PDF(st.rv_continuous):
#     def _pdf(self, x):
#         return 3*x**2

def backup_function(data_value, backup_price, probability):
    backup_prob = np.random.choice([0, 1], 1, p=[1 - probability, probability])
    if backup_prob == 1:
        return backup_price
    else:
        return data_value
