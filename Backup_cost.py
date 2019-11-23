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
        counter_big = 0
        success_type = None

        # Full backup operation
        while success == 0:
            if self.backups[i].date < self.disaster_date and self.backups[i].backup_type == "big":
                full_info = self.recovery_attempt(self.backups[i])
                success = full_info[0]
                print("tried with full backup date:", self.backups[i].date)
                print("success state:", success)
                counter_big += 1
                if success == 1:
                    success_type = self.backups[i].backup_type
                    info.append(1)
                    info.append(self.backups[i].date)
                    print("Full successful recovery date: ", success_type, full_info[1])
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
            print("First incremental", self.backups[i].date)
            print("Disaster date", self.disaster_date)
            while success == 1 and self.backups[i].backup_type == 'small' and self.disaster_date > self.backups[i].date:
                inc_info = self.recovery_attempt(self.backups[i])
                success = inc_info[0]
                print("Tried with inc backup date:", self.backups[i].backup_type, self.backups[i].date)
                print("success state:", success)
                fail_counter_small += 1
                if success == 0:
                    info[1] = self.backups[i+1].date
                if inc_info[0] == 1:
                    success_type = "small"
                if success == 1 and self.backups[i-1].backup_type == 'big':
                    info[1] = self.backups[i].date
                i -= 1

        # formatting return data
        print("Incremental count:", fail_counter_small)
        print("Last successful backup:", info[1], success_type)
        print("failed full count:", counter_big)
        info.append(fail_counter_small)
        info.append(counter_big)
        info.append(success_type)
        return info

    def time_delta(self, recovery_date):
        time_passed = self.disaster_date - recovery_date
        return time_passed

    def backup_price_total(self):
        print("disaster date:", self.disaster_date)
        new_info = self.data_loss_info()
        print(new_info)
        if new_info[0] == 1:
            backup_delta = self.time_delta(new_info[1])
            total = backup_delta.days * self.work_rate + new_info[2] * self.single_try_small + new_info[3] * self.single_try_big
            print("total recovery price:", total, '\n')
            return [total, new_info[4], new_info[2]]
        if new_info[0] == 0:
            print("Pay the ransom if data value is less", '\n')
            price = ((self.disaster_date - self.backups[-1].date).days + 10) * self.work_rate + self.single_try_big * new_info[3]
            return [price, new_info[4]]

    def point(self):
        color = 0
        colors = [50, 55, 60, 65, 70, 75, 80]
        info = self.backup_price_total()
        x = self.disaster_date
        y = info[0]
        success_type = info[1]
        if success_type is None:
            color = 0
        elif success_type == 'big':
            color = 30
        elif success_type == 'small':
            color = colors[info[2]]
        return [x, y, color]
