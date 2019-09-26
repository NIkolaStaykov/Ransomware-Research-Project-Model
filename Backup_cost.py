import numpy as np
import datetime as dt


class Backup_cost:
    def __init__(self, work_rate, recovery_price, today, backups, fail_prob):
        self.work_rate = work_rate
        self.recovery_price = recovery_price
        self.today = today
        self.backups = backups
        self.prob = fail_prob

    def initial_price(self):
        delta_t = 1
        self.recovery_price + delta_t*self.work_rate

    def recovery_attempt(self, backup_date):
        success = np.random.choice([1, 0], 1, p=[1 - self.prob, self.prob])
        if success == 1:
            return [success, backup_date]
        else:
            return success

    def data_loss(self):
        success = 0
        successful_backups = []
        while success == 0:
            i = 0
            info = self.recovery_attempt(self.backups[i])
            success = info[0]
            i += 1
        successful_backups.append(info[1])

    def backup_price_total(self):
        self.initial_price() + self.data_loss()*self.work_rate

backups = ['8/26/2019', '5/26/2019', '2/26/2019']
Backup_cost(300, 30, '9/26/2019', )
