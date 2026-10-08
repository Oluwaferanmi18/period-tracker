print("===================================")
print("      🌸🩸Period Tracker🩸🌸")
print("===================================")

name = input("Enter your name: ")
print(f"Hey, {name}! lets track your period.")
print()
print("Your cycle length is the number of days")
print("from the first day of one period to the day before")
print("your next period starts.")
print()


last_period = input("When did your last period start? (Please enter in DD/MM/YYYY format):  ")

while len(last_period) != 10 or last_period[2] != "/" or last_period[5] != "/":
    print("Please enter a valid date in DD/MM/YYYY format.")
    last_period = input("When did your last period start? (Please enter in DD/MM/YYYY format): ")

day = int(last_period[0:2])
month = int(last_period[3:5])
year = int(last_period[6:10])


days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

number_of_days = days_in_month[month - 1]

while True:
    try:
        cycle_length = input("How many days is your average cycle?")
        cycle_length = int(cycle_length)
        if cycle_length >= 21 and cycle_length <= 35:
            break
        else:
            print("Please enter a cycle length between 21 and 35 days.")

    except ValueError:
        print("Please enter a valid number.")

while True:
    try:
        period_length = input("How many days does your period usually last?  ")
        period_length = int(period_length)
        if period_length >= 1 and period_length <= 7:
            break
        else:
            print("Please enter a period length between 1 and 7 days.")
    except ValueError:
        print("Please enter a valid number.")

print()

print("Hello", name)
print("Your last period started on", last_period)
print("Your average cycle is", cycle_length, "days.")
print("Your period usually lasts", period_length, "days.")

print(f"Hey, {name}! You’re doing amazing, girl. Be gentle with yourself, listen to your body, and remember, you’ve got this. 💕")

