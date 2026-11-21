from datetime import datetime
#ASK FOR THE DATA
print("--- REGISTRATION ---")
first = input("Enter your first name: ").strip()
last = input("Enter your last name: ").strip()
section = input("Enter section: ").upper()
event = input("Enter the name of the event: ").title()
year = input("Enter the year of the event: ")
month = input("Enter the month of the event: ")
day = input("Enter the day of the event: ")
now = datetime.now()
formatted_time = now.strftime("%B %d, %Y at %I:%M %p")

#THE OUTPUT
print("--- STUDENT EVENT REGISTRATION SUMMARY ---")
print("Name:", first.title(), last.title())
print("Name Code:", first.upper(), last.upper())
print(section)
print(event)
print("Language Used: Python")
print("String Feature Used: strip(), title(), upper()")
print("Date/Time Feature Used:", formatted_time )

#REFLECTION
#This Python program demonstrates how to effectively collect and gather user input and clean it using
# built-in string methods like .strip(), .title(), and .upper(). By automatically removing
# accidental spaces and standardizing capitalization, the code makes sure that names, sections,
# and event titles appear neat and consistent in the final registration summary. Overall,
# writing this script highlights how basic string manipulation can significantly improve data
# formatting and readability in simple interactive applications.