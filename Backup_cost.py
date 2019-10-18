import numpy as np
import datetime
import matplotlib.pyplot as plt


class Backup_cost:
    info = []

    def __init__(self, work_rate, single_try_price, disaster_date, backups, fail_prob):
        self.work_rate = work_rate
        self.disaster_date = datetime.datetime.strptime(disaster_date, '%m/%d/%Y')
        self.backups = backups
        self.prob = fail_prob
        self.single_try_price = single_try_price

    def recovery_attempt(self, backup_date):
        success = np.random.choice([1, 0], 1, p=[1 - self.prob, self.prob])
        if success == 1:
            return [success, backup_date]
        else:
            return [success, "nada"]

    def data_loss(self):
        global info  # info[0] is the success state of the recovery, info[1] is the successful backup date or "nada"
        number_of_backups = len(self.backups)
        # print("Number of backups:", number_of_backups)
        # successful_backups = []
        i = 0
        success = 0
        while success == 0:
            if datetime.datetime.strptime(self.backups[i], '%m/%d/%Y') < self.disaster_date:
                info = self.recovery_attempt(self.backups[i])
                success = info[0]
                print("tried with backup date:", self.backups[i])
                print("success state:", success)
            else:
                print(self.backups[i], "does not exist yet")
            if i == number_of_backups - 1 and success == 0:
                print("Couldn't restore data")
                break
            i += 1
        info.append(i)
        return info

    def time_delta(self, recovery_date):
        recovery_date = datetime.datetime.strptime(recovery_date, '%m/%d/%Y')
        time_passed = self.disaster_date - recovery_date
        return time_passed

    def backup_price_total(self):
        new_info = self.data_loss()
        if new_info[0] == 1:
            backup_delta = self.time_delta(new_info[1])
            total = backup_delta.days*self.work_rate + info[2] * self.single_try_price
            print("total recovery price:", total)
            return total
        if new_info[0] == 0:
            print("Pay the ransom if data value is less")
            return None

    def point(self):
        x = self.time_delta(self.backups[-1])
        y = self.backup_price_total()
        return [x, y]


backs = ['9/23/2019', '9/20/2019', '9/13/2019']

# Backup_cost(work rate, recovery try price, disaster date, backup dates, failure probability)
a = Backup_cost(300, 50, '09/25/2019', backs, 1/2)
a.backup_price_total()
x = []
y = []
for it in range(200):
    # for k in range(5):
    y.append(a.backup_price_total())
    x.append(a.disaster_date)
    a.disaster_date += datetime.timedelta(days=1)
plt.plot(x, y, color="red")
plt.gcf().autofmt_xdate()
plt.show()
