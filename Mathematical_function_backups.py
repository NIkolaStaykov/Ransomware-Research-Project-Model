import numpy as np
full = 0
incremental = 0
not_backed = int(input("Not backed: "))
work_rate = int(input("Work rate: "))


class Backup:
    def __init__(self):
        self.probability = float(input("Fail prob: "))
        self.price = int(input('Recovery price: '))
        self.interval = int(input("Interval:"))


def setting_the_constants():
    global full, incremental
    print("Full backup:")
    full = Backup()
    print("Incremental backup:")
    incremental = Backup()


def days_from_working_full(i, x):
    number_of_fails = i
    days_from_first = x
    global full
    days = full.interval(np.modf(days_from_first/full.interval)[0] + number_of_fails)
    return days


def expected_price(x):
    days_from_first_backup = x
    global full, incremental, not_backed, work_rate
    print(full.probability)
    work_total = (days_from_first_backup + not_backed)*work_rate
    full_backups_count = np.modf(days_from_first_backup/full.interval)[1] + 1
    price = pow(full.probability, full_backups_count)(work_total + full_backups_count*full.price)
    print(price)


setting_the_constants()
expected_price(30)

