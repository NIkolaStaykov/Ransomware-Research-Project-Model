import numpy as np
import datetime


class Backup_cost:
    info = []

    def __init__(self, work_rate, single_try_small, single_try_big, disaster_date, backups, fail_prob_small, fail_prob_big):
        self.work_rate = work_rate
        self.disaster_date = datetime.datetime.strptime(disaster_date, '%m/%d/%Y')
        self.backups = backups
        self.fail_prob_small = fail_prob_small
        self.single_try_small = single_try_small
        self.single_try_big = single_try_big
        self.fail_prob_big = fail_prob_big

    def recovery_attempt(self, backup):
        if backup.backup_type == "small":
            success = np.random.choice([1, 0], 1, p=[1 - self.fail_prob_small, self.fail_prob_small])
            if success == 1:
                return [success, backup.date]
            else:
                return [success, None]
        if backup.backup_type == "big":
            success = np.random.choice([1, 0], 1, p=[1 - self.fail_prob_big, self.fail_prob_big])
            if success == 1:
                return [success, backup.date]
            else:
                return [success, None]

    # calculates the difference between the successful backup date and the disaster date in dates
    # returns the difference in days and the number of unsuccessful backups from the respective types
    def data_loss_info(self):
        info = []  # info[0] is the success state of the recovery, info[1] is the successful backup date or "nada"
        # info[2] is the number of small backups, info[3]- the same for big backups and info[4]-the type of
        # successful backup, if any
        number_of_backups = len(self.backups)
        i = 0
        success = 0
        fail_counter_small = 0
        fail_counter_big = 0
        success_type = None

        # Full backup operation
        while success == 0:
            if self.backups[i].date < self.disaster_date and self.backups[i].backup_type == "big":
                full_info = self.recovery_attempt(self.backups[i])
                success = full_info[0]
                print("tried with backup date:", self.backups[i].date)
                print("success state:", success)
                if success == 0:
                    fail_counter_big += 1
                if success == 1:
                    success_type = self.backups[i].backup_type
                    info.append(1)
                    info.append(self.backups[i].date)
                    print("Full successful recovery date: ", success_type, self.backups[i].date)
            elif self.backups[i].date < self.disaster_date and self.backups[i].backup_type == "small":
                print(self.backups[i].date, "Small backup, ignore for now")
            else:
                print(self.backups[i].date, "Does not exist yet")
            if i == number_of_backups - 1 and success == 0:
                info.append(0)
                info.append(None)
                print("Couldn't restore data")
                break
            i += 1

        # Incremental backups operation
        if success == 1:
            i -= 2
            while success == 1 and self.backups[i].backup_type == 'small':
                inc_info = self.recovery_attempt(self.backups[i])
                success = inc_info[0]
                fail_counter_small += 1
                i -= 1
                if success == 0:
                    info[1] = self.backups[i+1].date
        print("failed incremental count:", fail_counter_small)
        print("failed full count:", fail_counter_big)
        info.append(fail_counter_small)
        info.append(fail_counter_big)
        info.append(success_type)
        return info

    def time_delta(self, recovery_date):
        time_passed = self.disaster_date - recovery_date
        return time_passed

    def backup_price_total(self):
        print("disaster date:", self.disaster_date)
        new_info = self.data_loss_info()
        if new_info[0] == 1:
            backup_delta = self.time_delta(new_info[1])
            total = backup_delta.days*self.work_rate + new_info[2] * self.single_try_small + new_info[3] * self.single_try_big
            print("total recovery price:", total, '\n', "number of fails:", new_info[2] + new_info[3], '\n')
            return [backup_delta, total, new_info[4]]
        if new_info[0] == 0:
            print("Pay the ransom if data value is less", '\n')
            return [0, -100, new_info[4]]

    def point(self):
        color = 0
        colors = ['#42DE20', '#39C01B', '#309F17', '#288314', '#226D11', '#174E0B', '#114007']
        info = self.backup_price_total()
        x = self.disaster_date
        y = info[1]
        success_type = info[2]
        if success_type is None:
            color = "red"
        elif success_type == 'big':
            color = "blue"
        elif success_type == 'small':
            color = "green"
        return [x, y, color]
