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


last_period = input("When did your last period start? (Please enter in DD/MM/YYYY format): ")

cycle_length = input("How many days is your average cycle?")
cycle_length = int(cycle_length)
period_length = input("How many days does your period usually last? ")
period_length = int(period_length)


print()

print("Hello", name)
print("Your last period started on", last_period)
print("Your average cycle is", cycle_length, "days.")
print("Your period usually lasts", period_length, "days.")

print(f"Hey, {name}! You’re doing amazing, girl. Be gentle with yourself, listen to your body, and remember, you’ve got this. 💕")
