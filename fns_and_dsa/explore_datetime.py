from datetime import datetime

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_date)

display_current_datetime()
from datetime import datetime, timedelta
def calculate_future_date(days):
    future_date = datetime.now() + timedelta(days=days)
    print(future_date.strftime("%Y-%m-%d"))
days_input = int(input("Enter the number of days: "))
calculate_future_date(days_input)
