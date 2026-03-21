from datetime import datetime

def days(start, end):
    d_start = datetime.strptime(start, "%Y-%m-%d").date()
    d_end = datetime.strptime(end, "%Y-%m-%d").date()
    days = (d_end - d_start).days
    return days


print(days("2024-01-01", "2024-12-31"))
print(days("2024-02-15", "2024-03-20"))

