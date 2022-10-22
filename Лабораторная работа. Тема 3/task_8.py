money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05


def calc_month_number(salary, spend, increase=0.05, money_capital=10000):
    month = 0
    while True:
        spend += spend * increase
        money_capital -= spend
        if money_capital < 0:
            break
        month += 1
        money_capital += salary
    print(month)


calc_month_number(salary=salary, spend=spend)
