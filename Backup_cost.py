import numpy as np
import datetime


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
            return [success, None]

    # calculates the difference between the successful backup date and the disaster date in dates
    # returns the difference in days and the number of unsuccessful backups from the respective types
    def data_loss_info(self):
        info = []  # info[0] is the success state of the recovery, info[1] is the successful backup date or "nada"
        number_of_backups = len(self.backups)
        i = 0
        success = 0
        fail_counter_small = 0
        fail_counter_big = 0
        while success == 0:
            if datetime.datetime.strptime(self.backups[i].date, '%m/%d/%Y') < self.disaster_date:
                info = self.recovery_attempt(self.backups[i].date)
                success = info[0]
                print("tried with backup date:", self.backups[i].date)
                print("success state:", success)
                if self.backups[i].backup_type == "small" and success == 0:
                    fail_counter_small += 1
                if self.backups[i].backup_type == "big" and success == 0:
                    fail_counter_big += 1
            else:
                print(self.backups[i].date, "does not exist yet")
            if i == number_of_backups - 1 and success == 0:
                print("Couldn't restore data")
                break
            i += 1
        info.append(fail_counter_small)
        info.append(fail_counter_big)
        return info

    def time_delta(self, recovery_date):
        # recovery_date = datetime.datetime.strptime(recovery_date, '%m/%d/%Y')
        time_passed = self.disaster_date - recovery_date
        return time_passed

    def backup_price_total(self):
        new_info = self.data_loss_info()
        if new_info[0] == 1:
            backup_delta = self.time_delta(new_info[1])
            total = backup_delta.days*self.work_rate + new_info[2] * self.single_try_price
            print("total recovery price:", total, '\n', "number of fails:", new_info[2], '\n')
            return [backup_delta, total]
        if new_info[0] == 0:
            print("Pay the ransom if data value is less", '\n')
            return [0, -100]

    def point(self):
        x = self.disaster_date
        y = self.backup_price_total()[1]
        if y == -100:
            color = "red"
        else:
            color = "blue"
        return [x, y, color]
