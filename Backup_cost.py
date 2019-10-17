import numpy as np
import datetime
import matplotlib.pyplot as plt


class Backup_cost:
    info = []

    def __init__(self, work_rate, recovery_price, disaster_date, backups, fail_prob):
        self.work_rate = work_rate
        self.recovery_price = recovery_price
        self.disaster_date = datetime.datetime.strptime(disaster_date, '%m/%d/%Y')
        self.backups = backups
        self.prob = fail_prob

    def initial_price(self):
        delta_t = 1
        in_price = self.recovery_price + delta_t*self.work_rate
        return in_price

    def recovery_attempt(self, backup_date):
        success = np.random.choice([1, 0], 1, p=[1 - self.prob, self.prob])
        if success == 1:
            return [success, backup_date]
        else:
            return [success, "nada"]

    def data_loss(self):
        global info  # info[0] is the success state of the recovery, info[1] is the successful backup date
        success = 0
        number_of_backups = len(self.backups)
        # print("Number of backups:", number_of_backups)
        # successful_backups = []
        i = 0
        while success == 0:
            info = self.recovery_attempt(self.backups[i])
            success = info[0]
            # print("tried with backup date:", self.backups[i])
            # print("success state:", info[0])
            print("successful backup date:", info[1])
            if i == number_of_backups-1 and success == 0:
                print("Couldn't restore data")
                info[1] = 0
                break
            i += 1
        # successful_backups.append(info[1])
        if info[1] == 0:
            unsuccessful_recovery()
        return info

    def time_delta(self):
        state = self.data_loss()
        if state[1] != 0:
            successful_backup_date = datetime.datetime.strptime(state[1], '%m/%d/%Y')
            time_passed = self.disaster_date-successful_backup_date
            return time_passed

    def backup_price_total(self):
        data_delta = self.time_delta()
        total = self.initial_price() + data_delta.days*self.work_rate
        # print("total recovery price:", total)
        return total


def unsuccessful_recovery():
    print("You better pay the ransom")


backs = ['9/23/2019', '9/20/2019', '9/13/2019']
# Backup_cost(work rate, recovery try price, disaster date, backup dates, failure probability)
a = Backup_cost(300, 30, '09/26/2019', backs, 1/5)
x = []
y = []
for i in range(20):
    y.append(a.backup_price_total())
    x.append(a.disaster_date)
    a.disaster_date += datetime.timedelta(days=1)
print(y)
plt.plot(x, y, color="red")
plt.show()
