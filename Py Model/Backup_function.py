import numpy as np


def willingness_to_pay(data_value, backup_price, probability):
    backup_prob = np.random.choice(1, 1, p=[1 - probability, probability])
    if backup_prob == 1:

        return backup_price

    else:
        return data_value

