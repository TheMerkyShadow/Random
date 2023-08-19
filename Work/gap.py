import datetime

def calculate_sales_goal():
    goal = int(input("Enter the sales goal: "))
    current_sales = int(input("Enter the current sales: "))
    
    current_date = datetime.datetime.now()
    last_day = (current_date.replace(day=28) + datetime.timedelta(days=4)).replace(day=1) - datetime.timedelta(days=1)
    
    remaining_days = 0
    days_worked = 0

    for day in range(current_date.day, last_day.day + 1):
        if current_date.replace(day=day).weekday() != 6:
            remaining_days += 1
            days_worked += 1
    
    gap = abs((current_sales - goal) / days_worked)
    boxes = int(gap) if gap >= 1 else 0
    
    print(f"Remaining days (excluding Sundays and off days): {remaining_days}")
    print(f"Gap: {gap:.2f}")
    print(f"Boxes: {boxes:.1f}")

if __name__ == "__main__":
    print("Sales Goal Calculator")
    calculate_sales_goal()
