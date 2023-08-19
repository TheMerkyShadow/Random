from datetime import datetime, timedelta
import calendar

# Input your sales goal and current sales
goal = int(input("Enter your sales goal: "))
current_sales = int(input("Enter your current sales: "))

# Get the current date
current_date = datetime.now()

# Get the last day of the current month
_, last_day = calendar.monthrange(current_date.year, current_date.month)

# Calculate the remaining days while excluding Sundays and off days
remaining_days = 0
days_worked = 0
for day in range(current_date.day, last_day + 1):
    if datetime(current_date.year, current_date.month, day).weekday() != 6:  # Sunday
        if (day - current_date.day) % 7 != 0:  # Exclude off days every 7 days
            remaining_days += 1
            days_worked += 1

# Calculate the positive gap
positive_gap = (goal - current_sales) / days_worked

print("Remaining days (excluding Sundays and off days):", remaining_days)
print("Positive Gap:", positive_gap)
