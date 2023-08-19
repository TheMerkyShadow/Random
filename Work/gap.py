import datetime
import math

def calculate():
    goal = int(input("Sales Goal: "))
    current_sales = int(input("Current Sales: "))

    current_date = datetime.datetime.now()
    last_day = (current_date.replace(day=28) + datetime.timedelta(days=4)).replace(day=1) - datetime.timedelta(days=1)
    
    remaining_days = 0
    days_worked = 0
    for day in range(current_date.day, last_day.day + 1):
        if current_date.replace(day=day).weekday() != 6:  # Sunday is 6
            if (day - current_date.day) % 7 != 0:
                remaining_days += 1
                days_worked += 1
    
    gap = abs((current_sales - goal) / days_worked)
    rounded_gap = math.ceil(gap) if gap > 1 else (0 if gap < 1 else gap)
    
    print(f"Remaining days (excluding Sundays and off days): {remaining_days}")
    print(f"Gap: {rounded_gap:.1f}")

calculate()
