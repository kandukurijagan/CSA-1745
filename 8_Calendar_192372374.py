import calendar
year = int(input("Enter year (e.g., 2025): "))
month = int(input("Enter month (1-12): "))
print("\nHere is the calendar:\n")
print(calendar.month(year, month))
