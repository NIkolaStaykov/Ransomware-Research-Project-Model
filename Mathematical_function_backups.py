import numpy as np

full = 0
incremental = 0
not_backed = 10  # int(input("Not backed: "))
work_rate = 300  # int(input("Work rate: "))


class Backup:
    def __init__(self):
        self.probability = float(input("Fail prob: "))
        self.price = int(input('Recovery price: '))
        self.interval = int(input("Interval: "))


def set_globals(days_to_first_backup, w_rate):
    global work_rate, not_backed
    work_rate = w_rate
    not_backed = days_to_first_backup


def setting_the_constants():
    global full, incremental
    print("Full backup:")
    full = Backup()
    print("Incremental backup:")
    incremental = Backup()


def days_from_successful_full(number_of_fails, days_from_first):
    global full
    days = full.interval*(np.modf(days_from_first/full.interval)[0] + number_of_fails)
    return days


def incremental_count(days_from_success_full):
    global full, incremental
    if full.interval <= days_from_success_full:
        number = np.modf(full.interval/incremental.interval)[1]
        return number
    else:
        number = np.modf(days_from_success_full/incremental.interval)[1]
        return number


def incremental_cost(days_from_succ_full):
    global incremental, full, work_rate
    l = int(incremental_count(days_from_succ_full))
    price = pow(1-incremental.probability, l)*((days_from_succ_full - incremental.interval*l)*work_rate + incremental.price*l)
    for i in range(l):
        price += pow(1-incremental.probability, i)*incremental.probability*((days_from_succ_full - incremental.interval * i) * work_rate + incremental.price * (i + 1))
    return price


def expected_price(days_from_first_backup):
    x = days_from_first_backup
    global full, incremental, not_backed, work_rate
    work_total = (x + not_backed)*work_rate
    full_backups_count = np.modf(x/full.interval)[1] + 1
    price = pow(full.probability, full_backups_count)*(work_total + full_backups_count*full.price)
    for i in range(int(full_backups_count)):
        price += (1-full.probability)*pow(full.probability, i)*(incremental_cost(days_from_successful_full(i, x)) + (i + 1) * full.price)
    return price


def only_full_price(days_from_first_backup):
    x = days_from_first_backup
    global full, not_backed, work_rate
    work_total = (x + not_backed) * work_rate
    full_backups_count = np.modf(x / full.interval)[1] + 1
    price = pow(full.probability, full_backups_count) * (work_total + full_backups_count * full.price)
    for i in range(int(full_backups_count)):
        price += (1-full.probability)*pow(full.probability, i)*((np.modf(days_from_first_backup/full.interval)[0] + i) * full.interval * work_rate + (i + 1)*full.price)
    return price
