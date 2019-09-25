import numpy as np


class Backup_cost:
    def __init__(self, work_rate, recovery_price, today, backups, prob):
        self.work_rate = work_rate
        self.recovery_price = recovery_price
        self.today = today
        self.backups = backups

    def initial_price(self):
        delta_t = 1
        self.recovery_price + delta_t*self.work_rate

    def recovery_attempt(self, date):
        prob = np.random.choice()

    def data_loss(self):
        success = 0
        while success == 0:
            i = 0
            self.recovery_attempt(self.backups[i])
            i += 1

    def backup_price_total(self):
        self.initial_price() + self.data_loss()*self.work_rate
