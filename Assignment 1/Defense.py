from datetime import datetime

def is_valid(date_string):
    try:
        parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
        print(parsed_date.date())
        return True
    except ValueError:
        return False

while True:
    user_input = input("Enter a date (YYYY-MM-DD): ")

    if is_valid(user_input):
        print("Valid date. Thank you!")
        break
    else:
        print("Invalid date. Please try again.")
