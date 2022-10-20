salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

while months > 0:
    diff = spend - salary
    need_money += diff
    months -= 1
    spend += spend * increase

print(round(need_money))
