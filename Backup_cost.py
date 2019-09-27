import numpy as np
# import datetime as dt


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
            return [success, "nada"]

    def data_loss(self):
        success = 0
        number_of_backups = len(self.backups)
        print("Number of backups:", number_of_backups)
        # successful_backups = []
        i = 0
        while success == 0:
            info = self.recovery_attempt(self.backups[i])
            success = info[0]
            print("tried with backup date:", self.backups[i])
            print("success state:", info[0])
            print("successful backup date:", info[1])
            if i == number_of_backups-1 and success == 0:
                print("Couldn't restore data")
                break
            i += 1
        # successful_backups.append(info[1])

    def backup_price_total(self):
        self.initial_price() + self.data_loss()*self.work_rate


backs = ['8/26/2019', '5/26/2019', '2/26/2019']
a = Backup_cost(300, 30, '9/26/2019', backs, 6/7)
a.data_loss()
